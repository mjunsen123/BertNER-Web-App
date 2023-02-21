# BertNER-Web-App

This is an ad-hoc project to quickly recap how to deploy a machine learning model. This project use pre-trained language model (bert-base-NER) for NER task. See more from the model source : https://huggingface.co/dslim/bert-base-NER. 

No fine-tuning is performed to the model and transformer pipelines is used for model inference for the sake of time (see more : https://huggingface.co/docs/transformers/main_classes/pipelines). Below is the output from the output with the input of "RGU is a university located in Aberdeen, south east part of Scotland". 
( PS: I know it's north east part of Scotland XD )

<kbd>
<img width="1240" alt="image" src="https://user-images.githubusercontent.com/37623890/219695853-f5e132ec-ab00-4535-9bd4-8631db29970c.png">
</kbd>

The colour set as follow : `ORG(green)`, `LOC(red)`, `PER(blue)` and `MISC(purple)`

## High-level workflow
### Model inference
1. `Flask` is used as web application framework and `Gunicorn` is used as the server gateway.
  1.1. Create a form in `index.html` (front-end) which serve as the text input
  1.2. Create an `app.py` (back-end) which take the input from front end
2. Load the pre-trained model `AutoModelForTokenClassification` and tokenizer `AutoTokenizer` by using HuggingFace.
3. Tokenize the input and feed to the model for inference by using `pipeline` from transformer library.
4. Post-process the output result (see postProcessing function)
Raw result 

"[{'entity': 'B-ORG',
  'score': 0.99754566,
  'index': 1,
  'word': 'R',
  'start': 0,
  'end': 1},
 {'entity': 'I-ORG',
  'score': 0.9739576,
  'index': 2,
  'word': '##G',
  'start': 1,
  'end': 2},
 {'entity': 'I-ORG',
  'score': 0.9781341,
  'index': 3,
  'word': '##U',
  'start': 2,
  'end': 3},
 {'entity': 'B-LOC',
  'score': 0.99568594,
  'index': 9,
  'word': 'Aberdeen',
  'start': 31,
  'end': 39},
 {'entity': 'B-LOC',
  'score': 0.9995809,
  'index': 15,
  'word': 'Scotland',
  'start': 60,
  'end': 68}]"
  
6. Transform the processed JSON result to HTML by highlighting the keyword with different colours (see highlightWord function).
7. Return the transformed HTML
### Model deployment
1. Test the model from local host (`flask run` command from terminal)
2. Once inference made successfully, ready to deploy.
3. THe easiest way is deploy via heroku as the process is very straight forward. However, 


Latest update (19/02/2023) : Work on local environment but failed on both Heroku and AWS Elastic BeanStalk (memory issue)

Update Heroku (memory error)
<img width="1156" alt="image" src="https://user-images.githubusercontent.com/37623890/219966869-0152ac29-53da-4fb5-b4d4-8cb065641289.png">

Update Elastic BeanStalk (same memory error)
"web: RuntimeError: [enforce fail at alloc_cpu.cpp:75] err == 0. DefaultCPUAllocator: can't allocate memory: you tried to allocate 2359296 bytes. Error code 12 (Cannot allocate memory)"

Latest Update (Elastic BeanStalk)
Manage to deploy on elastic beanstalk, with t2.medium instance (not free tier).
Link :  http://bert-ner-env.eba-wfszxiqr.eu-west-2.elasticbeanstalk.com
As the instance is charged per hour, please contact me via email yee_js@hotmail.com if demo required. Thank you.
