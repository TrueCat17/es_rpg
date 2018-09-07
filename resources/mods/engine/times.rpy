init -1000 python:
	
	times = {}
	def make_time(name, **kwargs):
		def func():
			times['next_name'] = name
			
			if not has_screen('location') or not times.has_key('current_name') or not cur_location:
				set_time_direct()
			else:
				place = {
					'x': me.x,
					'y': me.y,
					'width': 0,
					'height': 0
				}
				set_location(cur_location.name, place)
		
		times[name] = {}
		for key in kwargs:
			times[name][key] = kwargs[key]
		globals()[name + '_time'] = func
	
	def set_time_direct():
		name = times['current_name'] = times['next_name']
		times['next_name'] = None
		
		g = globals()
		for key in times[name]:
			g[key + '_time_rgb'] = times[name][key]
	
	make_time('day',    sprite=(255, 255, 255), location=(255, 255, 255)) # def day_time
	make_time('sunset', sprite=(240, 210, 255), location=(240, 210, 255))
	make_time('night',  sprite=(160, 200, 210), location=(140, 180, 210))
	
	day_time()

