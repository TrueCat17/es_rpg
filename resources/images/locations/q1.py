import os

pngs = []
for d, _, fs in os.walk('.'):
	for f in fs:
		if f.endswith('.png'):
			pngs.append(os.path.join(d, f))

def get_size(f):
	return os.stat(f).st_size


start_sizes = end_sizes = 0

num = 0
for png in pngs:
	num += 1
	print num, '/', len(pngs)
	
	s = get_size(png)
	start_sizes += s
	os.system('mogrify -strip ' + png)
	os.system('optipng -strip all -o7 ' + png)
	e = get_size(png)
	end_sizes += e
	
	print s - e, start_sizes, end_sizes
