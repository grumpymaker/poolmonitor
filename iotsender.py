import requests
import json
import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = os.environ.get('SENSORPATH')
apikey = os.environ.get('IOTPLOTTERAPI')
iotplotterfeed = os.environ.get('IOTPLOTTERFEED')
iotplottersensor = os.environ.get('IOTPLOTTERSENSOR')
makewebhook = os.environ.get('MAKEWEBHOOK')

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
        return round(temp_f,1)


headers = {'api-key': apikey}

payload = {}
payload["data"] = {}
payload["data"][iotplottersensor] = []
payload["data"][iotplottersensor].append({"value":read_temp()})

requests.post(iotplotterfeed, headers=headers, data=json.dumps(payload))

#requests.post(makewebhook, data=json.dumps(payload))
