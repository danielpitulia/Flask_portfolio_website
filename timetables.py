# Send two requests to västtrafik. First, get the ID of the given bus stop. Then, get the departure tables.
import requests
import datetime

# 1) Send request for stop ID based on user input_departure_stop


def get_timetables(token, user_input_stopID):
    format = "json"
    url_stopID = "https://api.vasttrafik.se/bin/rest.exe/v2/location.name?input=" + \
        user_input_stopID + "&format=" + format
    headers = {
        "Authorization": "Bearer " + token
    }

    x2 = requests.get(url_stopID, headers=headers)
    stopID = x2.json()['LocationList']['StopLocation'][0]['id']

    # 2) Initialise time variables and send GET request for departures.
    date_now = datetime.datetime.now().strftime("%Y%m%d")
    hour_now = datetime.datetime.now().strftime("%H")
    minutes_now = datetime.datetime.now().strftime("%M")

    url_departures = "https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard?id=" + stopID + \
        "&date=" + date_now + "&time=" + hour_now + \
        "%3A" + minutes_now + "&format=" + format

    try:
        x3 = requests.get(url_departures, headers=headers)
        departures = x3.json()['DepartureBoard']['Departure']
        stop_name = departures[0]['stop']
    except:
        departures = ["N/A"]
        stop_name = "Not found, try another stop name."

    current_date = datetime.datetime.now()
    current_date = current_date.replace(second=0, microsecond=0)
    # Remove seconds and microseconds for simplicity because they are not provided in the departure times by Västtrafik

    line = list()
    delta = list()
    direction = list()

    if departures != ["N/A"]:
        for departure in departures:
            date_iso = departure['date']
            time_iso = departure['time']
            dep_date = datetime.datetime.fromisoformat(
                date_iso + " " + time_iso)
            # Time difference in minutes
            delta_x = [int((dep_date - current_date).total_seconds() / 60)]

            if delta_x[0] > 0:
                delta += delta_x
                line += [departure['name']]
                direction += [departure['direction']]
                # Extra brackets converts strings into one list item
            if len(line) >= 10:
                break

        departure_zip = zip(line, delta, direction)
    else:
        departure_zip = False

    return departure_zip, stop_name
