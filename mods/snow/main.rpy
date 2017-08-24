init python:
	mods['snow'] = 'snow'
	start_screens = 'snow'
	
	IMAGE_RENDER = False
	
	COUNT = 1000
	
	width, height = get_stage_width(), get_stage_height()
	
	objs = []
	for i in xrange(COUNT):
		obj = Object()
		obj.size = random.randint(2, 10)
		obj.x = random.randint(0, width - obj.size - 1)
		obj.y = random.randint(0, height - obj.size - 1)
		obj.dx = (random.random() * 2 - 1) * obj.size / 8
		obj.dy = (random.random() * 7 + 5) * obj.size / 30
		obj.image = im.Scale('images/anim/snow.png', obj.size, obj.size)
		objs.append(obj)
	
	prev_time = time.time()
	frame_times = []


screen snow:
	zorder -2.5
	
	image 'images/bg/bus_stop.jpg':
		size (1.0, 1.0)
	
	python:
		width, height = get_stage_width(), get_stage_height()
		tmp_image_args = [(width, height)]
		
		for obj in objs:
			next_x, next_y = obj.x + obj.dx, obj.y + obj.dy
			
			if next_x < -obj.size:
				next_x = width
			elif next_x > width:
				next_x = 0
			
			if next_y > height:
				next_y = 0
			
			obj.x, obj.y = next_x, next_y
			if IMAGE_RENDER:
				tmp_image_args.append((next_x, next_y))
				tmp_image_args.append(obj.image)
		
		if IMAGE_RENDER:
			tmp_image = im.Composite(*tmp_image_args)
	
	if IMAGE_RENDER:
		image tmp_image
	else:
		for obj in objs:
			image obj.image:
				xpos int(obj.x)
				ypos int(obj.y)
	
	python:
		dtime = (time.time() - prev_time) * 1000
		prev_time = time.time()
		
		frame_times.append(dtime)
		frame_times = frame_times[-30:]
		
		mid_time = int(sum(frame_times) / len(frame_times) * 10) / 10.0
		fps = 1000.0 / mid_time
		print fps
	
#	use fps_meter


label snow:
	$ set_fps(60)
	
	while True:
		pause 0.1
