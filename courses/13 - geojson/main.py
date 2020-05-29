import urllib.request, urllib.parse, urllib.error
import json
import ssl

# South Federal University - ChIJ0V94rPl_bIcRqLdrlbjFMDk

# Enable SSL retrieval
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/json?"
location = input('Enter location: ')

params = dict()
params["key"] = 42
params["address"] = location

urlWithParams = url + urllib.parse.urlencode(params)

response = urllib.request.urlopen(urlWithParams, context=context).read().decode()
j = json.loads(response)

name = j["results"][0]["place_id"]

print(str(name))