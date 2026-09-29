init -1000 python:
	sfx = {}
	
	def add_sfx(name, filename = None, path = 'sound/sfx/', ext = '.ogg'):
		sfx[name] = path + (filename or name) + ext
	
	add_sfx('mystery_movement')
	add_sfx('computer_noise')
	add_sfx('keyboard_mouse_computer_noise')
	add_sfx('message', filename = 'icq', ext = '.mp3')
	add_sfx('close_door')
	
	add_sfx('bus_door_open')
	add_sfx('bus_door_close')
	add_sfx('bus_idle')
	add_sfx('bus_interior_moving')
	
	add_sfx('horn')
	add_sfx('knock_door')
	add_sfx('stomach_growl')
