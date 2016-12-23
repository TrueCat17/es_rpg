init -1002 python:
	es2d_gui = 'images/es2d/gui/'
	
	alphabet = list(map(chr, xrange(ord('a'), ord('z') + 1)))
	numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)



init -10000 python:
	def ceil(n):
		res = int(n)
		if res != n and n > 0:
			res += 1
		return res
	
	def get_image(name):
		code = get_image_code(name)
		res = eval(code)
		return res
	
	
	def get_traceback(tb):
		import traceback
		l = traceback.format_tb(tb)
		return '\n\t'.join(l)
	
	class Object:
		def __init__(self, obj = None, **kwords):
			if obj is not None:
				for k in obj.__dict__.keys():
					self.__dict__[k] = obj.__dict__[k]
			for k in kwords.keys():
				self.__dict__[k] = kwords[k];
		
		def __getattr__(self, attr):
			return self.__dict__[attr]
		
		def __setattr__(self, attr, value):
			self.__dict__[attr] = value
		
		def __delattr__(self, attr):
			del self.__dict__[attr]
		
		
		def get_props(self):
			return ' '.join(self.__dict__.keys())
	
	
