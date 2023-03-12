import json
import requests

data = {
    "problem_description" : "Problametic",
    "serial_number" : "51-B-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC-125447-DC",
    "light_indicator1" : "on",
    "light_indicator2" : "blinking",
    "light_indicator3" : "off"
}
json_data = json.dumps(data)

response = requests.post("http://localhost:8000/problem-report", data=json_data).text

print(response)




