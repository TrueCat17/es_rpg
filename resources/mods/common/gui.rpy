init python:
	gui.dialogue_text_font = 'FixEx3'
	gui.name_text_font = 'FixEx3'
	
	gui.choice_button_text_font = 'FixEx3'
	
	gui.dialogue_menu_button_width = 0
	
	
	def set_interface_time(name):
		gui.dialogue_box_bg = 'images/gui/dialogue/' + name + '/voice.png'
		gui.name_box_bg = 'images/gui/dialogue/' + name + '/name.png'
		
		gui.dialogue_prev_ground = 'images/gui/dialogue/' + name + '/to_prev.png'
		gui.dialogue_next_ground = 'images/gui/dialogue/' + name + '/to_next.png'
		
		db.update_styles()
	
	signals.add('time', set_interface_time)
	day_time()
	
	make_time('winter')
