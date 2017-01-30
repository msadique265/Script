#-----
#- descr  : Script to find links of google search result of a url
#- Author : Md Sadique
#----------------------
import urllib2, sys, urllib
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
	print('usage : ' + sys.argv[0] + ' <url>')
	sys.exit()
	
url = 'http://www.google.com/search?' + urllib.urlencode({'q': ' '.join(sys.argv[1:])})
#url = sys.argv[1]

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
data = opener.open(url).read()

soup = BeautifulSoup(data, 'lxml')

links = soup.find_all('div', 'g')
for link in links:
	print(link.a.get('href')[7:])
