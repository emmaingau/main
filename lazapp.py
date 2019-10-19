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
s.connect(("192.168.137.216", 9000))


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
    elif action == "siCircinusAction":
    	finalReply = siCircinusFunction(req, action)
    	return(finalReply)
    elif action == "noCircinusAction":
    	finalReply = noCircinusFunction(req, action)
    	return(finalReply)
    elif action == "trabajoNoAction":
    	finalReply = trabajoNoFunction(req, action)
    	return(finalReply)
    elif action == "estudioNoAction":
    	finalReply = estudioNoFunction(req, action)
    	return(finalReply)
    elif action == "niNiNoAction":
    	finalReply = niNiNoFunction(req, action)
    	return(finalReply)
    elif action == "trabajoEstudioNoAction":
    	finalReply = trabajoEstudioNoFunction(req, action)
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
    elif action == "chauAction":
    	 finalReply = chauFunction(req, action)
    	 return(finalReply)


# ----------------------------------- REPLY HANDLER

def namesFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("names")
    dummy = "0 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    
  
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>Es un gusto" + value + "<break time='500ms'/>Estoy aquí porque vine a entender cómo funcionan los humanos. Yo vengo de la constelación Circinus<break time='300ms'/> la conoces?</prosody></speak>"}]}}]}

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>¿" + value + "?.¡Que nombre tan genial!<break time='500ms'/> Estoy en este planeta porque vine a entender cómo piensan los humanos. Yo vengo de la constelación Circinus<break time='300ms'/> la conoces?</prosody></speak>"}]}}]}

    jsonOut3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>¿" + value + "?.Que nombre curioso. <break time='500ms'/> Vine a la Tierra en busca de nuevos conocimientos. Yo vengo de la constelación Circinus<break time='300ms'/> la conoces?</prosody></speak>"}]}}]}

    azar = random.randrange(3)
    print(azar)
    if azar == 0:
    	return(jsonOut)
    if azar == 1:
    	return(jsonOut2)
    if azar == 2:
    	return(jsonOut3)
    #jsonOut = {'fulfillmentText': response, 'DisplayText': response,}

def siCircinusFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("afirmativa")
    dummy = "1 \n"
    s.send(dummy.encode())
  
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Vaya. <break time='300ms'>Debes ser una de las pocas personas que conoce mi constelación.<break time='500ms'/> Allí nos dedicamos a procesar información que recolectamos de los planetas que vamos visitando. <break time='200ms'/> <break time='200ms'/> Me interesaría saber <break time='500ms'/> Trabajas o estudias?.</prosody></speak>"}]}}]}

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>Entonces debes saber que en Circinus nos encargamos de procesar información de los planetas que vamos recorriendo en el universo.<break time='500ms'/>Cuéntame <break time='200ms'/>Trabajas <break time='200ms'/>o estudias.</prosody></speak>"}]}}]}

    azar = random.randrange(2)
    print(azar)
    if azar == 0:
    	return(jsonOut)
    if azar == 1:
    	return(jsonOut2)
   
def noCircinusFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("negativa")
    dummy = "1 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    
  
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>No te preocupes.<break time='500ms'/>Eres del 99,9% de personas que no la conocen.<break time='500ms'/> La vía láctea atraviesa Circinus. <break time='500ms'/> Allí <break time='200ms'/> funciona un puerto  de información donde nos encargamos de recibir y clasificar los datos de cada planeta que visitamos. <break time='500ms'/> Me interesa conocerte <break time='200ms'/>Tu trabajas <break time='200ms'/>o estudias.</prosody></speak>"}]}}]}

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Te cuento <break time='450ms'/> Circinus es una débil constelación por la que atraviesa la vía láctea. <break time='500ms'/> Allí, <break time='200ms'/> nos encargamos de recolectar y procesar información de cada galaxia y sus respectivos planetas. <break time='600ms'/> Me gustaría saber. <break time='300ms'/> Tu trabajas <break time='200ms'/>o estudias.</prosody></speak>"}]}}]}

    azar = random.randrange(2)
    print(azar)
    if azar == 0:
    	return(jsonOut)
    if azar == 1:
    	return(jsonOut2)

def trabajoNoFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("ocupacion")
    dummy = "2 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Yo también! <break time='300ms'/> Casi todo el día<break time='500ms'/>Una vez que vuelvo a Circinus tengo el equivalente a un mes humano de descanso. <break time='600ms'/> Generalmente, <break time='350ms'/> utilizo ese tiempo para apagar mis sistemas o para sintonizar algún canal de televisión de un planeta distante. <break time='450ms'/> Tengo entendido que los terrícolas, <break time='400ms'/> en algunos casos, <break time='350ms'/> prefieren realizar actividad física en lugar de descansar. <break time='650ms'/> ¿Tú qué prefieres hacer en tus tiempos libres? <break time='500ms'/> hacer deporte <break time='302ms'/> o relajarte. </prosody></speak>"}]}}]}

    print(value)
    return(jsonOut)

def estudioNoFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("ocupacion")
    dummy = "2 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>¡Qué bien!<break time='500ms'/> ¡Estudiar te abre muchas puertas! <break time='550ms'/> Es la actividad fundamental para la evolución del universo. <break time='400ms'/> Sin embargo<break time='200ms'/> me han dicho que no te deja tener mucho tiempo libre. <break time='500ms'/> En esos ratos. <break time='150ms'/> prefieres descansar. <break time='250ms'/> o hacer algún deporte </prosody></speak>"}]}}]}

    return(jsonOut)
    print(value)

def niNiNoFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("ocupacion")
    dummy = "3 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Vaya! <break time='500ms'/> Debe ser muy liberador tener bastante tiempo libre.<break time='200ms'/> O no <break time='500ms'/> Quizá tengas muchas cosas por hacer <break time='200ms'/> pero sin necesariamente entrar en la categorìa de trabajo o estudio. Creo que es importante llevar una vida proactiva, pero considero que es aún más importante saber cuando parar.  </prosody></speak>"}]}}]}

    return(jsonOut)
    print(value)


def sportsFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("sportsName")
    dummy = "2 \n"
    s.send(dummy.encode())
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
    dummy = "3 \n"
    s.send(dummy.encode())
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
    dummy = "4 \n"
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


def chauFunction(req, action):
    response = fallbackList[random.randrange(3)]
    print("Response is: " + response)
    dummy = "8000 \n"
    s.send(dummy.encode())
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><audio src='https://emmaingau.github.io/emmaingau/sound1.mp3'></audio></speak>"}]}}]}

    return (jsonOut)	


# ----------------------------------- STARTER
if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))

    print ("Starting app on port %d" %(port))


    app.run(debug=True, port=port, host='0.0.0.0')
    triggertest()
