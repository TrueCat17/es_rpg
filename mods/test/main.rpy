init python:
	set_fps(60)
	
	m = im.matrix.brightness(0.5) * im.matrix.invert()

label start:
	image bg bus_stop = im.MatrixColor('images/bg/bus_stop.jpg', m)
	
	scene bg bus_stop:
		size (1.0, 1.0)
	me "qwe"

