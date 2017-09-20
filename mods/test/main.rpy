init python:
	set_fps(60)
	
	mods['test_label'] = 'test'

label test_label:
	image bg bus_stop = im.MatrixColor('images/bg/bus_stop.jpg',
											im.matrix.saturation(0.5*4))
	scene bg bus_stop:
		size (1.0, 1.0)
	me "qwe"

