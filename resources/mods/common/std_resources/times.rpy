init -1000 python:
	def day_time():
		persistent.st_r = 255
		persistent.st_g = 255
		persistent.st_b = 255
		persistent.sprite_time = 'day'
	
	def sunset_time():
		persistent.st_r = 240
		persistent.st_g = 210
		persistent.st_b = 255
		persistent.sprite_time = 'sunset'
	
	def night_time():
		persistent.st_r = 160
		persistent.st_g = 200
		persistent.st_b = 210
		persistent.sprite_time = 'night'
	
	
	def prolog_time():
		pass
	
	def new_chapter(day_num, day_name):
		pass
