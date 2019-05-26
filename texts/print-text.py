import sys, re

for line in sys.stdin.readlines():
	if line.strip() == '':
		continue
	line = line.strip('\n')
	line = re.sub(r'\t\t*', r'\t', line)
	line = re.sub(r'  +', r'\t', line)

	row = line.split('\t')
	csent = row[2].replace('-','')	
	csent = csent.replace('[','').replace(']','')
	print('%s %s\tcro\t%s\n\t   \t%s\n\teng\t%s' % (row[0], row[1], csent, row[2], row[3]))
	print()
