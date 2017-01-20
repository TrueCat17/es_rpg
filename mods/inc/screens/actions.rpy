init -1001 python:
	def exec_funcs(funcs):
		if isinstance(funcs, list) or isinstance(funcs, tuple):
			for func in funcs:
				if func is not None:
					func()
		else: # if get only 1 func
			if funcs is not None:
				funcs()
	
	
	def If(cond, true, false):
		return true if cond else false
	
	class Function(Object):
		def __init__(self, func, *args, **kwargs):
			Object.__init__(self)
			self.func, self.args, self.kwargs = func, args, kwargs
		def __call__(self):
			apply(self.func, self.args, self.kwargs)
	
	class AddVariable(Object):
		def __init__(self, var_name, d):
			Object.__init__(self)
			self.var_name, self.d = var_name, d
		def __call__(self):
			g = globals()
			g[self.var_name] += self.d
	
	class SetVariable(Object):
		def __init__(self, var_name, value):
			Object.__init__(self)
			self.var_name, self.value = var_name, value
		def __call__(self):
			g = globals()
			g[self.var_name] = self.value
	
	def Play(file_name, channel):
		return Function(renpy.play, file_name, channel)
	def Stop(channel):
		return Function(renpy.stop, channel)
	
	
	
	# Return -> call_screen.rpy
