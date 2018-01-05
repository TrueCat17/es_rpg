init python:
	def day_time():
		persistent.tint_sprite_time = im.matrix.tint(1, 1, 1)
		persistent.sprite_time = 'day'
	
	def sunset_time():
		persistent.tint_sprite_time = im.matrix.tint(0.94, 0.82, 1)
		persistent.sprite_time = 'sunset'
	
	def night_time():
		persistent.tint_sprite_time = im.matrix.tint(0.63, 0.78, 0.82)
		persistent.sprite_time = 'night'
	
	
	def prolog_time():
		pass
	
	def new_chapter(day_num, day_name):
		pass
