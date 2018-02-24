init -997 python:
	
	start_screens = 'location sprites dialogue_box inventory fps_meter'
	
	
	config = renpy.config
	
	config.quick_save_table = 'quick'
	config.quick_save_name  = '0'
	config.quick_load_key = 'L'
	config.quick_save_key = 'Q'
	
	config.count_prev_texts = 25
	
	
	if config.fps_meter is None:
		config.fps_meter = True
	
	if config.text_cps is None:
		config.text_cps = 60
	
	for std_mixer in std_mixers:
		if config[std_mixer + '_volume'] is None:
			config[std_mixer + '_volume'] = 1
		renpy.music.set_mixer_volume(config[std_mixer + '_volume'], std_mixer)
	
