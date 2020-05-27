import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# http://py4e-data.dr-chuck.net/comments_42.html - 2553
# http://py4e-data.dr-chuck.net/comments_551921.html
url = input('Enter - ')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
spans = soup('span')

count = 0

for span in spans:
    strNum = span.string
    count += int(strNum)

print(count)
