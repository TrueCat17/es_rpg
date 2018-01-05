init python:
	set_fps(60)
	
	draw_fps = not False
	IMAGE_RENDER = False
	
	start_screens = 'snow'
	if draw_fps:
		start_screens += ' fps_meter'
	
	COUNT = 1400
	
	width, height = get_stage_width(), get_stage_height()
	
	objs = []
	for i in xrange(COUNT):
		size = random.randint(2, 10)
		
		obj = {}
		obj['x'] = random.randint(0, width - size - 1)
		obj['y'] = random.randint(0, height - size - 1)
		obj['dx'] = (random.random() * 2 - 1) * size / 8
		obj['dy'] = (random.random() * 7 + 5) * size / 30
		
		if IMAGE_RENDER:
			obj['image'] = im.Scale('images/anim/snow.png', size, size)
		else:
			obj['size'] = (size, size)
		objs.append(obj)
	
	prev_time = prev_time_update = time.time()
	frame_times = []


screen snow:
	zorder -2.5
	
	key 'ESCAPE' action show_pause
	
	image 'images/bg/bus_stop.jpg':
		size (1.0, 1.0)
	
	python:
		k = (time.time() - prev_time_update) * 60
		prev_time_update = time.time()
		
		width, height = get_stage_width(), get_stage_height()
		
		if IMAGE_RENDER:
			tmp_image_args = [(width, height)]
			for obj in objs:
				obj['x'] = (obj['x'] + obj['dx'] * k) % width
				obj['y'] = (obj['y'] + obj['dy'] * k) % height
				
				tmp_image_args.append((obj['x'], obj['y']))
				tmp_image_args.append(obj['image'])
			tmp_image = im.Composite(*tmp_image_args)
		else:
			for obj in objs:
				obj['x'] = (obj['x'] + obj['dx'] * k) % width
				obj['y'] = (obj['y'] + obj['dy'] * k) % height
	
	if IMAGE_RENDER:
		image tmp_image
	else:
		for obj in objs:
			image 'images/anim/snow.png':
				xpos int(obj['x'])
				ypos int(obj['y'])
				size obj['size']
	
	python:
		if not draw_fps:
			dtime = (time.time() - prev_time) * 1000
			prev_time = time.time()
			
			frame_times.append(dtime)
			frame_times = frame_times[-300:]
			
			mid_time = sum(frame_times) / len(frame_times)
			fps = int(1000.0 / mid_time * 10) / 10.0
			print fps


label start:
	while True:
		pause 0.1
