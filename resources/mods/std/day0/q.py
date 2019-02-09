name = 'main.rpy'

f = open(name)
lines = map(lambda s: s[:-1], f.readlines())

for i in xrange(len(lines)):
	line = lines[i]
	
	n = 0
	while n < len(line) and line[n] == '\t':
		n += 1
	
	if n < len(line) and line[n] not in ('"', "'"):
		line = line[:n] + '"' + line[n:] + '"'
	lines[i] = line

f = open(name, 'w')
f.writelines(map(lambda s: s + '\n', lines))

