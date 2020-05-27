import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Enable SSL retrieval
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

html = urllib.request.urlopen(url, context=context).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Get href attribute on tag
    print(tag.get('href', None))
    # Recurse to fully scrape