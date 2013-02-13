import sys
import random

silence = "silence"
nothing = "nothing"
all_lines = list()

for line in sys.stdin:
	line = line.strip()
	if silence in line or nothing in line:
		line = line.replace(".  ", ".\n")
		line = line.replace("!  ", "!\n")
		all_lines.append(line)

random.shuffle(all_lines)
		
for line in all_lines:		
	print line
