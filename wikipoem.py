#Kim Ash
#wikipoem.py

from bs4 import BeautifulSoup
import urllib
import sys
import re
import random

sourceText = ''

# list of 14 empty lists, one for each word length
words_by_len = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], ]

# list for words that will be in poem
poem_words = list()
poem = ''

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
# necessary to access articles on Wikipedia
class FakeMozillaOpener(urllib.FancyURLopener):
  version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
urllib._urlopener = FakeMozillaOpener()

term = sys.argv[1]
url = 'http://en.wikipedia.org/wiki/' + term
first_let = term[0].upper()

data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

sourceText += extract_text(soup.p)

for sibling in soup.p.next_siblings:
	sourceText += extract_text(sibling)
#re.sub(r"\[\s\w{1,}\s\]", "", sourceText)

for i in range(len(words_by_len)):
#find words of each length (i+1 because range() starts at 0)
	regexp = r"\b\w{" + str(i+1) + r"}\b"
	for match in re.findall(regexp, sourceText):
		words_by_len[i].append(match)
      
#randomly select words for use in poem
for i in range(len(words_by_len)):
	poem_words.append(random.choice(words_by_len[i]))

print poem_words[11] + " " + poem_words[12] + " " + poem_words[5]
print poem_words[7] + " " + poem_words[8] + "\n"
print poem_words[10] + " " + poem_words[2] + " " + poem_words[6]
print poem_words[3] + " " + poem_words[13]
print poem_words[1] + " " + poem_words[9] + " " + poem_words[4]
