init python:
	mods['test_label'] = 'test'

label test_label:
	$ set_fps(60)
	
	image bg bus_stop = im.MatrixColor('images/bg/bus_stop.jpg',
											im.matrix.saturation(0.5*4))
	scene bg bus_stop
	me "qwe"

