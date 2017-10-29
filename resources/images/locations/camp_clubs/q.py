from PIL import Image

im = Image.open('main.png')
pixels = im.load()

def f(a, n):
	return 255 if a == 255 else int(a / n) * n

w, h = im.size
for y in xrange(h):
	if (y % 10) == 0:
		print str(y) + '/' + str(h)
	for x in xrange(w):
		color = list(pixels[x, y])
		for i in xrange(len(color)):
			color[i] = f(color[i], 3)
		pixels[x, y] = tuple(color)

im.save('tmp.png')
