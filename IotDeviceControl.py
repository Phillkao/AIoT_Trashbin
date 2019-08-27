import requests
import numpy as np
import time
import json
import configparser 


def IotDeviceState_TrashCan100Per_On():
    config = configparser.ConfigParser()
    config.read('./cht.conf')
    projectKey = config.get('device-key', 'projectKey')
    deviceId   = config.get('device-key', 'deviceId')
    sensorId   = config.get('device-key', 'sensorId')
    #sensorId   = config.get('device-key', 'sensorIdTest')
    
    apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/rawdata'
    headers = { 
        "CK":projectKey,
        "Content-Type": "application/json",
    }   
    payload=[{"id":sensorId, "value":[1]}]
    response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
    
def IotDeviceState_TrashCan100Per_Off():
    config = configparser.ConfigParser()
    config.read('./cht.conf')
    projectKey = config.get('device-key', 'projectKey')
    deviceId   = config.get('device-key', 'deviceId')
    sensorId   = config.get('device-key', 'sensorId')
    #sensorId   = config.get('device-key', 'sensorIdTest')
    
    apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/rawdata'
    headers = { 
        "CK":projectKey,
        "Content-Type": "application/json",
    }   
    payload=[{"id":sensorId, "value":[0]}]
    response = requests.post(apiURL, headers=headers, data=json.dumps(payload))

    
def IotDeviceState_TrashCount_PlusOne():
    config = configparser.ConfigParser()
    config.read('./cht.conf')
    projectKey = config.get('device-key', 'projectKey')
    deviceId   = config.get('device-key', 'deviceId')
    trashcountId = config.get('device-key', 'trashcountId')
    #sensorId   = config.get('device-key', 'sensorIdTest')
    
    apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/rawdata'
    headers = { 
        "CK":projectKey,
        "Content-Type": "application/json",
    }
    
    response = requests.get(apiURL, headers=headers)
    jdict = json.loads(response.text)
    recent_trash_count = jdict[1]['value'][0]
    
    payload=[{"id":trashcountId, "value":[int(recent_trash_count)+1]}]
    response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
	
def IotDeviceState_TrashCount_Clean():
    config = configparser.ConfigParser()
    config.read('./cht.conf')
    projectKey = config.get('device-key', 'projectKey')
    deviceId   = config.get('device-key', 'deviceId')
    trashcountId = config.get('device-key', 'trashcountId')
	
    apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/rawdata'
    headers = { 
        "CK":projectKey,
        "Content-Type": "application/json",
    }
    payload=[{"id":trashcountId, "value":[0]}]
    response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
