from flask import Flask, request
from labnetapp import app
from collections import deque
from nodeConfig import *
from labnetapp.base import reqRittalStatusFromAll

@app.route('/plug/<id>/status', methods=['GET'])
def getPlugStatus(id):
    return plugs[id].getStatus()

@app.route('/plug/<id>/power', methods=['POST'])
def setPlugPower(id):
    print(request.data.decode("utf-8"))
    dataDict = json.loads(request.data.decode("utf-8"))
    print(id + dataDict["state"])
    obj = canObj.canObj()
    msg = obj.genPlugChangeMsg(get_plug_adress_by_id(id), dataDict["state"])
    #print(msg)
    base.msgTX.append(msg)
    return "OK"

# API
# returns the complete labnet config file 
@app.route('/config')
def nodeConfig():
    f = open("nodeConfig/mainv2.json", 'r').read()
    #print(getAllPlugsJson())
    return f
 

# API
# reloads config
@app.route('/config/reload')
def nodeConfigReload():
    loadConfig()
    #reqRittalStatusFromAll()
    return "OK"
