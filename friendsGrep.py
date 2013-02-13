import sys

friends = "friends"

for line in sys.stdin:
	line = line.strip()
	if friends in line:
		print line
