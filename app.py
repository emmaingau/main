#!/usr/bin/env python

import random
import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response
import socket
import time
import numpy
import keyboard


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1243))
s.connect(("127.0.0.1", 1243))


# Flask app should start in global layout
app = Flask(__name__)

appVersion = "EMMA alpha"

@app.route('/webhook', methods=['POST'])

def webhook():
    req = request.get_json(silent=True, force=True)
    userSaid = req.get("queryResult").get("queryText")
    print('\n' + "NEW QUERY -----------------------------------------------------------------------------")
    print("Request was: " + userSaid)


    #print(json.dumps(req, indent=4))

    res = parameterEvaluator(req)

    res = json.dumps(res, indent=4)
    print("END QUERY -----------------------------------------------------------------------------" + '\n')
    r = make_response(res)
    #print("Details: " + str(r))
    r.headers['Content-Type'] = 'application/json'
    return r

# ----------------------------------- PARAMETER EVALUATOR

def parameterEvaluator(req):

    action = req.get("queryResult").get("action")
    print(action + " detected")
    
    if action == "nameAction":
    	finalReply = namesFunction(req, action)
    	return(finalReply)
    elif action == "sportsAction":
        finalReply = sportsFunction(req, action)
        return(finalReply)
    elif action == "colorAction":
        finalReply = colorFunction(req, action)
        return(finalReply)
        


# ----------------------------------- REPLY HANDLER

def namesFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("names")
    s.send(value.encode())
    #f = open("replySports.txt", "r")
    #replyList = f.readlines()
    #print(replyList)
    #f.close()

    response = "Es un gusto " + value + ". Estoy acá porque vine a intentar entender cómo funcionan los humanos. Yo vengo de la galaxia Circinus. ¿La conoces?"
    print("Response is: " + response)
    
    #SSML response bitch!
    #jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='default' pitch='+1st'>"+ response +"</prosody></speak>"}]}}]}

    jsonOut = {'fulfillmentText': response, 'DisplayText': response,}
    return (jsonOut)

def sportsFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("sportsName")
    s.send(value.encode())
    f = open("replySports.txt", "r")
    replyList = f.readlines()
    print(replyList)
    f.close()

    response = replyList[(random.randrange(3))]
    print("Response is: " + response)
    
    #SSML response bitch!
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='default' pitch='+2st'>"+ response +"</prosody></speak>"}]}}]}

    #jsonOut = {'fulfillmentText': response, 'DisplayText': response,}
    return (jsonOut)


def colorFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("colorName")
    s.send(value.encode())
    replyList = ["Respuesta custom para Color", 
                    "A mi también me gusta el "+ value, 
                    "Sabías que el color " + value + " significa alegría?"]

    response = random.choice(replyList)
    print("Response is: " + response)
    
    jsonOut = {'fulfillmentText': response, 'DisplayText': response,}
    return (jsonOut)




	


# ----------------------------------- STARTER
if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))

    print ("Starting app on port %d" %(port))


    app.run(debug=True, port=port, host='0.0.0.0')
    triggertest()


