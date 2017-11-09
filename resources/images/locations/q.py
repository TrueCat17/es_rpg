import os
import math
from PIL import Image

N = 50

def get_sqr(fp, w, h, x, y):
	minx = x * N
	miny = y * N
	maxx = min((x+1) * N, w)
	maxy = min((y+1) * N, h)
	
	for y in xrange(miny, maxy):
		for x in xrange(minx, maxx):
			if fp[x, y] == 1:
				return True
	return False

def get_free_map(fp, w, h):
	res = []
	
	maxx = int(math.ceil(float(w) / N))
	maxy = int(math.ceil(float(h) / N))
	
	for y in xrange(maxy):
		line = []
		
		for x in xrange(maxx):
			v = get_sqr(fp, w, h, x, y)
			line.append(v)
		
		res.append(line)
	
	return res


def overed(fp, m, x, y, w, h):
	minx = max(x - 10, 0)
	miny = y
	maxx = min(x + 10, w)
	maxy = min(y + 100, h)
	
	minx2 = minx / N
	miny2 = miny / N
	maxx2 = int(math.ceil(float(maxx) / N))
	maxy2 = int(math.ceil(float(maxy) / N))
	
	b = False
	for y in xrange(miny2, maxy2):
		line = m[y]
		for x in xrange(minx2, maxx2):
			if line[x]:
				b = True
				break
		if b:
			break
	if not b:
		return False
	
	for y in xrange(miny, maxy):
		for x in xrange(minx, maxx):
			if fp[x, y] == 1:
				return True
	return False

def proc(path):
	main = Image.open(path + "/main.png").convert("RGBA")
	free = Image.open(path + "/free.png")
	
	mp = main.load()
	fp = free.load()
	
	w, h = main.size
	
	m = get_free_map(fp, w, h)
	
	for y in xrange(h):
		if (y % 5) == 0:
			print y, '/', h
		
		for x in xrange(w):
			if not overed(fp, m, x, y, w, h):
				mp[x, y] = (0, 0, 0, 0)
	main.save(path + '/over.png')

e = os.path.exists
dirs = []
for path in os.listdir('.'):
	if os.path.isdir(path):
		if e(path + '/main.png') and e(path + '/free.png') and not e(path + '/over.png'):
			dirs.append(path)

n = 0
for path in dirs:
	n += 1
	print str(n) + '/' + str(len(dirs)) + ': ' + path
	proc(path)

