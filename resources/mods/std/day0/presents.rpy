init python:
	presents_time = 5
	
	presents_appearance_time = 1
	
	presents_start_time = 0
	def show_presents():
		global presents_start_time
		presents_start_time = get_game_time()
		show_screen('presents')
		pause(presents_time)
	def hide_presents():
		hide_screen('presents')

screen presents:
	python:
		dtime = get_game_time() - presents_start_time
		
		if dtime < presents_time:
			text = 'Бесконечное лето\nRPG'
			if dtime < presents_appearance_time:
				alpha = dtime / presents_appearance_time
			elif dtime > presents_time - presents_appearance_time:
				alpha = (presents_time - dtime) / presents_appearance_time
			else:
				alpha = 1
		else:
			text = ''
			alpha = 0
	
	text text:
		alpha alpha
		bold True
		text_align 'center'
		align (0.5, 0.5)
		color 0xFFFFFF
		text_size 30
