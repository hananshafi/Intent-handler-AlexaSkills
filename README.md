# Intent-handler-AlexaSkills
This code is about extracting intents from the commands and then executing the required API's pertaining to the slot names in the intent.

Steps:
- Create a Skill in Alexa Skills console.
- Add intents and slot names to the skills, build the model and publish it.
- Host alexaskills.py in your system by making necessary changes. ( In my case I have used 'GoTo' Intent)
- With the help of ngrok create a webhook so that alexa skills console can communicate with your Hosted app. (link for ngrok: https://ngrok.com/)
- Add the webhook address to the End point in Alexa skills console.
