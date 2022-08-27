# Send request to Västtrafik for 1) access token, 2) bus stop based on input and 3) departures

import base64
import requests
import datetime

id = "device_12345"
nyckel="WO0vwoy1KvBrlheiA97k8XQBOWQa"
hemlighet="UqBaPs6X2W4ink1FItAtm79XHkUa"
to_be_encoded = nyckel + ":" + hemlighet
encoded_string = base64.b64encode(to_be_encoded.encode("ascii")).decode()

url_token = "https://api.vasttrafik.se/token"
data = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic " + encoded_string + "=grant_type=client_credentials&scope=" + id,
    "grant_type": "client_credentials",
    "client_secret": hemlighet,
    "client_id": nyckel
}

x = requests.post(url_token, data=data)
print(x.json())
access_token = x.json()['access_token']

# 2) Send request for stop ID based on user input_departure_stop


user_input_stopID = "Rävekärrsgatan"
format = "json"
url_stopID = "https://api.vasttrafik.se/bin/rest.exe/v2/location.name?input=" + user_input_stopID + "&format=" + format
headers={
    "Authorization": "Bearer " + access_token
}

x2 = requests.get(url_stopID, headers=headers)
print(x2.json()['LocationList']['StopLocation'][0]['name']) # Bus stop name
stopID = x2.json()['LocationList']['StopLocation'][0]['id']

# 3) Send GET request for departures. This requires some time variables.
date_now= datetime.datetime.now().strftime("%Y%m%d")
hour_now= datetime.datetime.now().strftime("%H")
minutes_now= datetime.datetime.now().strftime("%M")
url_departures = "https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard?id=" + stopID + "&date=" + date_now + "&time=" + hour_now + "%3A" + minutes_now + "&format=" + format
x3 = requests.get(url_departures, headers=headers)

departures = x3.json()['DepartureBoard']['Departure']

for x in departures:
    date_iso = x['date']
    time_iso = x['time']
    dep_date = datetime.datetime.fromisoformat(date_iso + " " + time_iso)
    current_date = datetime.datetime.now()
    current_date = current_date.replace(second=0,microsecond=0) # Remove seconds and microseconds for simplicity because they are not provided in the departure times by Västtrafik
    direction = x['direction']
    delta = str(int((dep_date - current_date).total_seconds()/60)) # Time difference in minutes
    vehicle = x['name']
    print(vehicle + " arrival: " + delta + " min. Departure = " + dep_date.strftime("%H:%M") + " Direction = " + direction)
