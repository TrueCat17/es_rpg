init python:
	urhere = [
		[-0.5,  1.5, 0.3, 4  , '#EEEEEE',  40, True ],
		[-0.5,  1.5, 0.1, 3  , '#111111',  80, False],
		[-0.5,  1.5, 0.7, 5  , '#AA33DD',  60, False],
		[-0.5,  1.5, 0.5, 4  , '#EE3344', 100, False],
		[-0.5,  1.5, 0.8, 3  , '#DD0000',  50, False],
		[ 1.0, -1.0, 0.1, 4  , '#EE0011',  60, True ],
		[ 1.0, -1.0, 0.3, 3  , '#AADD55',  30, False],
		[ 1.0, -1.0, 0.8, 5  , '#FF5544',  90, True ],
		[ 1.0, -1.0, 0.6, 4  , '#DD1100',  65, False],
		[ 1.0, -1.0, 0.4, 3.5, '#EEEE11',  30, True ]
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

