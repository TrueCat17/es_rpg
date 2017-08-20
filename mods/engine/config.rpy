init -998 python:
	
	start_screens = 'location sprites dialogue_box'
	
	
	config = renpy.config
	
	if config.fps_meter is None:
		config.fps_meter = True
	
	if config.text_cps is None:
		config.text_cps = 60
	
	if config.music_volume is None:
		config.music_volume = 100
		config.voice_volume = 100
		config.ambience_volume = 100
	
