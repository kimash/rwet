from bs4 import BeautifulSoup
import urllib
import sys

# here's how to fake a user agent string with urllib
class FakeMozillaOpener(urllib.FancyURLopener):
  version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
urllib._urlopener = FakeMozillaOpener()

url = "http://en.wikipedia.org/wiki/Nabokov"

data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

for words in soup.findAll('p'):
  print words 

sleep(1.0)