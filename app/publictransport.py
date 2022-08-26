import base64
import requests

id = "123"
nyckel='WO0vwoy1KvBrlheiA97k8XQBOWQa'
hemlighet='UqBaPs6X2W4ink1FItAtm79XHkUa'
to_be_encoded = nyckel + ":" + hemlighet
encoded_string = base64.b64encode(to_be_encoded.encode('ascii')).decode()

url = 'https://api.vasttrafik.se/token'
data = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic ' + encoded_string + '=grant_type=client_credentials&scope=<' + id + '>'
}

x = requests.post(url, data=data)
print(x.headers)
