init -10 python:
	fps_meter_size = 25
	fps_meter_color = 0xFFFF00
	fps_meter_font = 'Alcdnova'
	fps_meter_xalign, fps_meter_yalign = 0.01, 0.01
	
	
	fps_meter_last_upd = 0
	
	count_last_fps = 60
	fps_array = []
	
	def get_middle_fps(last_fps):
		global fps_array
		
		fps_array.append(last_fps)
		fps_array = fps_array[-count_last_fps:]
		
		mid_fps = sum(fps_array) / float(len(fps_array))
		return min(ceil(mid_fps), get_fps())


screen fps_meter:
	window:
		python:
			spend = time.time() - fps_meter_last_upd
			fps_meter_last_upd = time.time()
		
			last_fps = 1.0 / spend
	
		text get_middle_fps(last_fps):
			font fps_meter_font
			size fps_meter_size
			color fps_meter_color
			xalign fps_meter_xalign
			yalign fps_meter_yalign
