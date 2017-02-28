init -1001 python:
	es2d_gui = 'images/es2d/gui/'
	
	alphabet = tuple(map(chr, xrange(ord('a'), ord('z') + 1))) # a-z
	numbers = tuple(xrange(10)) # 0-9



init -1100000000 python:
	def get_traceback(tb):
		import traceback
		l = traceback.format_tb(tb)
		return ''.join(l)


init -10000 python:
	def ceil(n):
		res = int(n)
		if res != n and n > 0:
			res += 1
		return res
	
	def get_dist(x1, y1, x2, y2):
		return ((x1-x2)**2 + (y1-y2)**2) ** 0.5
	
	
	def get_from_hard_config(param, ret_type):
		res = _get_from_hard_config(str(param))
		return ret_type(res)
	
	def get_mods():
		mods_str = _get_mods()
		mods_dict = eval(mods_str)
		return mods_dict
	
	def out_msg(msg, err = ''):
		_out_msg(msg, err)
	
	def get_image(name):
		code = get_image_code(name)
		
		res = None
		try:
			res = eval(code)
		except:
			res = im.Scale('images/bg/black.jpg', 256, 256)
		return res
	
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
			if self.__dict__.has_key(attr) or persistent_updates:
				return self.__dict__[attr]
			return None
		
		def __setattr__(self, attr, value):
			self.__dict__[attr] = value
			
			if self.in_persistent:
				if isinstance(value, Object):
					value.in_persistent = True
					
				global persistent_need_save
				persistent_need_save = True
			
		
		def __delattr__(self, attr):
			del self.__dict__[attr]
			if self.in_persistent:
				global persistent_need_save
				persistent_need_save = True
		
		
		def has_attr(self, attr):
			return self.__dict__.has_key(attr)
		
		def __nonzero__(self):
			return True
		def __str__(self):
			return '<Object ' + str(type(self)) + '>'
		def __repr__(self):
			return str(self)
		
		def get_props(self):
			keys = self.__dict__.keys()
			keys.remove('in_persistent')
			
			return ' '.join(keys)
		
		
		# for pickle
		def __getstate__(self):
			return self.__dict__
		def __setstate__(self, new_dict):
			self.__dict__.update(new_dict)
	
