init python:
	mods['test_label'] = 'test'

label test_label:
	$ set_fps(60)
	
	image bg bus_stop = im.MatrixColor('images/bg/bus_stop.jpg', im.matrix.saturation(5))
	scene bg bus_stop
	
	me "{color=FFFFFF}qwe!{/color}ewq"
	call test_call
	me "..."

label test_call:
	dv "qwe!"
	if 4 < 5:
		return
	$ print 4
	us "ewq!"
