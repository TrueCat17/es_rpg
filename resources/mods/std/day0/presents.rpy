init python:
	presents_time1 = 6
	presents_time2 = 2
	presents_time3 = 6
	
	presents_appearance_time = 1
	
	presents_start_time = 0
	def show_presents():
		global presents_start_time
		presents_start_time = time.time()
		show_screen('presents')
		pause(presents_time1 + presents_time2 + presents_time3)
	def hide_presents():
		hide_screen('presents')

screen presents:
	python:
		dtime = time.time() - presents_start_time
		
		if dtime < presents_time1:
			text = 'Snowcrash.Studio\nПредставляет'
			if dtime < presents_appearance_time:
				alpha = dtime
			elif dtime > presents_time1 - presents_appearance_time:
				alpha = (presents_time1 - dtime) / presents_appearance_time
			else:
				alpha = 1
		elif dtime < presents_time1 + presents_time2:
			text = ''
			alpha = 0
		else:
			text = 'Бесконечное лето\nRPG'
			dtime -= presents_time1 + presents_time2
			if dtime < presents_appearance_time:
				alpha = dtime
			elif dtime > presents_time3 - presents_appearance_time:
				alpha = (presents_time3 - dtime) / presents_appearance_time
			else:
				alpha = 1
	
	text text:
		alpha alpha
		bold True
		text_align 'center'
		align (0.5, 0.5)
		color 0xFFFFFF
		text_size 30
