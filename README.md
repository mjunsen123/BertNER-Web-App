# BertNER-Web-App

<img width="1240" alt="image" src="https://user-images.githubusercontent.com/37623890/219695853-f5e132ec-ab00-4535-9bd4-8631db29970c.png">

Below is the colour set:

'ORG': 'green',
'LOC': 'red',
'PER': 'blue',
'MISC': 'purple'

Latest update (19/02/2023) : Work on local environment but failed on both Heroku and AWS Elastic BeanStalk (memory issue)

Update Heroku (memory error)
<img width="1156" alt="image" src="https://user-images.githubusercontent.com/37623890/219966869-0152ac29-53da-4fb5-b4d4-8cb065641289.png">

Update Elastic BeanStalk (same memory error)
"web: RuntimeError: [enforce fail at alloc_cpu.cpp:75] err == 0. DefaultCPUAllocator: can't allocate memory: you tried to allocate 2359296 bytes. Error code 12 (Cannot allocate memory)"

Latest Update (Elastic BeanStalk)
Manage to deploy on elastic beanstalk, with t2.medium instance (not free tier).
Link :  http://bert-ner-env.eba-wfszxiqr.eu-west-2.elasticbeanstalk.com
As the instance is charged per hour, please contact me via email yee_js@hotmail.com if demo required. Thank you.