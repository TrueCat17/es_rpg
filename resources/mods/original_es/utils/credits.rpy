init python:
	credits_ystart = 1.3
	credits_yend = -1.0
	
	credits_time = 87
	
	def show_credits():
		global credits_start_time
		credits_start_time = time.time()
		show_screen('credits')

screen credits:
	python:
		if time.time() - credits_start_time >= credits_time:
			hide_screen('credits')
	
	vbox:
		spacing 10
		xalign 0.5
		ypos credits_ystart + (credits_yend - credits_ystart) * (time.time() - credits_start_time) / credits_time
		
		for text_line in credits_text:
			text text_line:
				xalign 0.5
				text_size 50 * get_stage_height() / 1080
				color 0xFFFFFF

