init -1000 python:
	
	def make_time(name, r, g, b):
		def func():
			persistent.st_r, persistent.st_g, persistent.st_b = r, g, b # st -> sprite_time
			persistent.sprite_time = name
			if not has_screen('locations'):
				persistent.lt_r, persistent.lt_g, persistent.lt_b = r, g, b # lt -> location_time
				persistent.location_time = name
		
		globals()[name + '_time'] = func
	
	make_time('day',    255, 255, 255) # def day_time
	make_time('sunset', 240, 210, 255)
	make_time('night',  160, 200, 210)
	
	day_time()

