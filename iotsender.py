import requests
import json

headers = {'api-key': 'e8e09f57af79bfa3aa2dc53182879e7643ad651543'}
payload = {} #The variable to send to IoTPlotter
payload["data"] = {} #A dictionary containing the data to send to IoTPlotter
payload["data"]["HOTTUB_TEMP"] = [] #Creates a list for sending one or more values to IoTPlotter for the 'GRAPH_NAME' graph.

#Appends three values for the graph 'GRAPH_NAME': 
payload["data"]["HOTTUB_TEMP"].append({"value":99}) #'GRAPH_NAME' is set to 25.05

requests.post("http://iotplotter.com/api/v2/feed/507729691826868583", headers=headers, data=json.dumps(payload))

requests.post("https://hook.us1.make.com/men8mmy2fvk982cwojzaadda46ae024y", data=json.dumps(payload))