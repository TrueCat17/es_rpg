init -1001 python:
	
	# Особенности реализации:
	
	# Все функции возвращают в качестве результата строку (принимают тоже строки)
	# При обновлении экрана (рендере) обновляются все image
	# Сначала выполняются все im-функции
	
	# По сути - это просто манипуляции со строками
	# Т. е. довольно дёшево относительно манипуляций с реальными изображениями
	
	# Потом, когда получена окончательная строка, по ней составляется изображение
	# Т. к. используется кэш, то как бы сложны не были манипуляции, выполняются они только один раз для каждой окончательной строки
	# Разумеется, при превышении определённого размера, часть кэша (наиболее редко используемая) удаляется
	# Если запрашиваемая часть была когда-то удалена - она создаётся заново (Ваш К.О.)
	#   Если часть используемых промежуточных изображений сохранилась в кэше, то она тоже используется
	
	# Так как тут нет всяких ограничений типа "im-функции принимают на вход только путь до изображения или image и возвращают image", то
	# в качестве аргумента любой функции может быть использована любая строка
	# (В отличие от Ren'Py, где результат ConditionSwitch не может быть подан на вход im.Scale, например)
	#                                                                       (См. 9-й слайд 4-го урока лолбота)
	
	# + из-за автообновления такая чушь из оригинала:
	# image cs normal stethoscope far = ConditionSwitch(
	# 	"persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
	# 	"persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
	# 	True,im.Composite((630,1080), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_normal.png") )
	
	# заменяется на лаконичное
	# image cs normal stethoscope far = im.MatrixColor(
	# 	im.Composite((630,1080),
	# 		(0,0), "images/sprites/far/cs/cs_1_body.png",
	# 		(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",
	# 		(0,0), "images/sprites/far/cs/cs_1_normal.png"
	# 	),
	# 	persistent.tint_sprite_time
	# )
	
	# Где persistent.tint_sprite_time меняется вместе с persistent.sprite_time
	# Но оригинальный вариант тоже работает, разумеется
	
	
	
	def ConditionSwitch(*args):
		if len(args) % 2:
			out_msg('ConditionSwitch', 'Ожидалось чётное количество аргументов')
			return ''
		
		for i in xrange(0, len(args), 2):
			cond = args[i]
			if type(cond) == bool and cond == True:
				return args[i + 1]
			
			cond_res = eval(cond)
			if cond_res:
				return args[i + 1]
		
		out_msg('ConditionSwitch', 'Ни одно условие не выполнено')
		return args[1]
	
	def get_back_with_color(image, color = '#000', alpha = 0.05):
		w, h = get_texture_width(image), get_texture_height(image)
		return im.Composite((w, h),
		                    (0, 0), im.Alpha(im.Rect(color, w, h), alpha),
		                    (0, 0), image)
	
	
	class Matrix(list):
		def __new__(cls, *args):
			size = len(args)
			
			if size == 1:
				args = args[0]
			else:
				if size != 0 and size != 20 and size != 25:
					out_msg('Matrix', 'Ожидалось 20 или 25 значений, получено ' + str(len(args)))
				args = list(args) + [0] * (25 - size)
			
			return list.__new__(cls, args)
		
		def __init__(self, *args):
			size = len(args)
			
			if size == 1:
				args = args[0]
			else:
				if size != 0 and size != 20 and size != 25:
					out_msg('Matrix', 'Ожидалось 20 или 25 значений, получено ' + str(len(args)))
				args = list(args) + [0] * (25 - size)
			
			list.__init__(self, args)
		
		def __str__(self):
			return ' '.join(map(str, self))
		
		def __mul__(self, other):
			res = Matrix()
			
			for y in xrange(5):
			    for x in xrange(5):
			        for i in xrange(5):
			            res[y * 5 + x] += self[i * 5 + x] * other[y * 5 + i]
			return res
		
		
		@staticmethod
		def identity():
			res = Matrix(
				1, 0, 0, 0, 0,
				0, 1, 0, 0, 0,
				0, 0, 1, 0, 0,
				0, 0, 0, 1, 0,
				0, 0, 0, 0, 1
			)
			return res
		
		@staticmethod
		def tint(r, g, b, a = 1):
			res = Matrix(
				r, 0, 0, 0, 0,
				0, g, 0, 0, 0,
				0, 0, b, 0, 0,
				0, 0, 0, a, 0,
				0, 0, 0, 0, 1
			)
			return res
		
		@staticmethod
		def saturation(level, desat=(0.2126, 0.7152, 0.0722)):
			r, g, b = desat
			def I(a, b):
				return a + (b - a) * level
			
			res = Matrix(
				I(r, 1), 	I(g, 0), 	I(b, 0), 	0, 	0,
				I(r, 0), 	I(g, 1), 	I(b, 0), 	0, 	0,
				I(r, 0), 	I(g, 0), 	I(b, 1), 	0, 	0,
				0, 			0, 			0, 			1, 	0,
				0, 			0, 			0, 			0, 	1
			)
			return res
		
		@staticmethod
		def invert():
			res = Matrix(
				-1, 0, 0, 0, 1,
				0, -1, 0, 0, 1,
				0, 0, -1, 0, 1,
				0, 0, 0,  1, 0,
				0, 0, 0,  0, 1
			)
			return res
		
		@staticmethod
		def brightness(b):
			res = Matrix(
				1, 0, 0, 0, b,
				0, 1, 0, 0, b,
				0, 0, 1, 0, b,
				0, 0, 0, 1, 0,
				0, 0, 0, 0, 1
			)
			return res
		
		@staticmethod
		def contrast(c):
			return Matrix.brightness(-0.5) * Matrix.tint(c, c, c) * Matrix.brightness(0.5)
		
		@staticmethod
		def opacity(o):
			res = Matrix(
				1, 0, 0, 0, 0,
				0, 1, 0, 0, 0,
				0, 0, 1, 0, 0,
				0, 0, 0, o, 0,
				0, 0, 0, 0, 1
			)
			return res
		
		@staticmethod
		def colorize(black_color, white_color):
			r0, g0, b0, _a0 = renpy.easy.color(black_color)
			r1, g1, b1, _a1 = renpy.easy.color(white_color)
			
			r0 /= 255.0
			g0 /= 255.0
			b0 /= 255.0
			r1 /= 255.0
			g1 /= 255.0
			b1 /= 255.0
			
			res = Matrix(
				(r1-r0), 0, 0, 0, r0,
				0, (g1-g0), 0, 0, g0,
				0, 0, (b1-b0), 0, b0,
				0, 0, 0, 1, 0,
				0, 0, 0, 0, 1
			)
			return res
	
	
	
	class Im():
		matrix = Matrix
		
		
		@staticmethod
		def scale(image, w, h):
			return 'Scale|(' + image + ')|' + str(int(w)) + '|' + str(int(h))
		
		@staticmethod
		def factor_scale(image, k):
			return 'FactorScale|(' + image + ')|' + str(k)
		
		@staticmethod
		def renderer_scale(image, w, h):
			return 'RendererScale|(' + image + ')|' + str(int(w)) + '|' + str(int(h))
		
		@staticmethod
		def crop(image, rect):
			rect = map(lambda f: str(int(f)), rect)
			rect = ' '.join(rect)
			return 'Crop|(' + image + ')|(' + rect + ')'
		
		
		@staticmethod
		def composite(*args):
			if (len(args) % 2) == 0:
				out_msg('im.Composite', 'Ожидалось нечётное количество аргументов')
				return ''
			
			size = str(int(args[0][0])) + ' ' + str(int(args[0][1]))
			res = 'Composite|(' + size + ')'
			
			for i in xrange(1, len(args) - 1, 2):
				pos = str(int(args[i][0])) + ' ' + str(int(args[i][1]))
				img = str(args[i + 1])
				
				res += '|(' + pos + ')|(' + img + ')'
			return res
		
		
		@staticmethod
		def flip(image, horizontal = False, vertical = False):
			return 'Flip|(' + image + ')|' + str(bool(horizontal)) + '|' + str(bool(vertical))
		
		
		@staticmethod
		def matrix_color(image, matrix):
			return 'MatrixColor|(' + image + ')|(' + str(matrix) + ')'
		
		@staticmethod
		def grayscale(image, desat=(0.2126, 0.7152, 0.0722)):
			return im.matrix_color(image, matrix.saturation(0.0, desat))
		
		@staticmethod
		def sepia(image, tint=(1.0, 0.94, 0.76), desat=(0.2126, 0.7152, 0.0722)):
			return im.matrix_color(image, im.matrix.saturation(0.0, desat) * im.matrix.tint(tint[0], tint[1], tint[2]))
		
		
		@staticmethod
		def recolor(image, r, g, b, a = 255):
			colors = map(str, (r + 1, g + 1, b + 1, a + 1))
			colors = ' '.join(colors)
			return 'ReColor|(' + image + ')|(' + colors + ')'
		
		@staticmethod
		def color(image, color):
			r, g, b, a = renpy.easy.color(color)
			return im.recolor(image, r, g, b, a)
		
		@staticmethod
		def alpha(image, alpha):
			return im.recolor(image, 255, 255, 255, int(alpha * 255))
		
		
		@staticmethod
		def rotozoom(image, angle, zoom):
			return 'Rotozoom|(' + image + ')|(' + str(int(angle)) + ')|(' + str(zoom) + ')'
		
		
		@staticmethod
		def mask(image, mask, value, channel = 'r', cmp_func_name = 'le', alpha_channel = 'a', alpha_image = 1):
			return 'Mask|(' + image + ')|(' + mask + ')|(' + channel + ')|(' + str(int(value)) + ')|(' + cmp_func_name + ')|(' + alpha_channel + ')|(' + str(alpha_image) + ')'
		@staticmethod
		def alpha_mask(image, mask):
			return im.mask(image, mask, 0, 'r', 'g', 'r', 2)
		
		
		@staticmethod
		def motion_blur(image, cx = 0.5, cy = 0.5, dist = 5):
			return 'MotionBlur|(' + image + ')|' + str(cx) + '|' + str(cy) + '|' + str(int(dist))
		
		
		@staticmethod
		def rect(color, width = 1, height = 1):
			r, g, b, a = renpy.easy.color(color)
			m = im.matrix.invert() * im.matrix.tint(r / 255.0, g / 255.0, b / 255.0, a / 255.0)
			return im.scale(im.matrix_color('images/bg/black.jpg', m), width, height)
		@staticmethod
		def circle(color, width = 64, height = None):
			r, g, b, a = renpy.easy.color(color)
			m = im.matrix.invert() * im.matrix.tint(r / 255.0, g / 255.0, b / 255.0, a / 255.0)
			return im.scale(im.matrix_color('images/bg/black_circle.png', m), width, height or width)
		
		@staticmethod
		def bar(progress_end, progress_start = 0, vertical = False, ground = None, hover = None):
			if ground is None:
				ground = vbar_ground if vertical else bar_ground
			if hover is None:
				hover  = vbar_hover if vertical else bar_hover
			tw, th = get_texture_width(ground), get_texture_height(ground)
			
			if vertical:
				x, y = 0, progress_start * th
				w, h = tw, (progress_end - progress_start) * th
			else:
				x, y = progress_start * tw, 0
				w, h = (progress_end - progress_start) * tw, th
			
			x, y = in_bounds(int(x), 0, tw), in_bounds(int(y), 0, th)
			w, h = in_bounds(int(w), 0, tw), in_bounds(int(h), 0, th)
			
			if w <= 0 or h <= 0:
				return ground
			if (x, y, w, h) == (0, 0, tw, th):
				return hover
			
			return im.composite((tw, th),
			                    (0, 0), ground,
			                    (x, y), im.crop(hover, (x, y, w, h)))
		
		@staticmethod
		def save(image, path, width = None, height = None):
			save_image(image, path, str(width and int(width)), str(height and int(height)))
		
		
		Scale = scale
		FactorScale = factor_scale
		RendererScale = renderer_scale
		Crop = crop
		
		Composite = composite
		
		Flip = flip
		
		MatrixColor = matrix_color
		Grayscale = grayscale
		Sepia = sepia
		
		ReColor = Recolor = recolor
		Color = color
		Alpha = alpha
		
		Rotozoom = RotoZoom = rotozoom
		
		Mask = mask
		AlphaMask = alpha_mask
		
		MotionBlur = motion_blur
		
		Rect = rect
		Circle = circle
		Bar = bar
		
		Save = save

init -1000 python:
	im = Im

