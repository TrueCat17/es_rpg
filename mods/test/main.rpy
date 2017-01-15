init python:
	mods['test_label'] = 'test'

label test_label:
	$ set_fps(60)
	scene bg bus_stop
	
	me "1"
	call test_call
	me "..."

label test_call:
	dv "qwe!"
	if 4 < 5:
		return
	$ print 4
	us "ewq!"
