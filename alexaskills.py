import logging
from flask import Flask, session, request
from flask_ask import Ask, statement, context, session, question
import json
from executor import ToyotaExecutor
from config import SLOT_MAP
app = Flask(__name__)
ask = Ask(app,"/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)



@ask.launch
def launched():
    return question('Welcome to Dev Skills')



@ask.intent("GoTo")
def GoTo():
    req = request.data
    req_decode = req.decode('utf-8')
    value = json.loads(req_decode)
    requestValue = value['request']
    intent = requestValue['intent']
    SlotName = intent['slots']['Screen']['value']
    resp = "Executing your request for {}".format(SlotName)
    -- Call required API's --
    return statement(resp)

if __name__ == "__main__":
    app.run(debug=True)

