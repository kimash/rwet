#Kim Ash
#charlen.py
#uses regex to find words of char lengths 1-9
#creates poem of format 3 5 9 / 2 4 6 / 7 8

import sys
import random
import re

#list of 9 empty lists, one for each length
words_by_len = [ [], [], [], [], [], [], [], [], [] ]

#list for words that will be in poem
poem_words = list()

for line in sys.stdin:
  line = line.strip()
  for i in range(len(words_by_len)):
    #find words of each length (i+1 because range() starts at 0)
    regexp = r"\b\w{" + str(i+1) + r"}\b"
    for match in re.findall(regexp, line):
      words_by_len[i].append(match)

#randomly select words for use in poem      
for i in range(len(words_by_len)):
	poem_words.append(random.choice(words_by_len[i]))

print poem_words[2] + " " + poem_words[4] + " " + poem_words[8]
print poem_words[1] + " " + poem_words[3] + " " + poem_words[5]
print poem_words[6] + " " + poem_words[7]
