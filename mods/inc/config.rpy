init -998 python:
	
	start_screens = 'location sprites dialogue_box'
	
	
	config = renpy.config
	
	if not config.has_attr('fps_meter'):
		config.fps_meter = True
	
	if not config.has_attr('text_cps'):
		config.text_cps = 60
	
	if not config.has_attr('music_volume'):
		config.music_volume = 100
		config.voice_volume = 100
		config.ambience_volume = 100
	
