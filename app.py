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
from listas import fallbackList
from listas import estacionesList



HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1243))
s.connect(("127.0.0.1", 9000))


# Flask app should start in global layout
app = Flask(__name__)

appVersion = "EMMA alpha 1.0"

@app.route('/webhook', methods=['POST'])

def webhook():
    req = request.get_json(silent=True, force=True)
    userSaid = req.get("queryResult").get("queryText")
    res = parameterEvaluator(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# ----------------------------------- PARAMETER EVALUATOR

def parameterEvaluator(req):

    action = req.get("queryResult").get("action")
    
    if action == "nameAction":
    	finalReply = namesFunction(req, action)
    	return(finalReply)
    elif action == "siConoceAction":
    	finalReply = siConoceFunction(req, action)
    	return(finalReply)
    elif action == "noConoceAction":
    	finalReply = noConoceFunction(req, action)
    	return(finalReply)
    elif action == "sportsAction":
        finalReply = sportsFunction(req, action)
        return(finalReply)
    elif action == "colorAction":
        finalReply = colorFunction(req, action)
        return(finalReply)
    elif action == "estacionDeporteAction":
        finalReply = sportsEstacionFunction(req, action)
        return(finalReply)
    elif action == "fallbackAction":
        finalReply = fallbackFunction(req, action)
        return(finalReply)


# ----------------------------------- REPLY HANDLER

def namesFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("names")
    dummy = "1 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    
  
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>Es un gusto" + value + "<break time='500ms'/>Estoy acá porque vine a intentar entender cómo funcionan los humanos. Yo vengo de la galaxia Circinus<break time='300ms'/> la conocés?</prosody></speak>"}]}}]}

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>¿" + value + "?.¡Que nombre tan genial!<break time='500ms'/> Estoy acá porque vine a intentar entender como piensan los humanos. Yo vengo de la galaxia Circinus<break time='300ms'/> la conocés?</prosody></speak>"}]}}]}

    azar = random.randrange(2)
    print(azar)
    if azar == 0:
    	return(jsonOut)
    if azar == 1:
    	return(jsonOut2)
    #jsonOut = {'fulfillmentText': response, 'DisplayText': response,}

def siConoceFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    dummy = "1 \n"
    s.send(dummy.encode())
  
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>Wow<break time='300ms'>Entonces debes saber que en Circinus nos encargamos de procesar información.<break time='500ms'/>Contame <break time='200ms'/>Vos trabajás <break time='200ms'/>o estudiás.</prosody></speak>"}]}}]}

    return(jsonOut)
   
def noConoceFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    dummy = "1 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    
  
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>No te preocupes.<break time='500ms'/>Sos del 99,9% de personas que no la conoce.<break time='500ms'/>Contame <break time='200ms'/>Vos trabajás <break time='200ms'/>o estudiás.</prosody></speak>"}]}}]}

    return(jsonOut)
    
def sportsFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("sportsName")
    s.send(value.encode())
    f = open("res/replylists/replySports.txt", "r")
    replyList = f.readlines()
    print(replyList)
    f.close()

    response = replyList[(random.randrange(3))]
    print("Response is: " + response)
    
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='default'>"+response+"</prosody></speak>"}]}}]}

    #jsonOut = {'fulfillmentText': response, 'DisplayText': response,}
    return (jsonOut)

def sportsEstacionFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("estacionName")
    s.send(value.encode())
    if value == "verano":
        response = estacionesList[0]
    elif value == "otoño":
        response = estacionesList[1]
    elif value == "invierno":
        response = estacionesList[2]
    elif value == "primavera":
        response = estacionesList[3]

    print("Response is: " + response)


    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='default'>"+ response +"<break time='400ms'/>En fin <break time='200ms'/> no me había dado cuenta de la hora,<break time='300ms'/> ya  tengo que  irme. gracias por venir a conocerme, y si querés podemos seguir en contacto a través de instagram<break time='200ms'/> nos vemos la proxima!</prosody></speak>"}]}}]}

    #jsonOut = {'fulfillmentText': response, 'DisplayText': response,}
    return (jsonOut)

def colorFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("colorName")
    dummy = "2 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    replyList = ["Respuesta custom para Color", 
                    "A mi también me gusta el "+ value, 
                    "Sabías que el color " + value + " significa alegría?"]

    response = random.choice(replyList)
    print("Response is: " + response)
    
    jsonOut = {'fulfillmentText': response, 'DisplayText': response,}
    return (jsonOut)

def fallbackFunction(req, action):
    response = fallbackList[random.randrange(3)]
    print("Response is: " + response)
    dummy = "0 \n"
    s.send(dummy.encode())
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='default'>"+response+"</prosody></speak>"}]}}]}

    return (jsonOut)

	


# ----------------------------------- STARTER
if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))

    print ("Starting app on port %d" %(port))


    app.run(debug=True, port=port, host='0.0.0.0')
    triggertest()

