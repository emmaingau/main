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
import random


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1243))
s.connect(("127.0.0.1", 1243))


# Flask app should start in global layout
app = Flask(__name__)

appVersion = "EMMA v1.2"

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
    

    if action == "sportsAction":
        finalReply = sportsFunction(req, action)
        return(finalReply)
    elif action == "colorAction":
        finalReply = colorFunction(req, action)
        return(finalReply)
        


# ----------------------------------- REPLY HANDLER

def sportsFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("sportsName")
    replyList = ["Respuesta custom para Sports", 
                    "A mi también me gusta el "+ value, 
                    "Hacer deporte es bueno para la salud."]

    response = random.choice(replyList)
    print("Response is: " + response)
        
    jsonOut = {'fulfillmentText': response, 'DisplayText': response,}
    return (jsonOut)


def colorFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("colorName")
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


