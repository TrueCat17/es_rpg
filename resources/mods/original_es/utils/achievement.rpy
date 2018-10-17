init python:
	def show_achievement(achievement):
		global achievement_start_time
		achievement_start_time = time.time()
		show_screen('achievement')

screen achievement:
	pass
