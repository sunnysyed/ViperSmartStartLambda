from __future__ import print_function

import urllib2
import json


def lambda_handler(event, context):
    url = "https://colt.calamp-ts.com"
    response = urllib2.urlopen(url + "/auth/login/" + event['email'] + "/" + event['password']).read()
    data = json.loads(response)   
    sessionId = data['Return']['Results']['SessionID']
    response = urllib2.urlopen(url + "/device/advancedsearch?sessid=" + sessionId).read()
    data = json.loads(response)
    vehicleId = data['Return']['Results']['Devices'][0]['DeviceId']
    response = urllib2.urlopen(url + "/device/sendcommand/" + vehicleId + "/" + event['command'] + "?sessid=" + sessionId).read()
    data = json.loads(response)
    return data
