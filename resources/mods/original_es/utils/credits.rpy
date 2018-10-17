init python:
	credits_ystart = 1.3
	credits_yend = -1.0
	
	credits_time = 87
	
	def show_credits():
		global credits_start_time
		credits_start_time = time.time()
		show_screen('credits')
		renpy.pause(credits_time)

screen credits:
	python:
		if time.time() - credits_start_time >= credits_time:
			hide_screen('credits')
	
	text credits_text:
		xalign 0.5
		ypos credits_ystart + (credits_yend - credits_ystart) * (time.time() - credits_start_time) / credits_time
