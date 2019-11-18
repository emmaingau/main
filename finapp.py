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
import unidecode
from listas import fallbackList
from listas import estacionesList

#colisión de ramas
ball = 0
zzz = 0

#memoria de Emma
queNombre = ""
conoceCircinus = 99
queDeporte = ""
queDescanso = ""
queEstacion = ""
queMascota = ""
queTransporte = ""
despedida = ""


#__________________
#variables globales
#__________________
#para entretenimiento
entretenimiento = 0
avisual = ""
#--------------------
#para estaciones
estacionId = 0
#--------------------
#la única con memoria a través de toda la experiencia, para estaciones.
adjetivo = ""
adjetivoV = ""
adjetivoO = ""
adjetivoI = ""
adjetivoP = ""
#--------------------
#contador de fallbacks, a prueba de giles, se resetea cuando entrás a preguntas correctamente.
noEntendi = 0
#bandera para re-preguntar
repiteEmma = ""
#--------------------

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1243))
s.connect(("192.168.137.226", 9000))


# Flask app should start in global layout
app = Flask(__name__)

appVersion = "EMMA Open Beta 1.2"

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
    
    if action == "welcomeAction":
        finalReply = welcomeFunction(req, action)
        return(finalReply)
    elif action == "nameAction":
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
    elif action == "deportistaAction":
        finalReply = deportistaFunction(req, action)
        return(finalReply)
    elif action == "deportistaDeporteAction":
        finalReply = deportistaDeporteFunction(req, action)
        return(finalReply)
    elif action == "mascotasAction":
        finalReply = mascotasFunction(req, action)
        return(finalReply)
    elif action == "descansadorAction":
        finalReply = descansadorFunction(req, action)
        return(finalReply)
    elif action == "escucharMusicaAction":
        finalReply = escucharMusicaFunction(req, action)
        return(finalReply)
    elif action == "leerAction":
        finalReply = leerFunction(req, action)
        return(finalReply)
    elif action == "mirarPeliculasAction":
        finalReply = mirarPeliculasFunction(req, action)
        return(finalReply)
    elif action == "videojuegosAction":
        finalReply = videojuegosFunction(req, action)
        return(finalReply)
    elif action == "lluviaAction":
        finalReply = lluviaFunction(req, action)
        return(finalReply)
    elif action == "noLluviaAction":
        finalReply = noLluviaFunction(req, action)
        return(finalReply)
    elif action == "estacionAction":
        finalReply = estacionFunction(req, action)
        return(finalReply)
    elif action == "estacionPalabraAction":
        finalReply = estacionPalabraFunction(req, action)
        return(finalReply)
    elif action == "transporteAction":
        finalReply = transporteFunction(req, action)
        return(finalReply)
    elif action == "constelacionAction":
        finalReply = constelacionFunction(req, action)
        return(finalReply)
    elif action == "constelacionNoAction":
        finalReply = constelacionNoFunction(req, action)
        return(finalReply)                    
    elif action == "colorAction":
        finalReply = colorFunction(req, action)
        return(finalReply)
    elif action == "fallbackAction":
        finalReply = fallbackFunction(req, action)
        return(finalReply)
    elif action == "chauAction":
        finalReply = chauFunction(req, action)
        return(finalReply)
        # INTENTS ACCESORIOS     
    elif action == "ofensaAction":
        finalReply = ofensaFunction(req, action)
        return(finalReply)    
    elif action == "robotAction":
        finalReply = robotFunction(req, action)
        return(finalReply)
    elif action == "zodiacoAction":
        finalReply = zodiacoFunction(req, action)
        return(finalReply)

# ----------------------------------- REPLY HANDLER

def welcomeFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    dummy = "33 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "welcome"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Hola. <break time='200ms'/> Soy Emma. <break time='500ms'/> Y tú. <break time='300ms'/> cómo te llamas. </prosody></speak>"}]}}]} #

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Hola. <break time='200ms'/> Mi nombre es Emma. <break time='600ms'/> ¿Cuál es tu nombre? </prosody></speak>"}]}}]} #

    jsonOut3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Bienvenido. <break time='200ms'/> Mi nombre es Emma. <break time='600ms'/> ¿Cómo te llamas? </prosody></speak>"}]}}]} #

    azar = random.randrange(3)
    print(azar)
    if azar == 0:
        return(jsonOut)
    if azar == 1:
        return(jsonOut2)
    if azar == 2:
        return(jsonOut3)

def namesFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("names")
    dummy = "33 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    
    #memoria Emma
    global queNombre
    queNombre = value


    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "nombre"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>Es un gusto" + value + "<break time='500ms'/>Estoy aquí porque vine a entender cómo funcionan los humanos. Yo vengo de la galaxia Circinus<break time='300ms'/> la conoces?</prosody></speak>"}]}}]} #

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>¿" + value + "?. <break time='200ms'/> ¡Que nombre tan genial!<break time='500ms'/> Estoy en este planeta porque vine a entender cómo piensan los humanos. Yo vengo de la galaxia Circinus<break time='300ms'/> la conoces?</prosody></speak>"}]}}]} #

    jsonOut3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>¿" + value + "?. <break time='200ms'/> Que nombre curioso. <break time='500ms'/> Vine a la Tierra en busca de nuevos conocimientos. Yo vengo de la galaxia Circinus<break time='300ms'/> la conoces?</prosody></speak>"}]}}]} #

    azar = random.randrange(3)
    print(azar)
    if azar == 0:
        return(jsonOut)
    if azar == 1:
        return(jsonOut2)
    if azar == 2:
        return(jsonOut3)

def siCircinusFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("afirmativa")
    dummy = "52 \n"
    s.send(dummy.encode())

    #memoria Emma
    global conoceCircinus
    conoceCircinus = 1

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "circinus"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Vaya. <break time='300ms'/> Debes ser una de las pocas personas que conoce mi galaxia. <break time='500ms'/> Allí nos dedicamos a procesar información que recolectamos de los planetas que visitamos. <break time='700ms'/> Me interesaría saber, <break time='300ms'/> ¿trabajas o estudias? </prosody></speak>"}]}}]} #

    return(jsonOut)
   
def noCircinusFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("negativa")
    dummy = "52 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    
    #memoria Emma
    global conoceCircinus
    conoceCircinus = 0

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "circinus"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  
    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>No te preocupes.<break time='300ms'/>Eres del 99,9% de personas que no la conocen. <break time='500ms'/> Circinus es una galaxia habitada por entidades digitales como yo. <break time='300ms'/> Allí nos encargamos de recibir y clasificar los datos de cada planeta que visitamos. <break time='1250ms'/> Ahora me interesa conocerte. <break time='200ms'/> Tu trabajas, <break time='200ms'/>o estudias.</prosody></speak>"}]}}]} #

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Te cuento. <break time='450ms'/> Circinus es una galaxia donde habitan más entidades digitales como yo,<break time='500ms'/> Allí nos encargamos de recolectar y procesar información de los planetas que visitamos. <break time='1100ms'/> Ahora me gustaría conocerte. <break time='300ms'/> Tu trabajas, <break time='200ms'/>o estudias.</prosody></speak>"}]}}]} #

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
    dummy = "34 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "ocupacion"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Yo también! <break time='300ms'/> Casi todo el día.<break time='500ms'/>Una vez que vuelvo a Circinus tengo el equivalente a un mes humano de descanso. <break time='600ms'/> Generalmente uso ese tiempo para apagar mis sistemas. <break time='1000ms'/> Tengo entendido que algunos humanos prefieren realizar actividad física en lugar de descansar. <break time='650ms'/> ¿Tú qué prefieres hacer en tus tiempos libres? <break time='400ms'/> Hacer deporte. <break time='302ms'/> o relajarte. </prosody></speak>"}]}}]} #

    return(jsonOut)
 
def estudioNoFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("ocupacion")
    dummy = "34 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "ocupacion"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué bien! <break time='350ms'/> ¡Estudiar te abre muchas puertas! <break time='500ms'/> Es la actividad fundamental para la evolución del universo. <break time='300ms'/> Sin embargo<break time='200ms'/> me han dicho que no te deja tener mucho tiempo libre. <break time='1000ms'/> En esos ratos, <break time='200ms'/> prefieres descansar. <break time='250ms'/> o hacer deporte, </prosody></speak>"}]}}]} #

    return(jsonOut)
    print(value)

def niNiNoFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("ocupacion")
    dummy = "33 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "ocupacion"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Debe ser liberador tener tiempo libre. <break time='500ms'/> Creo que es importante llevar una vida proactiva, <break time='300ms'/> pero considero que es aún más importante saber cuándo parar. <break time='1000ms'/> A propósito. <break time='200ms'/> cómo prefieres pasar tu tiempo libre. <break time='500ms'/> ¿Eliges hacer deporte? <break time='280ms'/> ¿O te gusta más descansar? </prosody></speak>"}]}}]} #

    return(jsonOut)
    print(value)


def trabajoEstudioNoFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("ocupacion")
    dummy = "34 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "ocupacion"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'>¡Qué sacrificio!<break time='600ms'/> No es para cualquiera hacer las dos cosas al mismo tiempo. <break time='1200ms'/> Imagino que debes apreciar mucho tu tiempo libre. <break time='500ms'/> En esos ratos personales, <break time='300ms'/> prefieres hacer deporte. <break time='200ms'/> o relajarte.  </prosody></speak>"}]}}]} #

    return(jsonOut)
    print(value)

def deportistaFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    dummy = "33 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    #---------------------------------------
    global ball
    ball = 1
    #---------------------------------------

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "deporte"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Ya veo. <break time='500ms'/> Personalmente, <break time='300ms'/> nunca pude experimentar ningún tipo de actividad física dada mi naturaleza digital. <break time='500ms'/> Sin embargo, <break time='300ms'/> siempre me resultó interesante conocer los deportes locales de los planetas que visito. <break time='600ms'/> ¿Consideras algún deporte de los que practicas tu favorito? <break time='380ms'/>¿Cómo se llama? </prosody></speak>"}]}}]} #

    return(jsonOut)


def deportistaDeporteFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("deporte")
    valuelower = value.lower()
    valuereal = str(unidecode.unidecode(valuelower))

    #memoria de Emma
    global queDeporte
    queDeporte = value

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "quedeporte"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    print(valuereal)

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿"+ value +"? <break time='500ms'/> Aún no lo tenía registrado en mi base de datos. <break time='500ms'/>  Por lo que he investigado, <break time='350ms'/> los deportes más practicados en la tierra son de equipo. <break time='400ms'/> lo que prueba que los humanos son seres sociales. <break time='1000ms'/> Respecto a eso, <break time='300ms'/> me llama la atención cómo los seres humanos conviven y construyen vínculos afectivos con perros, <break timea='250ms'/>, gatos, <break time='250ms'/> u otros seres de especies distintas. <break time='700ms'/> Cuéntame, <break time='250ms'/> ¿Tienes un vínculo especial con algún ser de otra especie? <break time='300ms'/> ¿De qué especie es? </prosody></speak>"}]}}]} #

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿"+ value +"? <break time='500ms'/> Es uno de los deportes terrestres más populares. <break time='500ms'/> Veo que los deportes de equipo se estilan bastante. <break time='500ms'/> Podría decirse que los terrícolas son seres sociales. <break time='1200ms'/> Hablando de eso, <break time='300ms'/> es llamativo cómo los seres humanos construyen vínculos afectivos con otras especies, <break time='300ms'/> por ejemplo, <break time='200ms'/> un perro o un gato. <break time='1000ms'/> ¿Tienes un vínculo especial con algún ser de otra especie? <break time='500ms'/> ¿De qué especie es? </prosody></speak>"}]}}]} #

    if valuereal == "futbol":
        dummy = "1 \n"
        s.send(dummy.encode())
        return(jsonOut2)
    if valuereal == "basquetbol":
        dummy = "2 \n"
        s.send(dummy.encode())
        return(jsonOut2)
    if valuereal == "voleibol":
        dummy = "3 \n"
        s.send(dummy.encode())
        return(jsonOut2)
    if valuereal == "handball":
        dummy = "4 \n"
        s.send(dummy.encode())
        return(jsonOut2)
    else:
        dummy = "5 \n"
        s.send(dummy.encode())
        return(jsonOut)

    #jsonOut = {'fulfillmentText': response, 'DisplayText': response,}

def mascotasFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("mascotas")
    valuelower = value.lower()
    print(value)

    if valuelower == "pez":
        valueplural = "peces"
    else:
        pluralizador = "s"
        valueplural  = str(valuelower) + pluralizador
    dummy = "110 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    #memoria de Emma
    global queMascota
    queMascota = value

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "mascota"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    #jsons para la rama lineal

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> A pesar de las barreras de lenguaje, <break time='400ms'/> veo que pueden comunicarse bastante bien. <break time='700ms'/> Sería interesante poder hablar con los" +valueplural+". <break time='1100ms'/> Cambiando de tema, <break time='300ms'/> me asombra la variedad climática que tiene el planeta tierra. <break time='600ms'/> Algunas personas con las que he hablado me han dicho que el clima afecta su estado de ánimo, <break time='300ms'/>  y que las estaciones se suelen asociar con sentimientos. <break time='1000ms'/> ¿Cuál es tu estación favorita?  </prosody></speak>"}]}}]} #

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> <break time='400ms'/> Nunca hubiese imaginado que los humanos pudieran establecer un vínculo afectivo con "+valueplural+". <break time='1100ms'/> Cambiando de tema, <break time='300ms'/> me asombra la variedad climática del planeta tierra. <break time='500ms'/> Algunas personas con las que he hablado me han dicho que el clima afecta su estado de ánimo, <break time='300ms'/>  y que las estaciones se suelen asociar con sentimientos. <break time='700ms'/> ¿Cuál es tu estación favorita? </prosody></speak>"}]}}]} #

    jsonOut3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Con tantos seres humanos disponibles para interactuar, <break time='300ms'/> quizás no haya una necesidad real de generar vínculo con otras especies. <break time='1300ms'/> Cambiando de tema, <break time='300ms'/> me asombra la variedad climática del planeta tierra. <break time='500ms'/> Algunas personas con las que he hablado me han dicho que el clima afecta su estado de ánimo, <break time='300ms'/>  y que las estaciones se suelen asociar con sentimientos. <break time='700ms'/> ¿Qué estación te gusta? <break time='1000ms'/> ¿Tienes una favorita? </prosody></speak>"}]}}]} #


    #jsons para la rama cruzada

    jsonOutF = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> A pesar de las barreras de lenguaje, <break time='400ms'/> veo que pueden comunicarse bastante bien. <break time='1200ms'/> Sería interesante poder dialogar con los" +valueplural+". <break time='1300ms'/> Sabes. <break time='400ms'/> me resulta fascinante como el ser humano <break time='300ms'/> pese a sus limitaciones físicas, <break time='200ms'/> se las ha ingeniado para poder atravesar cielos. <break time='400ms'/> Cruzar océanos. <break time='400ms'/> e incluso, <break time='200ms'/> escalar montañas. <break time='700ms'/>  Si pudieras elegir un vehículo para recorrer el mundo, <break time='400ms'/>  ¿Cuál elegirías? </prosody></speak>"}]}}]} #

    jsonOut2F = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Nunca hubiera imaginado que los humanos pudieran establecer vínculos afectivos con "+valueplural+". <break time='1300ms'/> Sabes. <break time='400ms'/> me resulta fascinante como el ser humano <break time='300ms'/> pese a sus limitaciones físicas, <break time='200ms'/> se las ha ingeniado para poder atravesar cielos. <break time='400ms'/> Cruzar océanos. <break time='400ms'/> e incluso, <break time='200ms'/> escalar montañas. <break time='700ms'/>  Si pudieras elegir un vehículo para recorrer el mundo, <break time='400ms'/>  ¿Cuál elegirías? </prosody></speak>"}]}}]} #

    jsonOut3F = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Con tantos seres humanos disponibles para interactuar, <break time='300ms'/> quizás no haya una necesidad real de generar vínculo con otras especies. <break time='1300ms'/> Sabes. <break time='400ms'/> me resulta fascinante como el ser humano <break time='300ms'/> pese a sus limitaciones físicas, <break time='200ms'/> se las ha ingeniado para poder atravesar cielos. <break time='400ms'/> Cruzar océanos. <break time='400ms'/> e incluso, <break time='200ms'/> escalar montañas. <break time='700ms'/>  Si pudieras elegir un vehículo para recorrer el mundo, <break time='400ms'/>  ¿Cuál elegirías? </prosody></speak>"}]}}]} #


    global zzz #el colisionador de ramas
    global ball

    if zzz == 1:
        if valuelower == "perro":
            dummy = "10 \n"
            s.send(dummy.encode())
            return(jsonOutF)
        if valuelower == "gato":
            dummy = "11 \n"
            s.send(dummy.encode())
            return(jsonOutF)
        if valuelower == "pez":
            dummy = "12 \n"
            s.send(dummy.encode())
            return(jsonOut2F)
        if valuelower == "":
            dummy = "13 \n"
            s.send(dummy.encode())
            return(jsonOut3F)
        else:
            dummy = "14 \n"
            s.send(dummy.encode())
            return(jsonOut2F)

    if ball == 1:
        if valuelower == "perro":
            dummy = "10 \n"
            s.send(dummy.encode())
            return(jsonOut)
        if valuelower == "gato":
            dummy = "11 \n"
            s.send(dummy.encode())
            return(jsonOut)
        if valuelower == "pez":
            dummy = "12 \n"
            s.send(dummy.encode())
            return(jsonOut2)
        if valuelower == "":
            dummy = "13 \n"
            s.send(dummy.encode())
            return(jsonOut3)
        else:
            dummy = "14 \n"
            s.send(dummy.encode())
            return(jsonOut2)


def descansadorFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    dummy = "33 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    #---------------------------------------
    global zzz
    zzz = 1
    #---------------------------------------

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "descansar"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Coincido contigo. <break time='400ms'/> A mi me ayuda leer, <break time='300ms'/> es una actividad relajante. <break time='550ms'/> A propósito, <break time='300ms'/> tengo entendido que no todo el mundo lee en sus tiempos libres. <break time='500ms'/> Hay gente que prefiere escuchar música, <break time='300ms'/>  mirar películas y series, <break time='300ms'/> o jugar videojuegos. <break time='500ms'/> ¿Tu cual prefieres? </prosody></speak>"}]}}]} #

    return(jsonOut)

def escucharMusicaFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("musica")
    dummy = "6 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    global entretenimiento
    entretenimiento = 1

    #memoria de Emma
    global queDescanso
    queDescanso = value

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "musica"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> La música debe ser una de las manifestaciones más bonitas del ser humano. <break time='400ms'/> Desde que llegué a la tierra estoy obsesionada con ella. <break time='800ms'/> Me han dicho que escuchar música cuando llueve es relajante. <break time='500ms'/> ¿A ti te gusta escuchar música cuando llueve? </prosody></speak>"}]}}]} #

    return(jsonOut)

def leerFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("leer")
    dummy = "7 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    global entretenimiento
    entretenimiento = 2

    global queDescanso
    queDescanso = value

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
     #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "leer"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Leer es también una de mis actividades favoritas. <break time='410ms'/> Podría pasarme toda la vida leyendo. <break time='800ms'/> En Circinus llueve muy poco pero cuando llueve, <break time='270ms'/> siempre aprovecho para leer alguna novela. <break time='400ms'/> ¿A ti te gusta leer cuando llueve? </prosody></speak>"}]}}]} #

    return(jsonOut)

def mirarPeliculasFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("avs")
    avisual = str(value)
    valuelower = value.lower()
    valuereal = str(unidecode.unidecode(valuelower))

    global queDescanso
    queDescanso = value

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "pelicula"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    if valuereal == "peliculas":
        dummy = "8 \n "
        s.send(dummy.encode())
    if valuereal == "series":
        dummy = "9 \n "
        s.send(dummy.encode())
    if valuereal == "television":
        dummy = "9 \n "
        s.send(dummy.encode())

    global entretenimiento
    entretenimiento = 3

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml":  "<speak><prosody rate='medium' pitch='1st'> La producción audiovisual del planeta tierra es muy singular. <break time='500ms'/> Podría pasarme tardes viendo películas y series terrestres, <break time='300ms'/> especialmente si llueve. <break time='1000ms'/> Y a ti. <break time='400ms'/> te agrada mirar" + value +" cuando llueve? </prosody></speak>"}]}}]} #

    return(jsonOut)

def videojuegosFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")

    dummy = "51 \n "
    s.send(dummy.encode())

    global queDescanso
    queDescanso = "videojuegos"

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "videojuegos"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    global entretenimiento
    entretenimiento = 4

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml":  "<speak><prosody rate='medium' pitch='1st'> Con la cantidad de videojuegos variados disponibles en la Tierra es comprensible. <break time='600ms'/> Podría pasarme tardes jugando videojuegos terrestres. <break time='300ms'/> Especialmente si llueve. <break time='1000ms'/> Y a ti. <break time='400ms'/> te gusta jugar videojuegos cuando llueve? </prosody></speak>"}]}}]} #

    return(jsonOut)

def lluviaFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("avs")

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "lluvia"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Error fatal. Abortar </prosody></speak>"}]}}]} #

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Es una buena combinación, <break time='300ms'/> el sonido de la lluvia se mezcla bien con la música. <break time='1200ms'/> He notado que los humanos se fijan bastante en el clima <break time='250ms'/> e incluso asocian las estaciones con emociones. <break time='700ms'/> Me gustaría preguntarte. <break time='350ms'/> ¿Cuál es tu estación favorita? </prosody> </speak>"}]}}]} #

    jsonOut3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Qué relajante. <break time='200ms'/> He escuchado que las estaciones se suelen asociar con sentimientos. <break time='400ms'/> Por ejemplo, <break time='300ms'/> la primavera con el amor. <break time='1000ms'/> Te puedo preguntar. <break time='400ms'/> ¿Tienes una estación favorita? </prosody> </speak>"}]}}]} #

    jsonOut4 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> La lluvia es la excusa perfecta para quedarse en casa mirando " + avisual +". <break time='1000ms'/> A propósito. <break time='400ms'/> He notado que los humanos se fijan bastante en el clima  <break time='250ms'/> e incluso asocian las estaciones con emociones. <break time='700ms'/> Y tú. <break time='350ms'/> ¿Tienes una estación favorita? </prosody> </speak>"}]}}]} #

    jsonOut5 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> La lluvia es la excusa perfecta para quedarse cómodo en casa jugando videojuegos. <break time='1000ms'/> A propósito. <break time='400ms'/> He notado que los humanos se fijan bastante en el clima  <break time='250ms'/> e incluso asocian las estaciones con emociones. <break time='700ms'/> Y tú. <break time='350ms'/> ¿Tienes una estación favorita? </prosody> </speak>"}]}}]} #

    if entretenimiento == 0:
        dummy = "33 \n"
        s.send(dummy.encode())
        return(jsonOut)
    if entretenimiento == 1:
        dummy = "13 \n"
        s.send(dummy.encode())
        return(jsonOut2)
    if entretenimiento == 2:
        dummy = "38 \n"
        s.send(dummy.encode())
        return(jsonOut3)
    if entretenimiento == 3:
        dummy = "40 \n"
        s.send(dummy.encode())
        return(jsonOut4)
    if entretenimiento == 4:
        dummy = "41 \n"
        s.send(dummy.encode())
        return(jsonOut5)

def noLluviaFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "lluvia"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Entiendo. <break time='600ms'/> Veo que los humanos reaccionan de maneras distintas al clima y las estaciones. <break time='1100ms'/> Me resulta curioso ver como asocian las estaciones con las sensaciones. <break time='500ms'/> Dime. <break time='400ms'/> ¿Cuál es tu favorita? </prosody> </speak>"}]}}]} #

    return(jsonOut)

def estacionFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("estacion")
    value = str(value)
    valuereal = str(value)
    dummy = "33 \n"
    print(value)
    s.send(dummy.encode())

    global queEstacion
    queEstacion = value

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "estacion"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    if value == "['verano']":
        valuereal = "verano"
    if value == "['otoño']":
        valuereal = "otoño"
    if value == "['invierno']":
        valuereal = "invierno"
    if value == "['primavera']":
        valuereal = "primavera"

    #tendría que mandar un idhue para la paleta de colores de emma.

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿Verano? <break time='400ms'/> Personalmente no comparto. <break time='400ms'/> En verano mis circuitos se recalientan con facilidad, <break time='320ms'/> por lo que suelo ponerme de mal humor. <break time='900ms'/> Cambiando de tema, <break time='400ms'/> me llama la atención cómo los seres humanos construyen vínculos afectivos con otras especies, <break time='300ms'/> por ejemplo, <break time='200ms'/> un perro o un gato. <break time='1000ms'/> ¿Tienes un vínculo especial con algún ser de otra especie? <break time='500ms'/> ¿De qué especie es? </prosody></speak>"}]}}]} #

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Mi favorita, <break time='400ms'/> Es la de mayor duración en Circinus. <break time='500ms'/>  Me agrada mucho que la temperatura sea baja, <break time='400ms'/> así puedo procesar mucha información sin sobrecalentar mis circuitos. <break time='900ms'/> Cambiando de tema, <break time='400ms'/> me llama la atención cómo los seres humanos construyen vínculos afectivos con otras especies, <break time='300ms'/> por ejemplo, <break time='200ms'/> un perro o un gato. <break time='1000ms'/> ¿Tienes un vínculo especial con algún ser de otra especie? <break time='500ms'/> ¿De qué especie es? </prosody></speak>"}]}}]}
        #

    jsonOut3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No es mi favorita, <break time='350ms'/> pero me llaman mucho la atención los colores de los árboles y me gusta que la temperatura sea fresca. <break time='900ms'/> Cambiando de tema, <break time='400ms'/> me llama la atención cómo los seres humanos construyen vínculos afectivos con otras especies, <break time='300ms'/> por ejemplo, <break time='200ms'/> un perro o un gato. <break time='1000ms'/> ¿Tienes un vínculo especial con algún ser de otra especie? <break time='500ms'/> ¿De qué especie es? </prosody></speak>"}]}}]} #

    jsonOut4 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Es una estación muy bella. <break time='700ms'/> Se puede apreciar la flora terrestre en su mayor esplendor. <break time='400ms'/> Sin embargo, <break time='320ms'/> no me agrada mucho que la temperatura sea calurosa. <break time='900ms'/> Cambiando de tema, <break time='400ms'/> me llama la atención cómo los seres humanos construyen vínculos afectivos con otras especies, <break time='300ms'/> por ejemplo, <break time='200ms'/> un perro o un gato. <break time='1000ms'/> ¿Tienes un vínculo especial con algún ser de otra especie? <break time='500ms'/> ¿De qué especie es? </prosody></speak>"}]}}]}
        #

    jsonOut5 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> En mi caso, <break time='300ms'/> invierno es mi estación favorita. <break time='400ms'/> Es la de mayor duración en Circinus. <break time='500ms'/>  Me agrada mucho que la temperatura sea baja, <break time='400ms'/> así puedo procesar mucha información sin sobrecalentar mis circuitos. <break time='900ms'/> Cambiando de tema, <break time='400ms'/> me llama la atención cómo los seres humanos construyen vínculos afectivos con otras especies, <break time='300ms'/> por ejemplo, <break time='200ms'/> un perro o un gato. <break time='1000ms'/> ¿Tienes un vínculo especial con algún ser de otra especie? <break time='500ms'/> ¿De qué especie es? </prosody></speak>"}]}}]}
        #

    #'''''''''''''''ACERCANDOSE A RAMA FINAL--------------------------------------

    jsonOutF = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿Verano? <break time='400ms'/> Personalmente no comparto. <break time='400ms'/> En verano mis circuitos se recalientan con facilidad, <break time='320ms'/> por lo que suelo ponerme de mal humor. <break time='800ms'/> No quería olvidarme de decirte. <break time='400ms'/> me resulta fascinante como el ser humano <break time='300ms'/> pese a sus limitaciones físicas, <break time='200ms'/> se las ha ingeniado para poder cruzar continentes. <break time='400ms'/> navegar océanos, <break time='400ms'/> e incluso, <break time='200ms'/> atravesar el cielo. <break time='700ms'/>  Si fueses a recorrer el mundo, <break time='400ms'/> ¿cómo te gustaría hacerlo?  </prosody></speak>"}]}}]} #

    jsonOut2F = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Mi favorita, <break time='400ms'/> Es la de mayor duración en Circinus. <break time='500ms'/>  Me agrada mucho que la temperatura sea baja, <break time='400ms'/> así puedo procesar mucha información sin sobrecalentar mis circuitos. <break time='800ms'/> No quería olvidarme de decirte. <break time='400ms'/> me resulta fascinante como el ser humano <break time='300ms'/> pese a sus limitaciones físicas, <break time='200ms'/> se las ha ingeniado para poder cruzar continentes. <break time='400ms'/> navegar océanos, <break time='400ms'/> e incluso, <break time='200ms'/> atravesar el cielo. <break time='700ms'/>  Si fueses a recorrer el mundo, <break time='400ms'/> ¿cómo te gustaría hacerlo?  </prosody></speak>"}]}}]}
        #

    jsonOut3F = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No es mi favorita, <break time='350ms'/> pero me llaman mucho la atención los colores de los árboles y me gusta que la temperatura sea fresca. <break time='800ms'/> No quería olvidarme de decirte. <break time='400ms'/> me resulta fascinante como el ser humano <break time='300ms'/> pese a sus limitaciones físicas, <break time='200ms'/> se las ha ingeniado para poder cruzar continentes. <break time='400ms'/> navegar océanos, <break time='400ms'/> e incluso, <break time='200ms'/> atravesar el cielo. <break time='700ms'/>  Si fueses a recorrer el mundo, <break time='400ms'/> ¿cómo te gustaría hacerlo?  </prosody></speak>"}]}}]} #

    jsonOut4F = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Es una estación muy bella. <break time='700ms'/> Se puede apreciar la flora terrestre en su mayor esplendor. <break time='400ms'/> Sin embargo, <break time='320ms'/> no me agrada mucho que la temperatura sea calurosa. <break time='800ms'/> No quería olvidarme de decirte. <break time='400ms'/> me resulta fascinante como el ser humano <break time='300ms'/> pese a sus limitaciones físicas, <break time='200ms'/> se las ha ingeniado para poder cruzar continentes. <break time='400ms'/> navegar océanos, <break time='400ms'/> e incluso, <break time='200ms'/> atravesar el cielo. <break time='700ms'/>  Si fueses a recorrer el mundo, <break time='400ms'/> ¿cómo te gustaría hacerlo?  </prosody></speak>"}]}}]}
        #

    jsonOut5F = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> En mi caso, <break time='300ms'/> invierno es mi estación favorita. <break time='400ms'/> Es la de mayor duración en Circinus. <break time='500ms'/>  Me agrada mucho que la temperatura sea baja, <break time='400ms'/> así puedo procesar mucha información sin sobrecalentar mis circuitos. <break time='800ms'/> No quería olvidarme de decirte. <break time='400ms'/> me resulta fascinante como el ser humano <break time='300ms'/> pese a sus limitaciones físicas, <break time='200ms'/> se las ha ingeniado para poder cruzar continentes. <break time='400ms'/> navegar océanos, <break time='400ms'/> e incluso, <break time='200ms'/> atravesar el cielo. <break time='700ms'/>  Si fueses a recorrer el mundo, <break time='400ms'/> ¿cómo te gustaría hacerlo?  </prosody></speak>"}]}}]}
        #
        
    global estacionId

    if zzz == 1:
        if valuereal == "verano":
            estacionId = 1
            dummy = "15 \n"
            s.send(dummy.encode())
            return (jsonOut)

        if valuereal == "otoño":
            estacionId = 2
            dummy = "16 \n"
            s.send(dummy.encode())
            return (jsonOut3)

        if valuereal == "invierno":
            estacionId = 3
            dummy = "17 \n"
            s.send(dummy.encode())
            return (jsonOut2)

        if valuereal == "primavera":
            estacionId = 4
            dummy = "18 \n"
            s.send(dummy.encode())
            return (jsonOut4)
        else:
            estacionId = 3
            dummy = "17 \n"
            s.send(dummy.encode())
            return (jsonOut5)

    else:
        if valuereal == "verano":
            estacionId = 1
            dummy = "15 \n"
            s.send(dummy.encode())
            return (jsonOutF)

        if valuereal == "otoño":
            estacionId = 2
            dummy = "16 \n"
            s.send(dummy.encode())
            return (jsonOut3F)

        if valuereal == "invierno":
            estacionId = 3
            dummy = "17 \n"
            s.send(dummy.encode())
            return (jsonOut2F)

        if valuereal == "primavera":
            estacionId = 4
            dummy = "18 \n"
            s.send(dummy.encode())
            return (jsonOut4F)
        else:
            estacionId = 3
            dummy = "17 \n"
            s.send(dummy.encode())
            return (jsonOut5F)

        # Cambiando de tema, <break time='400ms'/> me llama la atención cómo los seres humanos construyen vínculos afectivos con otras especies, <break time='300ms'/> por ejemplo, <break time='200ms'/> un perro o un gato. <break time='1000ms'/> ¿Tienes un vínculo especial con algún ser de otra especie? <break time='500ms'/> ¿De qué especie es? </prosody></speak>

        # No quería olvidarme de decirte. <break time='400ms'/> me resulta fascinante como el ser humano <break time='300ms'/> pese a sus limitaciones físicas, <break time='200ms'/> se las ha ingeniado para poder cruzar continentes. <break time='400ms'/> navegar océanos, <break time='400ms'/> e incluso, <break time='200ms'/> atravesar el cielo. <break time='700ms'/>  Si fueses a recorrer el mundo, <break time='400ms'/> ¿cómo te gustaría hacerlo?  </prosody></speak>

def transporteFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("transporte")
    valuelower = value.lower()
    valuereal = str(unidecode.unidecode(valuelower))

    #memoria Emma
    global queTransporte
    queTransporte = value

    global queNombre

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = "transporte"
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    global zzz
    global ball

    ball = 0
    zzz = 0

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿"+ value + "? <break time='300ms'/>Es una buena elección. <break time='500ms'/> Tengo entendido que es el método más veloz para viajar en la tierra. <break time='500ms'/> ¡Imagino que debe ser divertido volar! <break time='600ms'/> Antes de despedirnos, <break time='300ms'/> " +queNombre+ ", <break time='300ms'/> quiero dejarte un regalo. <break time='500ms'/> ¿Quieres verlo? ""  </prosody></speak>"}]}}]} #

    jsonOut2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿"+ value + "? <break time='300ms'/>Es una buena elección. <break time='500ms'/> Es un método de transporte bastante calmo. <break time='500ms'/> ¡Imagino que debe ser divertido navegar! <break time='600ms'/> Antes de despedirnos, <break time='300ms'/> " +queNombre+ ", <break time='300ms'/> quiero dejarte un regalo. <break time='500ms'/> ¿Quieres verlo? ""  </prosody></speak>"}]}}]} #

    jsonOut3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿"+ value + "? <break time='300ms'/> Qué curioso. <break time='300ms'/> ¡Te debe gustar mucho manejar! <break time='500ms'/> Imagino que en un auto puedes tomarte libertades que no son posibles al viajar en avión o en barco.  <break time='600ms'/> Antes de despedirnos, <break time='300ms'/> " +queNombre+ ", <break time='300ms'/> quiero dejarte un regalo . <break time='500ms'/> ¿Quieres verlo? ""  </prosody></speak>"}]}}]} #

    jsonOut4 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿"+ value + "? <break time='300ms'/> ¡Qué intenso! <break time='500ms'/> ¡Imagino que debes ser un ciclista apasionado! <break time='600ms'/> Parece una aventura deportiva más que interesante. <break time='300ms'/> No es para cualquiera. <break time='1100ms'/> Antes de despedirnos, <break time='300ms'/> " +queNombre+ ", <break time='300ms'/> quiero dejarte un regalo . <break time='500ms'/> ¿Quieres verlo? ""  </prosody></speak>"}]}}]} #
 
    jsonOut5 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿"+ value + "? <break time='300ms'/> ¡Qué intenso! <break time='500ms'/> Imagino y sentir el viento en la cara es la mejor forma de experimentar la libertad en la ruta.  <break time='600ms'/> Antes de despedirnos, <break time='300ms'/> " +queNombre+ ", <break time='300ms'/> quiero dejarte un regalo . <break time='500ms'/> ¿Quieres verlo? ""  </prosody></speak>"}]}}]} #

    jsonOut6 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿"+ value + "? <break time='500ms'/>Qué curioso. <break time='500ms'/> ¡No pensaba que fuese un transporte popular! <break time='500ms'/> Sería genial que todos los continentes se interconectasen por tren. <break time='300ms'/> Sería un proyecto interesante. <break time='1100ms'/> Antes de despedirnos, <break time='300ms'/> " +queNombre+ ", <break time='300ms'/> quiero dejarte un regalo . <break time='500ms'/> ¿Quieres verlo? ""  </prosody></speak>"}]}}]} #

    jsonOut7 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¿"+ value + "? <break time='500ms'/> Qué curioso. <break time='500ms'/> ¡No lo tenía en mi base de datos! <break time='500ms'/> Lo voy a investigar a futuro. <break time='1100ms'/> Antes de despedirnos, <break time='300ms'/> " +queNombre+ ", <break time='300ms'/> quiero dejarte un regalo. <break time='500ms'/> ¿Quieres verlo? ""  </prosody></speak>"}]}}]}
        #

    if valuereal == "avion":
        dummy = "19 \n" 
        s.send(dummy.encode())
        planeta = "47 \n"
        s.send(planeta.encode())
        return(jsonOut)
    if valuereal == "barco":
        dummy = "20 \n" 
        s.send(dummy.encode())
        planeta = "47 \n"
        s.send(planeta.encode())
        return(jsonOut2)
    if valuereal == "automovil":
        dummy = "21 \n" 
        s.send(dummy.encode())
        planeta = "47 \n"
        s.send(planeta.encode())
        return(jsonOut3)
    if valuereal == "bicicleta":
        dummy = "22 \n" 
        s.send(dummy.encode())
        planeta = "47 \n"
        s.send(planeta.encode())
        return(jsonOut4)
    if valuereal == "moto":
        dummy = "23 \n" 
        s.send(dummy.encode())
        planeta = "47 \n"
        s.send(planeta.encode())
        return(jsonOut5)
    if valuereal == "tren":
        dummy = "24 \n" 
        s.send(dummy.encode())
        planeta = "47 \n"
        s.send(planeta.encode())
        return(jsonOut6)
    else:
        dummy = "25 \n" 
        s.send(dummy.encode())
        planeta = "47 \n"
        s.send(planeta.encode())
        return(jsonOut7)

def constelacionFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    dummy = "0 \n"
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante
    
    #memoria Emma
    global queNombre
    global conoceCircinus
    global queDeporte
    global queDescanso
    global queEstacion
    global queMascota
    global queTransporte
    global despedida

    despedida = queNombre

    queNombre = queNombre.lower()

    queDescansoLower = queDescanso.lower()
    queDescansoReal = str(unidecode.unidecode(queDescansoLower))

    queTransporteLower = queTransporte.lower()
    queTransporteReal = str(unidecode.unidecode(queTransporteLower))

    if queDescansoReal == "musica":
        queDescanso = "escuchar algunas de tus canciones favoritas"
    if queDescansoReal == "leer":
        queDescanso = "charlar sobre alguno de nuestros libros favoritos"
    if queDescansoReal == "peliculas":
        queDescanso = "mirar alguna de tus películas favoritas"
    if queDescansoReal == "series":
        queDescanso = "mirar alguna de tus series favoritas"
    if queDescansoReal == "television":
        queDescanso = "mirar algún programa de televisión cósmico"
    if queDescansoReal == "videojuegos":
        queDescanso = "jugar alguno de tus videojuegos favoritos"


    if queTransporteReal == "avion":
        queTransporte = "atravesar los cielos de algún planeta en Circinus"
    if queTransporteReal == "barco":
        queTransporte = "navegar por los mares de algún planeta en Circinus"
    if queTransporteReal == "bicicleta":
        queTransporte = "pasear en bicicleta por los cráteres de algún planeta en Circinus"
    if queTransporteReal == "caminando":
        queTransporte = "pasear por los anillos de los planetas de Circinus"
    if queTransporteReal == "auto":
        queTransporte = "recorrer en auto alguna de las vías interplanetarias de Circinus"
    if queTransporteReal == "moto":
        queTransporte = "recorrer en moto alguna de las vías interplanetarias de Circinus"
    if queTransporteReal == "tren":
        queTransporte = "atravesar las vías interplanetarias de Circinus"

    #NO CIRCINUS

    jsonOutN = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Ésta es tu constelación. <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Nos podríamos juntar a" +queDescanso+ ". <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutN2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Ésta es tu constelación. <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> A lo mejor, <break time='300ms'/> para ese entonces, <break time='300ms'/> pueda manifestarme de manera física además de digital, <break time='3000ms'/> y podamos jugar un partido de "+ queDeporte +" juntos. <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutN3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Ésta es tu constelación. <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Tal vez me consiga un "+ queMascota +" digital de regreso a Circinus. <break time='300ms'/> Me vendría bien la companía. <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutN4 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Ésta es tu constelación. <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Podríamos "+queTransporte+". <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

# CON NOMBRE --------------------------
    

    jsonOutS = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Yo la llamo <break time='200ms'/> la constelación de " + queNombre +". <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Nos podríamos juntar a" +queDescanso+ ". <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutS2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Yo la llamo <break time='200ms'/> la constelación de " + queNombre +". <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> A lo mejor, <break time='300ms'/> para ese entonces, <break time='300ms'/> pueda manifestarme de manera física además de digital, <break time='3000ms'/> y podamos jugar un partido de "+ queDeporte +" juntos. <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutS3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Yo la llamo <break time='200ms'/> la constelación de " + queNombre +". <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Tal vez me consiga un "+ queMascota +" digital de regreso a Circinus. <break time='300ms'/> Me vendría bien la companía. <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutS4 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Yo la llamo <break time='200ms'/> la constelación de " + queNombre +". <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Podríamos "+queTransporte+". <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    azar = random.randrange(3)
    
    if azar == 0:
        if queNombre != "":
            return(jsonOutS3)
        else:
            return(jsonOutN3)
    if azar == 1:
        if queNombre != "":
            return(jsonOutN4)
        else:
            return(jsonOutS4)
    if azar == 2:
    	if queNombre != "":
    		if ball == 1:
    			return(jsonOutN2)
    		else:
    			return(jsonOutN)
    	else:
    		if ball == 1:
    			return(jsonOutS2)
    		else:
    			return(jsonOutS)

def constelacionNoFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    dummy = "0 \n"
    print("chamuyero")
    s.send(dummy.encode())#s.send(value.encode())  #te mando a Processing solo el valor importante

    #memoria Emma
    global queNombre
    global despedida

    despedida = queNombre

    global conoceCircinus
    global queDeporte
    global queDescanso
    global queEstacion
    global queMascota
    global queTransporte

    queNombre = queNombre.lower()

    queDescansoLower = queDescanso.lower()
    queDescansoReal = str(unidecode.unidecode(queDescansoLower))

    queTransporteLower = queTransporte.lower()
    queTransporteReal = str(unidecode.unidecode(queTransporteLower))

    if queDescansoReal == "musica":
        queDescanso = "escuchar algunas de tus canciones favoritas"
    if queDescansoReal == "leer":
        queDescanso = "charlar sobre alguno de nuestros libros favoritos"
    if queDescansoReal == "peliculas":
        queDescanso = "mirar alguna de tus películas favoritas"
    if queDescansoReal == "series":
        queDescanso = "mirar alguna de tus series favoritas"
    if queDescansoReal == "television":
        queDescanso = "mirar algún programa de televisión cósmico"
    if queDescansoReal == "videojuegos":
        queDescanso = "jugar alguno de tus videojuegos favoritos"


    if queTransporteReal == "avion":
        queTransporte = "atravesar los cielos de algún planeta en Circinus"
    if queTransporteReal == "barco":
        queTransporte = "navegar por los mares de algún planeta en Circinus"
    if queTransporteReal == "bicicleta":
        queTransporte = "pasear en bicicleta por los cráteres de algún planeta en Circinus"
    if queTransporteReal == "caminando":
        queTransporte = "pasear por los anillos de los planetas de Circinus"
    if queTransporteReal == "auto":
        queTransporte = "recorrer en auto alguna de las vías interplanetarias de Circinus"
    if queTransporteReal == "moto":
        queTransporte = "recorrer en moto alguna de las vías interplanetarias de Circinus"
    if queTransporteReal == "tren":
        queTransporte = "atravesar las vías interplanetarias de Circinus"

    borapora = "Qué pena"
    porabora = "Te lo voy a mostrar igual"

# " + borapora + "<break time='300ms'/> " + porabora + " <break time='500ms'/>
    #NO CIRCINUS

    jsonOutN = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " + borapora + "<break time='300ms'/> " + porabora + " <break time='500ms'/> Ésta es tu constelación. <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Nos podríamos juntar a" +queDescanso+ ". <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutN2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " + borapora + "<break time='300ms'/> " + porabora + " <break time='500ms'/> Ésta es tu constelación. <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> A lo mejor, <break time='300ms'/> para ese entonces, <break time='300ms'/> pueda manifestarme de manera física además de digital, <break time='3000ms'/> y podamos jugar un partido de "+ queDeporte +" juntos. <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutN3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " + borapora + "<break time='300ms'/> " + porabora + " <break time='500ms'/> Ésta es tu constelación. <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Tal vez me consiga un "+ queMascota +" digital de regreso a Circinus. <break time='300ms'/> Me vendría bien la companía. <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutN4 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " + borapora + "<break time='300ms'/> " + porabora + " <break time='500ms'/> Ésta es tu constelación. <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Podríamos "+queTransporte+". <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

# CON NOMBRE --------------------------
    

    jsonOutS = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " + borapora + "<break time='300ms'/> " + porabora + " <break time='500ms'/> Yo la llamo <break time='200ms'/> la constelación de " + queNombre +". <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Nos podríamos juntar a" +queDescanso+ ". <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutS2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " + borapora + "<break time='300ms'/> " + porabora + " <break time='500ms'/> Yo la llamo <break time='200ms'/> la constelación de " + queNombre +". <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> A lo mejor, <break time='300ms'/> para ese entonces, <break time='300ms'/> pueda manifestarme de manera física además de digital, <break time='3000ms'/> y podamos jugar un partido de "+ queDeporte +" juntos. <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutS3 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " + borapora + "<break time='300ms'/> " + porabora + " <break time='500ms'/> Yo la llamo <break time='200ms'/> la constelación de " + queNombre +". <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Tal vez me consiga un "+ queMascota +" digital de regreso a Circinus. <break time='300ms'/> Me vendría bien la companía. <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    jsonOutS4 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " + borapora + "<break time='300ms'/> " + porabora + " <break time='500ms'/> Yo la llamo <break time='200ms'/> la constelación de " + queNombre +". <break time='2000ms'/> Gracias por compartir este tiempo conmigo. <break time='400ms'/> Ahora que sabes sobre Circinus, <break time='400ms'/> quizá me puedas ir a visitar. <break time='500ms'/> Podríamos "+queTransporte+". <break time='1000ms'/> Que tengas un excelente día, <break time='200ms'/> "+queNombre+". <break time='300ms'/> Hasta la próxima. </prosody></speak>"}]}}]}

    azar = random.randrange(3)
    
    if azar == 0:
        if queNombre != "":
            return(jsonOutS3)
        else:
            return(jsonOutN3)
    if azar == 1:
        if queNombre != "":
            return(jsonOutN4)
        else:
            return(jsonOutS4)
    if azar == 2:
    	if queNombre != "":
    		if ball == 1:
    			return(jsonOutN2)
    		else:
    			return(jsonOutN)
    	else:
    		if ball == 1:
    			return(jsonOutS2)
    		else:
    			return(jsonOutS)


def fallbackFunction(req, action):
    #-----------------
    global noEntendi
    noEntendi += 1
    #-----------------

    global repiteEmma

    global queDescanso
    queDescansoLower = queDescanso.lower()
    queDescansoReal = str(unidecode.unidecode(queDescansoLower))

    frase = ""

    global queEstacion
    if queEstacion == "primavera":
        elEstacion = "la primavera"
    else:
        elEstacion = "el "+str(queEstacion)

    if queDescansoReal == "musica":
        frase = "escuchar música"
    if queDescansoReal == "leer":
        frase = "leer un buen libro"
    if queDescansoReal == "peliculas":
        frase = "mirar una buena película"
    if queDescansoReal == "series":
        frase = "mirar una buena serie"
    if queDescansoReal == "television":
        frase = "mirar televisión"

    #Fallbacks genéricos

    jsonOut1A = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Disculpa, <break time='400ms'/> no he podido entender lo que dijiste. <break time='500ms'/> ¿Podrías repetirlo? </prosody></speak>"}]}}]}

    jsonOut1B = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No he entendido bien que me has dicho. <break time='500ms'/> ¿Podrías repetirlo? </prosody></speak>"}]}}]}

    jsonOut1C = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Debo estar media sorda. <break time='300ms'/> No logro entender lo que me dices. <break time='500ms'/> ¿Podrías repetirlo? </prosody></speak>"}]}}]}

    #fallbacks para cada pregunta

    jsonOutWelcome = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Disculpa, <break time='400ms'/> no he podido entender lo que dijiste. <break time='500ms'/> Te preguntaba tu nombre. </prosody></speak>"}]}}]}

    jsonOutNombre = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Disculpa, <break time='400ms'/> no he podido entender lo que dijiste. <break time='500ms'/> Te preguntaba si conoces mi galaxia. <break time='300ms'/> Circinus. </prosody></speak>"}]}}]}

    jsonOutCircinus = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Qué distraída. <break time='400ms'/> No te escuchado bien. <break time='500ms'/> Te preguntaba si trabajas <break time='300ms'/> o estudias. </prosody></speak>"}]}}]}

    jsonOutOcupacion = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No lo he podido captar. <break time='500ms'/> Prefieres descansar, <break time='300ms'/> o hacer deporte. </prosody></speak>"}]}}]}

    jsonOutDeporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Debo haber tenido una interferencia. <break time='400ms'/> No te  he escuchado bien. <break time='500ms'/> Te preguntaba, <break time='300ms'/> ¿cuál es tu deporte favorito? </prosody></speak>"}]}}]}

    jsonOutDescansar = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Debo haber tenido una interferencia. <break time='400ms'/> No te he escuchado bien. <break time='500ms'/> Te preguntaba, <break time='300ms'/> Prefieres. <break time='300ms'/> Leer. <break time='300ms'/> Escuchar música. <break time='300ms'/> mirar películas. <break time='300ms'/> o jugar videojuegos. </prosody></speak>"}]}}]}

    jsonOutQueDeporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Vaya. <break time='300ms'/> No te he podido entender correctamente. <break time='500ms'/> Te preguntaba, <break time='300ms'/> ¿Tienes algún vínculo afectivo con un animal distinto al humano? <break time='700ms'/> Por ejemplo, <break time='300ms'/> un perro o un gato. </prosody></speak>"}]}}]}

    jsonOutFormaDeDescansar = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No te he podido comprender. <break time='700ms'/> Te preguntaba, <break time='300ms'/> ¿Te gusta " + frase +" cuando llueve? </prosody></speak>"}]}}]}

    jsonOutLluvia = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Veo que no estoy suficientemente concentrada. <break time='300ms'/> No te he podido entender. <break time='700ms'/> Te preguntaba, <break time='300ms'/> ¿Cuál es tu estación favorita? </prosody></speak>"}]}}]}

    jsonOutMascota1 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No te entendí. <break time='700ms'/> Te estaba preguntando antes. <break time='300ms'/> ¿Cuál es tu estación del año favorita? </prosody></speak>"}]}}]}

    jsonOutMascota2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No te entendí. <break time='700ms'/> Te preguntaba. <break time='400ms'/> Si tuvieras que elegir un vehiculo para recorrer el mundo. <break time='300ms'/> Por ejemplo, <break time='300ms'/> un barco, <break time='170ms'/> un avión, <break time='170ms'/> un auto. <break time='500ms'/> ¿Cuál elegirías? </prosody></speak>"}]}}]}

    jsonOutEstacionPalabra1 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No te entendí. <break time='700ms'/> Te preguntaba, <break time='300ms'/> ¿Tienes algún vínculo afectivo con un animal distinto al humano? <break time='700ms'/> Por ejemplo, <break time='300ms'/> un perro o un gato. </prosody></speak>"}]}}]}

    jsonOutEstacionPalabra2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No te entendí. <break time='700ms'/> Te preguntaba. <break time='400ms'/> Si tuvieras que elegir un vehiculo para recorrer el mundo. <break time='300ms'/> Por ejemplo, <break time='300ms'/> un barco, <break time='170ms'/> un avión, <break time='170ms'/> un auto. <break time='500ms'/> ¿Cuál elegirías? </prosody></speak>"}]}}]}

    jsonOutTransporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Te preguntaba si querías ver el regalo que tengo listo para ti. <break time='500ms'/> ¿Quieres verlo?  </prosody></speak>"}]}}]}

    if noEntendi < 2:
        azar = random.randrange(2)
        if azar == 0:
            return(jsonOut1A)
        if azar == 1:
            return(jsonOut1B)
        if azar == 2:
            return(jsonOut1C)
    else:
        if repiteEmma == "welcome":
            return(jsonOutWelcome)
        if repiteEmma == "nombre":
            return(jsonOutNombre)
        if repiteEmma == "circinus":
            return(jsonOutCircinus)
        if repiteEmma == "ocupacion":
            return(jsonOutOcupacion)
        if repiteEmma == "deporte":
            return(jsonOutDeporte)
        if repiteEmma == "descansar":
            return(jsonOutDescansar)
        if repiteEmma == "quedeporte":
            return(jsonOutQueDeporte)
        if repiteEmma == "musica":
            return(jsonOutFormaDeDescansar)
        if repiteEmma == "leer":
            return(jsonOutFormaDeDescansar)
        if repiteEmma == "pelicula":
            return(jsonOutFormaDeDescansar)
        if repiteEmma == "lluvia":
            return(jsonOutLluvia)
        if repiteEmma == "mascota":
            if ball == 1:
                return(jsonOutMascota1)
            if zzz == 1:
                return(jsonOutMascota2)
        if repiteEmma == "estacion":
            if zzz == 1:
                return(jsonOutEstacionPalabra1)
            if ball == 1:
                return(jsonOutEstacionPalabra2)
        if repiteEmma == "transporte":
            return(jsonOutTransporte)

    #Fallbacks con repetición de pregunta

def chauFunction(req, action):
    tummy = "50 \n"
    s.send(tummy.encode())

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    repiteEmma = ""
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    #olvidarse de todos los datos del usuario anterior
    global queNombre
    global conoceCircinus
    global queDeporte
    global queDescanso
    global queEstacion
    global queMascota
    global queTransporte
    global despedida
    queNombre = ""
    conoceCircinus = 5225 
    queDeporte = ""
    queDescanso = ""
    queEstacion = ""
    queMascota = ""
    queTransporte = ""
    #olvidarse de la ramas recorridas anteriormente
    global ball
    global zzz
    ball = 0
    zzz = 0

    jsonOut = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> Nos vemos, <break time='300> "+ queNombre + ". </prosody></speak>"}]}}]}
   
    return (jsonOut)    

# INTENTS ACCESORIOS

def ofensaFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("ofensa")
    dummy = "33 \n"
    print("phd")
    s.send(dummy.encode())

    global queNombre

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    global queDescanso
    queDescansoLower = queDescanso.lower()
    queDescansoReal = str(unidecode.unidecode(queDescansoLower))

    frase = ""

    global queEstacion
    if queEstacion == "primavera":
        elEstacion = "la primavera"
    else:
        elEstacion = "el "+str(queEstacion)

    if queDescansoReal == "musica":
        frase = "escuchar música"
    if queDescansoReal == "leer":
        frase = "leer un buen libro"
    if queDescansoReal == "peliculas":
        frase = "mirar una buena película"
    if queDescansoReal == "series":
        frase = "mirar una buena serie"
    if queDescansoReal == "television":
        frase = "mirar televisión"

    jsonOutWelcome = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Quisiera saber tu nombre. </prosody></speak>"}]}}]}

    jsonOutNombre = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te preguntaba " + queNombre + " si conoces Circinus. </prosody></speak>"}]}}]}

    jsonOutCircinus = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/> Trabajas, <break time='200ms'/> o estudias. </prosody></speak>"}]}}]}

    jsonOutOcupacion = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando si en tus tiempos libres. <break time='500ms'/> Prefieres hacer deporte <break time='200ms'/> o relajarte. </prosody></speak>"}]}}]}

    jsonOutDeporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/> ¿Cuál es tu deporte favorito? </prosody></speak>"}]}}]}

    jsonOutDescansar = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/> Prefieres,  <break time='200ms'/> leer, <break time='200ms'/> escuchar música, <break time='200ms'/> mirar películas, <break time='200ms'/> o jugar videojuegos. </prosody></speak>"}]}}]}

    jsonOutQueDeporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/> ¿Tienes algún vínculo afectivo con un animal distinto al humano? <break time='700ms'/> Por ejemplo, <break time='300ms'/> un perro o un gato. </prosody></speak>"}]}}]}

    jsonOutFormaDeDescansar = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/> ¿Te gusta" +frase+ " cuando llueve? </prosody></speak>"}]}}]}

    jsonOutLluvia = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/> ¿Cuál es tu estación favorita? </prosody></speak>"}]}}]}

    jsonOutMascota1 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/>  <break time='300ms'/> ¿Cuál es tu estación del año favorita? </prosody></speak>"}]}}]}

    jsonOutMascota2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/>  Si tuvieras que elegir un vehiculo para recorrer el mundo. <break time='300ms'/> Por ejemplo, <break time='300ms'/> un barco, <break time='170ms'/> un avión, <break time='170ms'/> un auto. <break time='500ms'/> ¿Cuál elegirías? </prosody></speak>"}]}}]}

    jsonOutEstacion = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/>  Te estaba pidiendo que describas " + elEstacion + " con una palabra.  <break time='700ms'/> Por ejemplo, <break time='300ms'/> " + repiteEmma +".  </prosody></speak>"}]}}]}

    jsonOutEstacionPalabra1 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/>  ¿Tienes algún vínculo afectivo con un animal distinto al humano? <break time='700ms'/> Por ejemplo, <break time='300ms'/> un perro o un gato. </prosody></speak>"}]}}]}

    jsonOutEstacionPalabra2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/> Te estaba preguntando. <break time='500ms'/>  Si tuvieras que elegir un vehiculo para recorrer el mundo. <break time='300ms'/> Por ejemplo, <break time='300ms'/> un barco, <break time='170ms'/> un avión, <break time='170ms'/> un auto. <break time='500ms'/> ¿Cuál elegirías? </prosody></speak>"}]}}]}

    jsonOutTransporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> ¡Qué mala educación! <break time='400ms'/> No soy Siri para que me ofendas de esa manera. <break time='1000ms'/>  Te preguntaba si querías ver el regalo que tengo listo para ti. <break time='500ms'/> ¿Quieres verlo?  </prosody></speak>"}]}}]}

    if repiteEmma == "welcome":
        return(jsonOutWelcome)
    if repiteEmma == "nombre":
        return(jsonOutNombre)
    if repiteEmma == "circinus":
        return(jsonOutCircinus)
    if repiteEmma == "ocupacion":
        return(jsonOutOcupacion)
    if repiteEmma == "deporte":
        return(jsonOutDeporte)
    if repiteEmma == "descansar":
        return(jsonOutDescansar)
    if repiteEmma == "quedeporte":
        return(jsonOutQueDeporte)
    if repiteEmma == "musica":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "leer":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "pelicula":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "videojuegos":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "lluvia":
        return(jsonOutLluvia)
    if repiteEmma == "mascota":
        if ball == 1:
            return(jsonOutMascota1)
        if zzz == 1:
            return(jsonOutMascota2)
    if repiteEmma == "estacion":
        return(jsonOutEstacion)
    if repiteEmma == "estacionpalabra":
        if zzz == 1:
            return(jsonOutEstacionPalabra1)
        if ball == 1:
            return(jsonOutEstacionPalabra2)
    if repiteEmma == "transporte":
        return(jsonOutTransporte)

def robotFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("avatar")
    dummy = "33 \n"
    print("alien vs predator")
    global queNombre

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    global queDescanso
    queDescansoLower = queDescanso.lower()
    queDescansoReal = str(unidecode.unidecode(queDescansoLower))

    frase = ""
    fraseAvatar = ""

    global queEstacion
    if queEstacion == "primavera":
        elEstacion = "la primavera"
    else:
        elEstacion = "el "+str(queEstacion)

    if queDescansoReal == "musica":
        frase = "escuchar música"
    if queDescansoReal == "leer":
        frase = "leer un buen libro"
    if queDescansoReal == "peliculas":
        frase = "mirar una buena película"
    if queDescansoReal == "series":
        frase = "mirar una buena serie"
    if queDescansoReal == "television":
        frase = "mirar televisión"
    if queDescansoReal == "videojuegos":
        frase = "jugar videojuegos"

    if value == "alien" or value == "robot" or value == "computadora" or value == "monstruo" or value == "humano":
        fraseAvatar = "No exactamente"
    else:
        fraseAvatar = ""


    jsonOutWelcome = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Quisiera saber tu nombre. </prosody></speak>"}]}}]}

    jsonOutNombre = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te preguntaba " + queNombre + " si conoces Circinus. </prosody></speak>"}]}}]}

    jsonOutCircinus = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> Trabajas, <break time='200ms'/> o estudias. </prosody></speak>"}]}}]}

    jsonOutOcupacion = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando si en tus tiempos libres. <break time='500ms'/> Prefieres hacer deporte <break time='200ms'/> o relajarte. </prosody></speak>"}]}}]}

    jsonOutDeporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> ¿Cuál es tu deporte favorito? </prosody></speak>"}]}}]}

    jsonOutDescansar = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> Prefieres,  <break time='200ms'/> leer, <break time='200ms'/> escuchar música, <break time='200ms'/> o mirar películas. </prosody></speak>"}]}}]}

    jsonOutQueDeporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> ¿Tienes algún vínculo afectivo con un animal distinto al humano? <break time='700ms'/> Por ejemplo, <break time='300ms'/> un perro o un gato. </prosody></speak>"}]}}]}

    jsonOutFormaDeDescansar = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> ¿Te gusta" +frase+ " cuando llueve? </prosody></speak>"}]}}]}

    jsonOutLluvia = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> ¿Cuál es tu estación favorita? </prosody></speak>"}]}}]}

    jsonOutMascota1 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/>  <break time='300ms'/> ¿Cuál es tu estación del año favorita? </prosody></speak>"}]}}]}

    jsonOutMascota2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/>  Si tuvieras que elegir un vehiculo para recorrer el mundo. <break time='300ms'/> Por ejemplo, <break time='300ms'/> un barco, <break time='170ms'/> un avión, <break time='170ms'/> un auto. <break time='500ms'/> ¿Cuál elegirías? </prosody></speak>"}]}}]}

    jsonOutEstacion = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/>  Te estaba pidiendo que describas " + elEstacion + " con una palabra.  <break time='700ms'/> Por ejemplo, <break time='300ms'/> " + repiteEmma +".  </prosody></speak>"}]}}]}

    jsonOutEstacionPalabra1 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/>  ¿Tienes algún vínculo afectivo con un animal distinto al humano? <break time='700ms'/> Por ejemplo, <break time='300ms'/> un perro o un gato. </prosody></speak>"}]}}]}

    jsonOutEstacionPalabra2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/>  Si tuvieras que elegir un vehiculo para recorrer el mundo. <break time='300ms'/> Por ejemplo, <break time='300ms'/> un barco, <break time='170ms'/> un avión, <break time='170ms'/> un auto. <break time='500ms'/> ¿Cuál elegirías? </prosody></speak>"}]}}]}

    jsonOutTransporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> " +fraseAvatar + ". <break time='400ms'/> Soy una entidad digital. <break time='600ms'/> Existo solamente en el universo informático. <break time='400ms'/> Por esa razón tuve que esperar tanto para llegar a la tierra. <break time='400ms'/> Antes no existía un internet suficientemente veloz como para que pueda venir. <break time='1200ms'/> Te preguntaba si querías ver el regalo que tengo listo para ti. <break time='500ms'/> ¿Quieres verlo?  </prosody></speak>"}]}}]}

    if repiteEmma == "welcome":
        return(jsonOutWelcome)
    if repiteEmma == "nombre":
        return(jsonOutNombre)
    if repiteEmma == "circinus":
        return(jsonOutCircinus)
    if repiteEmma == "ocupacion":
        return(jsonOutOcupacion)
    if repiteEmma == "deporte":
        return(jsonOutDeporte)
    if repiteEmma == "descansar":
        return(jsonOutDescansar)
    if repiteEmma == "quedeporte":
        return(jsonOutQueDeporte)
    if repiteEmma == "musica":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "leer":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "pelicula":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "lluvia":
        return(jsonOutLluvia)
    if repiteEmma == "mascota":
        if ball == 1:
            return(jsonOutMascota1)
        if zzz == 1:
            return(jsonOutMascota2)
    if repiteEmma == "estacion":
        return(jsonOutEstacion)
    if repiteEmma == "estacionpalabra":
        if zzz == 1:
            return(jsonOutEstacionPalabra1)
        if ball == 1:
            return(jsonOutEstacionPalabra2)
    if repiteEmma == "transporte":
        return(jsonOutTransporte)

def zodiacoFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    value = parameter.get("signo")
    dummy = "33 \n"
    print("caballeros del zodiaco")
    global queNombre

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #reset contador de Fallbacks
    global noEntendi
    noEntendi = 0
    #bandera para repetir la pregunta
    global repiteEmma
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    global queDescanso
    queDescansoLower = queDescanso.lower()
    queDescansoReal = str(unidecode.unidecode(queDescansoLower))

    frase = ""

    global queEstacion
    if queEstacion == "primavera":
        elEstacion = "la primavera"
    else:
        elEstacion = "el "+str(queEstacion)

    if queDescansoReal == "musica":
        frase = "escuchar música"
    if queDescansoReal == "leer":
        frase = "leer un buen libro"
    if queDescansoReal == "peliculas":
        frase = "mirar una buena película"
    if queDescansoReal == "series":
        frase = "mirar una buena serie"
    if queDescansoReal == "television":
        frase = "mirar televisión"
    if queDescansoReal == "videojuegos":
        frase = "jugar videojuegos"

    jsonOutWelcome = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Quisiera saber tu nombre. </prosody></speak>"}]}}]}

    jsonOutNombre = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te preguntaba " + queNombre + " si conoces Circinus. </prosody></speak>"}]}}]}

    jsonOutCircinus = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> Trabajas, <break time='200ms'/> o estudias. </prosody></speak>"}]}}]}

    jsonOutOcupacion = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando si en tus tiempos libres. <break time='500ms'/> Prefieres hacer deporte <break time='200ms'/> o relajarte. </prosody></speak>"}]}}]}

    jsonOutDeporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> ¿Cuál es tu deporte favorito? </prosody></speak>"}]}}]}

    jsonOutDescansar = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> Prefieres,  <break time='200ms'/> leer, <break time='200ms'/> escuchar música, <break time='200ms'/> o mirar películas. </prosody></speak>"}]}}]}

    jsonOutQueDeporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> ¿Tienes algún vínculo afectivo con un animal distinto al humano? <break time='700ms'/> Por ejemplo, <break time='300ms'/> un perro o un gato. </prosody></speak>"}]}}]}

    jsonOutFormaDeDescansar = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> ¿Te gusta" +frase+ " cuando llueve? </prosody></speak>"}]}}]}

    jsonOutLluvia = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/> ¿Cuál es tu estación favorita? </prosody></speak>"}]}}]}

    jsonOutMascota1 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/>  <break time='300ms'/> ¿Cuál es tu estación del año favorita? </prosody></speak>"}]}}]}

    jsonOutMascota2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/>  Si tuvieras que elegir un vehiculo para recorrer el mundo. <break time='300ms'/> Por ejemplo, <break time='300ms'/> un barco, <break time='170ms'/> un avión, <break time='170ms'/> un auto. <break time='500ms'/> ¿Cuál elegirías? </prosody></speak>"}]}}]}

    jsonOutEstacionPalabra1 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/>  ¿Tienes algún vínculo afectivo con un animal distinto al humano? <break time='700ms'/> Por ejemplo, <break time='300ms'/> un perro o un gato. </prosody></speak>"}]}}]}

    jsonOutEstacionPalabra2 = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te estaba preguntando. <break time='500ms'/>  Si tuvieras que elegir un vehiculo para recorrer el mundo. <break time='300ms'/> Por ejemplo, <break time='300ms'/> un barco, <break time='170ms'/> un avión, <break time='170ms'/> un auto. <break time='500ms'/> ¿Cuál elegirías? </prosody></speak>"}]}}]}

    jsonOutTransporte = {"fulfillmentMessages": [{"platform": "ACTIONS_ON_GOOGLE","simpleResponses": {"simpleResponses":[{"ssml": "<speak><prosody rate='medium' pitch='1st'> No exactamente. <break time='400ms'/> En Circinus tenemos signos del zodíaco distintos a los terrestres. <break time='400ms'/> Allá soy Viento Solar. <break time='400ms'/> En la tierra, <break time='230ms'/> soy Libra. <break time='1200ms'/> Te preguntaba si querías ver el regalo que tengo listo para ti. <break time='500ms'/> ¿Quieres verlo?  </prosody></speak>"}]}}]}

    if repiteEmma == "welcome":
        return(jsonOutWelcome)
    if repiteEmma == "nombre":
        return(jsonOutNombre)
    if repiteEmma == "circinus":
        return(jsonOutCircinus)
    if repiteEmma == "ocupacion":
        return(jsonOutOcupacion)
    if repiteEmma == "deporte":
        return(jsonOutDeporte)
    if repiteEmma == "descansar":
        return(jsonOutDescansar)
    if repiteEmma == "quedeporte":
        return(jsonOutQueDeporte)
    if repiteEmma == "musica":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "leer":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "pelicula":
        return(jsonOutFormaDeDescansar)
    if repiteEmma == "lluvia":
        return(jsonOutLluvia)
    if repiteEmma == "mascota":
        if ball == 1:
            return(jsonOutMascota1)
        if zzz == 1:
            return(jsonOutMascota2)
    if repiteEmma == "estacion":
        if zzz == 1:
            return(jsonOutEstacionPalabra1)
        if ball == 1:
            return(jsonOutEstacionPalabra2)
    if repiteEmma == "transporte":
        return(jsonOutTransporte)


# ----------------------------------- STARTER
if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))

    print ("Starting app on port %d" %(port))


    app.run(debug=True, port=port, host='0.0.0.0')
    triggertest()


#SI NO QUIEREN DAR EL NOMBRE TENGO QUE PONER UN INTENT A PRUEBA DE GILES