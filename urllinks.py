
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urllib.request.urlopen(url, context=ctx).read()

count = int(input('Enter Count - '))
position = int(input('Enter Position - ')) - 1
print ("Retreiving: " + str(url))

for x in range(count - 1):
    soup = BeautifulSoup(html, 'html.parser')
    url = soup.find_all('a')[position].get('href', None)
    print ("Retreiving: " + str(url))
    html = urllib.request.urlopen(url, context=ctx).read()


soup2 = BeautifulSoup(html, 'html.parser')
print ("Retreiving: " + soup2.find_all('a')[position].get('href', None))
print (soup2.find_all('a')[position].string)
