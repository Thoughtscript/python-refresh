import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Kylan.html
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
name = ""

while count > 0:
    count -= 1
    anchorCount = 0
    print("Retrieving: " + url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup('a')

    for anchor in anchors:
        anchorCount += 1
        if anchorCount == position:
            url = anchor.get('href', None)
            name = url.replace('http://py4e-data.dr-chuck.net/known_by_', '')
            name = name.replace('.html', '')
            break

print(name)