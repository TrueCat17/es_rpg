import os

e = os.path.exists
dirs = []
for path in os.listdir('.'):
	if os.path.isdir(path):
		if e(path + '/free.png') and e(path + '/over.png'):
			dirs.append(path)
dirs.sort()

n = 0
for path in dirs:
	n += 1
	print n, '/', len(dirs), path
	os.system("./remove_over " + path)

