init python:
	urhere = [
		[-0.5,  1.5, 0.3, 4  , 0xEEEEEE,  40, True ],
		[-0.5,  1.5, 0.1, 3  , 0x111111,  80, False],
		[-0.5,  1.5, 0.7, 5  , 0xAA33DD,  60, False],
		[-0.5,  1.5, 0.5, 4  , 0xEE3344, 100, False],
		[-0.5,  1.5, 0.8, 3  , 0xDD0000,  50, False],
		[ 1.0, -1.0, 0.1, 4  , 0xEE0011,  60, True ],
		[ 1.0, -1.0, 0.3, 3  , 0xAADD55,  30, False],
		[ 1.0, -1.0, 0.8, 5  , 0xFF5544,  90, True ],
		[ 1.0, -1.0, 0.6, 4  , 0xDD1100,  65, False],
		[ 1.0, -1.0, 0.4, 3.5, 0xEEEE11,  30, True ]
	]
	
	urhere_start_time = 0
	urhere_last_time = 0
	
	urhere_bg = im.rect('#FFF')


screen urhere:
	zorder -2.5
	
	python:
		if time.time() - urhere_last_time > 1:
			urhere_start_time = time.time()
		urhere_last_time = time.time()
	
	image urhere_bg:
		size (1.0, 1.0)
	
	for xpos_from, xpos_to, ypos, x_time, color, size, italic in urhere:
		text ("{i}"*italic + "Ты здесь не просто так"):
			xpos (xpos_to - xpos_from) * ((urhere_last_time - urhere_start_time) % x_time) / x_time + xpos_from
			ypos ypos
			color color
			text_size size

