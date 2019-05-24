import sys, re

for line in sys.stdin.readlines():
	line = line.strip('\n')
	line = re.sub(r'\t\t*', r'\t', line)

	row = line.split('\t')
	
	print(row[0], row[1], '\tcro\t', row[2], '\n\teng\t', row[3])
