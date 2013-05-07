#Kim Ash
#wikipoem.py

from bs4 import BeautifulSoup
import urllib
import sys
import re
import random
import markov

sourceText = ''

def extract_text(tag):
  if hasattr(tag, "name") and tag.name in ["ul", "ol", "table"]:
	  return ""
  else:
	  tag_string = tag.string
	  if tag_string is None:
		children = tag.contents
		result = ''
		for child in children:
		  child_text = extract_text(child)
		  result += child_text + ' '
		return result
	  else:
		return tag_string.strip()

# here's how to fake a user agent string with urllib
class FakeMozillaOpener(urllib.FancyURLopener):
  version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
urllib._urlopener = FakeMozillaOpener()

url = "http://en.wikipedia.org/wiki/Nabokov"

data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

sourceText += extract_text(soup.p)

for sibling in soup.p.next_siblings:
	sourceText += extract_text(sibling)

#re.sub(r"\[\s\w{1,}\s\]", "", sourceText)
generator = markov.MarkovGenerator(n=2, max=500)
generator.feed(sourceText)
print generator.generate()

#print sourceText