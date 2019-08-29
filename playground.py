#!/usr/bin/env python

import random
import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response



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
    parameter = result.get("parameters")
    

    if parameter == "sportsAction":
        finalReply = sportsFunction(req, action)
        return(finalReply)
    elif action == "colorAction":
        finalReply = colorFunction(req, action)
        return(finalReply)
        

def sportsFunction(req, action):
    
    sportType = parameter.get("sportsName")
    responseList = ["Respuesta custom para Sports", 
                    "A mi también me gusta el "+sportType, 
                    "Hacer deporte es bueno para la salud."]

    response = random.choice(responseList)
    print("Response is: " + response)
        
    jsonOut = {'fulfillmentText': response, 'DisplayText': response,}
    return (jsonOut)


def colorFunction(req, action):
    result = req.get("queryResult")
    parameter = result.get("parameters")
    colorType = parameter.get("colorName")
    responseList = ["Respuesta custom para Color", 
                    "A mi también me gusta el "+colorType, 
                    "Sabías que el color " + colorType + " significa alegría?"]

    response = random.choice(responseList)
    print("Response is: " + response)
        
    jsonOut = {'fulfillmentText': response, 'DisplayText': response,}
    return (jsonOut)



# ----------------------------------- STARTER
if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))

    print ("Starting app on port %d" %(port))


    app.run(debug=True, port=port, host='0.0.0.0')


