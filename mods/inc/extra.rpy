init -1001 python:
	es2d_gui = 'images/es2d/gui/'
	
	alphabet = list(map(chr, xrange(ord('a'), ord('z') + 1)))
	numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)



init -10000 python:
	def ceil(n):
		res = int(n)
		if res != n and n > 0:
			res += 1
		return res
	
	
	def out_msg(msg, err = ''):
		_out_msg(msg, err)
	
	def get_image(name):
		code = get_image_code(name)
		res = eval(code)
		return res
	
	
	def get_traceback(tb):
		import traceback
		l = traceback.format_tb(tb)
		return '\n\t'.join(l)
	
	persistent_updates = False
	class Object:
		def __init__(self, obj = None, **kwords):
			self.in_persistent = False
			
			if obj is not None:
				for k in obj.__dict__.keys():
					self.__dict__[k] = obj.__dict__[k]
			for k in kwords.keys():
				self.__dict__[k] = kwords[k];
		
		
		def __getattr__(self, attr):
			if (not persistent_updates) and (not self.__dict__.has_key(attr)):
				return None
			return self.__dict__[attr]
		
		def __setattr__(self, attr, value):
			self.__dict__[attr] = value
			
			if isinstance(value, Object):
				value.in_persistent = True
			
			if self.in_persistent:
				global persistent_need_save
				persistent_need_save = True
			
		
		def __delattr__(self, attr):
			del self.__dict__[attr]
			if self.in_persistent:
				global persistent_need_save
				persistent_need_save = True
		
		
		def has_attr(self, attr):
			return self.__dict__.has_key(attr)
		
		
		def get_props(self):
			keys = self.__dict__.keys()
			keys.remove('in_persistent')
			
			return ' '.join(keys)
		
		
		# for pickle
		def __getstate__(self):
			return self.__dict__
		def __setstate__(self, new_dict):
			self.__dict__.update(new_dict)
	
