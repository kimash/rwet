import sys

baker = "Baker"
snark = "Snark"
forgot = "forgot"

for line in sys.stdin:
	line = line.strip()
	if baker in line and snark in line or forgot in line:
		print line
