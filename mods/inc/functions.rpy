init -1002 python:
	
	def out_msg(msg, err = ''):
		_out_msg(msg, err)
	
	def reload_names():
		pass
	
	def exec_funcs(funcs):
		if isinstance(funcs, list) or isinstance(funcs, tuple):
			for func in funcs:
				if func is not None:
					func()
		else:
			if funcs is not None:
				funcs() # get only 1 func
	
	def If(cond, true, false):
		return true if cond else false
	
	class Function:
		def __init__(self, func, *args, **kwargs):
			self.func, self.args, self.kwargs = func, args, kwargs
		def __call__(self):
			apply(self.func, self.args, self.kwargs)
	
	class Add:
		def __init__(self, var_name, d):
			self.var_name, self.d = var_name, d
		def __call__(self):
			g = globals()
			g[self.var_name] += self.d
	
	class Set:
		def __init__(self, var_name, value):
			self.var_name, self.value = var_name, value
		def __call__(self):
			g = globals()
			g[self.var_name] = self.value
		
	
	
	class Character:
		def __init__(self, name, **kwargs):
			self.name = name
			self.name_prefix = kwargs.get('name_prefix', '')
			self.name_postfix = kwargs.get('name_postfix', '')
			self.color = kwargs.get('color', 0)
			
			self.text_prefix = kwargs.get('text_prefix', '')
			self.text_postfix = kwargs.get('text_postfix', '')
			self.text_color = kwargs.get('text_color', 0xFFFF00)
		
		def __call__(self, text):
			show_text(	self.name, self.name_prefix, self.name_postfix, self.color,
						text, self.text_prefix, self.text_postfix, self.text_color)
	
	
	
	def set_name(who, name):
		g = globals()
		if g.has_key(who):
			g[who].name = name
		else:
			out_msg('set_name', 'Персонаж <' + who + '> не найден')
	
	def make_names_unknown():
        set_name('mt_voice', "Голос")
        set_name('odn', "Одногруппник")
        set_name('message', "Сообщение")
        set_name('voice', "Голос")
        set_name('me', "Семён")
        set_name('dy', "Голос из динамика")
        set_name('lk', "Луркмор-кун")
        set_name('pi', "Пионер")
        set_name('all', "Пионеры")
        set_name('kids', "Малышня")
        set_name('dreamgirl', "...")
        set_name('bush', "Голос")
        set_name('voices', "Голоса")
        set_name('el', "Пионер")
        set_name('un', "Пионерка")
        set_name('dv', "Пионерка")
        set_name('sl', "Пионерка")
        set_name('us', "Пионерка")
        set_name('mt', "Вожатая")
        set_name('cs', "Медсестра")
        set_name('mz', "Пионерка")
        set_name('mi', "Пионерка")
        set_name('uv', "Странная девочка")
        set_name('sh', "Пионер")
    
    def make_names_known():
        set_name('mt_voice', "Голос")
        set_name('odn', "Одногруппник")
        set_name('message', "Сообщение")
        set_name('voice', "Голос")
        set_name('me', "Семён")
        set_name('dy', "Голос из динамика")
        set_name('lk', "Луркмор-кун")
        set_name('pi', "Пионер")
        set_name('all', "Пионеры")
        set_name('kids', "Малышня")
        set_name('dreamgirl', "...")
        set_name('bush', "Голос")
        set_name('voices', "Голоса")
        set_name('el', "Электроник")
        set_name('un', "Лена")
        set_name('dv', "Алиса")
        set_name('sl', "Славя")
        set_name('us', "Ульяна")
        set_name('mt', "Ольга Дмитриевна")
        set_name('cs', "Виола")
        set_name('mz', "Женя")
        set_name('mi', "Мику")
        set_name('uv', "Юля")
        set_name('sh', "Шурик")
    
    def meet(who, name):
        set_name(who, name)
    
    def new_chapter(num, name):
    	pass
    
    
    def set_map_object(obj_name, x, y, alias = None):
    	if alias is None:
    		alias = obj_name
    	_set_map_object(obj_name, x, y, alias)
    
    def move_to_place(person_name, place_name, run, acceleration = "no"):
    	accelerations = ["no", "start", "end", "all"]
    	if acceleration not in accelerations:
    		out_msg("move_to_place", "acceleration '" + acceleration + "' not in " + str(accelerations))
    	
    	start = acceleration in ["start", "all"]
    	end = acceleration in ["end", "all"]
    	
    	_move_to_place(person_name, place_name, run, start, end)
