import requests
import json
import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/28-000006b197cf/w1_slave'

def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = (temp_c * (9.0/5.0)) + 32.0
        return temp_f


headers = {'api-key': 'e8e09f57af79bfa3aa2dc53182879e7643ad651543'}

payload = {}
payload["data"] = {}
payload["data"]["HOTTUB_TEMP"] = []
payload["data"]["HOTTUB_TEMP"].append({"value":read_temp()})

requests.post("http://iotplotter.com/api/v2/feed/507729691826868583", headers=headers, data=json.dumps(payload))

#requests.post("https://hook.us1.make.com/men8mmy2fvk982cwojzaadda46ae024y", data=json.dumps(payload))
