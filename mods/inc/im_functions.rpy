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
	
	
	
	
	
	class ImMatrix:
		def __init__(self, t = None):
			if t is None:
				t = [0] * 25
			self.t = t
		
		def __str__(self):
			res = str(self.t[0])
			for i in xrange(1, len(self.t)):
				res += ' ' + str(self.t[i])
			return res
		
		def __mul__(self, other):
			a, b = self.t, other.t
		    t = [ 0 ] * 25
		    for y in xrange(5):
		        for x in xrange(5):
		            for i in xrange(5):
		                t[x + y * 5] += a[x + i * 5] * b[i + y * 5]
		    res = ImMatrix(t)
		    return res
		
		
		def identity(self):
			res = ImMatrix((
				1, 0, 0, 0, 0,
				0, 1, 0, 0, 0,
				0, 0, 1, 0, 0,
				0, 0, 0, 1, 0,
				0, 0, 0, 0, 1
			))
			return res
		
		def tint(self, r, g, b, a = 1):
			res = ImMatrix((
				r, 0, 0, 0, 0,
				0, g, 0, 0, 0,
				0, 0, b, 0, 0,
				0, 0, 0, a, 0,
				0, 0, 0, 0, 1
			))
			return res
		
		def saturation(self, level, desat=(0.2126, 0.7152, 0.0722)):
			r, g, b = desat
			def I(a, b):
				return a + (b - a) * level
			
			res = ImMatrix((
				I(r, 1), 	I(g, 0), 	I(b, 0), 	0, 	0,
				I(r, 0), 	I(g, 1), 	I(b, 0), 	0, 	0,
				I(r, 0), 	I(g, 0), 	I(b, 1), 	0, 	0,
				0, 			0, 			0, 			1, 	0,
				0, 			0, 			0, 			0, 	1
			))
			return res
		
		def invert(self):
			res = ImMatrix((
				-1, 0, 0, 0, 1,
				0, -1, 0, 0, 1,
				0, 0, -1, 0, 1,
				0, 0, 0,  1, 0,
				0, 0, 0,  0, 1
			))
			return res
		
		def brightness(self, b):
			res = ImMatrix((
				1, 0, 0, 0, b,
				0, 1, 0, 0, b,
				0, 0, 1, 0, b,
				0, 0, 0, 1, 0,
				0, 0, 0, 0, 1
			))
			return res
		
		def contrast(self, c):
			return self.brightness(-0.5) * self.tint(c, c, c) * self.brightness(0.5)
		
		def opacity(self, o):
			res = ImMatrix((
				1, 0, 0, 0, 0,
				0, 1, 0, 0, 0,
				0, 0, 1, 0, 0,
				0, 0, 0, o, 0,
				0, 0, 0, 0, 1
			))
			return res
		
		def colorize(self, black_color, white_color):
		    r0, g0, b0, _a0 = renpy.easy.color(black_color)
		    r1, g1, b1, _a1 = renpy.easy.color(white_color)
		    
		    r0 /= 255.0
		    g0 /= 255.0
		    b0 /= 255.0
		    r1 /= 255.0
		    g1 /= 255.0
		    b1 /= 255.0
		    
			res = ImMatrix((
				(r1-r0), 0, 0, 0, r0,
				0, (g1-g0), 0, 0, g0,
				0, 0, (b1-b0), 0, b0,
				0, 0, 0, 1, 0,
				0, 0, 0, 0, 1
			))
			return res
	
	
	
	
	class Im:
		matrix = ImMatrix()
		
		
		def MatrixColor(self, image, matrix):
			return 'MatrixColor (' + image + ') (' + str(matrix) + ')'
		
		def Grayscale(self, image, desat=(0.2126, 0.7152, 0.0722)):
			return self.MatrixColor(image, self.matrix.saturation(0.0, desat))
		
		def Sepia(self, image, tint=(1.0, 0.94, 0.76), desat=(0.2126, 0.7152, 0.0722)):
			return self.MatrixColor(image, self.matrix.saturation(0.0, desat) * self.matrix.tint(tint[0], tint[1], tint[2]))
		
		
		def ReColor(self, image, r, g, b, a):
			return 'ReColor (' + image + ') (' + str(r) + ' ' + str(g) + ' ' + str(b) + ' ' + str(a) + ')'
		
		def Color(self, image, color):
			r, g, b, a = renpy.easy.color(color)
			return self.ReColor(image, r, g, b, a)
		
		def Alpha(self, image, alpha):
			return self.ReColor(image, 255, 255, 255, int(alpha * 255))
		
		
		def Flip(self, image, horizontal = False, vertical = False):
			return 'Flip (' + image + ') ' + str(bool(horizontal)) + ' ' + str(bool(vertical))
		
		
				
		def Composite(self, *args):
			if (len(args) % 2) == 0:
				out_msg('im.Composite', 'Ожидалось нечётное количество аргументов')
				return ''
			
			size = str(int(args[0][0])) + ' ' + str(int(args[0][1]))
			res = 'Composite (' + size + ')'
			
			for i in xrange(1, len(args) - 1, 2):
				pos = str(int(args[i][0])) + ' ' + str(int(args[i][1]))
				img = str(args[i + 1])
				
				res += ' (' + pos + ') (' + img + ')'
			return res
		
		def Scale(self, image, w, h):
			return 'Scale (' + image + ') ' + str(int(w)) + ' ' + str(int(h))
		
		def FactorScale(self, image, k):
			return 'FactorScale (' + image + ') ' + str(k)
		
		def Crop(self, image, rect):
			rect = map(lambda f: int(f), rect)
			rect = '(' + str(rect[0]) + ' ' + str(rect[1]) + ' ' + str(rect[2]) + ' ' + str(rect[3]) + ')'
			return 'Crop (' + image + ') ' + rect
		
		
		def Rect(self, color, width = 1, height = 1):
			r, g, b, a = renpy.easy.color(color)
			matrix = im.matrix.invert() * im.matrix.tint(r / 255.0, g / 255.0, b / 255.0, a / 255.0)
			return self.Scale(im.MatrixColor('images/bg/black.jpg', matrix), width, height)
	
	


init -1000 python:
	im = Im()
