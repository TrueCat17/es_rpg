init python:
	spr_default_background = 'images/bg/black.jpg'
	spr_background = spr_default_background
	
	def set_background(image):
		global spr_background
		spr_background = image
	
	def set_scene(name):
		image = get_image(name)
		if image:
			set_background(image)
		else:
			set_background(spr_default_background)


screen sprites:
	window:
		image spr_background:
			xysize (1, 1)
		
