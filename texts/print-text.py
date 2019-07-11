import sys, re
lno=1
for line in sys.stdin.readlines():
	if line.strip() == '':
		continue
	if line[0] == '#': 
		continue
	line = line.strip('\n')
	line = re.sub(r'\t\t*', r'\t', line)
	line = re.sub(r'  +', r'\t', line)

	row = line.split('\t')
	if len(row) < 4:
		print('WARNING:%d\t%s' % (lno, row), file=sys.stderr)
		continue
	csent = row[2].replace('-','')	
	csent = csent.replace('[','').replace(']','')
	print('%s %s\tcro\t%s\n\t   \t%s\n\teng\t%s' % (row[0], row[1], csent, row[2], row[3]))
	print()
	lno+=1
