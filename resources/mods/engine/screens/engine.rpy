screen engine:
	if not has_screen('console'):
		key 'p' action make_screenshot
		
		$ engine_shift = False
		key 'LEFT SHIFT'  action SetVariable('engine_shift', True) first_delay 0
		key 'RIGHT SHIFT' action SetVariable('engine_shift', True) first_delay 0
		if engine_shift:
			key 'o' action show_console
		
		if not has_screen('prev_text') and not db_hide_interface:
			key 'ESCAPE' action show_pause
		
		key config.quick_load_key action quick_load
		key config.quick_save_key action quick_save

