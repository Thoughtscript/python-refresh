import urllib.request, urllib.parse, urllib.error
import json
import ssl

# http://py4e-data.dr-chuck.net/comments_42.json - 2553
# http://py4e-data.dr-chuck.net/comments_551924.json

# Enable SSL retrieval
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
count = 0

response = urllib.request.urlopen(url, context=context).read()
j = json.loads(response)

for entry in j["comments"]:
    count += int(entry["count"])

print(str(count))