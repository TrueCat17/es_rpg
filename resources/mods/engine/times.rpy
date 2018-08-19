init -1000 python:
	
	def make_time(name, r, g, b):
		def func():
			persistent.next_rgb = r, g, b
			persistent.next_r, persistent.next_g, persistent.next_b = persistent.next_rgb
			persistent.next_time = name
			if not has_screen('locations'):
				persistent.cur_rgb = r, g, b
				persistent.cur_r, persistent.cur_g, persistent.cur_b = persistent.cur_rgb
				persistent.cur_time = name
		
		globals()[name + '_time'] = func
	
	make_time('day',    255, 255, 255) # def day_time
	make_time('sunset', 240, 210, 255)
	make_time('night',  160, 200, 210)
	
	day_time()

