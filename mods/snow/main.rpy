init python:
	mods['snow'] = 'snow'


screen snow:
	zorder -2.5
	
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
				pos (int(obj.x), int(obj.y))
#				xpos int(obj.x)
#				ypos int(obj.y)
	
	use fps_meter



label snow:
	$ set_fps(60)
	scene bg bus_stop
	
	python:
		IMAGE_RENDER = True
		
		COUNT = 5000
		
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
	
	show screen snow
	
	while True:
		pause 0.1
