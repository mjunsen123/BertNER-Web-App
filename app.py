import flask
import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import json
import re

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

def postProcessing(input):
        
        languageModel = pipeline("ner", model=model, tokenizer=tokenizer)
        ner_results = languageModel(input)

        counter = 0
        for index in range(len(ner_results)):
            ner_results[index]["parentEntity"] = ner_results[index]["entity"][-3:]
            if ner_results[index]["entity"][0] == "B":
                ner_results[index]["beginning"] = True
                counter += 1
            else:
                ner_results[index]["beginning"] = False
            ner_results[index]["groupNER"] = counter

        df = pd.DataFrame(ner_results)
        df['word'] = df.groupby(['groupNER'])['word'].transform(lambda x: ' '.join(x))
        df['word'] = df['word'].apply(lambda x: x.replace('#',''))
        df['word'] = df['word'].apply(lambda x: x.replace(' ',''))
        
        df = df[df['beginning']==True]
        df = df[["parentEntity","word"]]
        js = df.to_json(orient = "records")
        return js

def highlightWord(js,text):

    colors = {
            'ORG': 'green',
            'LOC': 'red',
            'PER': 'blue',
            'MISC': 'purple'
        }

    json_data = json.loads(js)
    
    words = re.findall(r'\w+|[^\w\s]+', text)
    highlighted_words = []
    for word in words:
        highlighted = False
        for item in json_data:
            if item['word'] == word:
                highlighted_words.append(f'<mark style="background-color: {colors[item["parentEntity"]]}">{word}</mark>')
                highlighted = True
                break
        if not highlighted:
            highlighted_words.append(word)
    highlighted_text = ' '.join(highlighted_words)

    return highlighted_text

app = flask.Flask(__name__, template_folder='html')
@app.route('/', methods=['GET', 'POST'])

def index():

    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        input = flask.request.form['input']
        jsonResult = postProcessing(input)
        htmlResult = highlightWord(jsonResult,input)
        return flask.render_template('index.html', result=htmlResult, original_input=input)

if __name__ == "__main__":
    app.run(debug=True)