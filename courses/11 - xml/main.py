import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# http://py4e-data.dr-chuck.net/comments_42.xml - 2553
# http://py4e-data.dr-chuck.net/comments_551923.xml

# Enable SSL retrieval
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
result = 0

html = urllib.request.urlopen(url, context=context).read()
xml = ET.fromstring(html)
counts = xml.findall('.//count')

for count in counts:
    result += int(count.text)

print(str(result))