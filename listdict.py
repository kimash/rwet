#Kim Ash
#creates list of lines and randomly sample it
#uses dictionary to remove punctuation from poem

import sys
import random

linelist = list()
punctuation = {'.': '\n', ', ': ' ', '; ': '\n', '"': '', '--': '--\n', '(': ' ', ')': '', '_': ''}

for line in sys.stdin:
	line = line.strip()
	if len(line) > 0:
		for key in punctuation.keys():
			line = line.replace(key, punctuation[key])
		linelist.append(line)

selection = random.sample(linelist, 8)

for item in selection:
	print item
