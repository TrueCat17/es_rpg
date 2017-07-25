init -1000 python:
	menu_item_choosed = True
	call_screen_stack = []
	
	def push_ret_names(screen_name, ret_name):
		call_screen_stack.append((screen_name, ret_name))
	
	def pop_ret_names():
		global call_screen_stack
		
		res = call_screen_stack[-1]
		call_screen_stack = call_screen_stack[0:-1]
		return res
	
	
	class Return(Object):
		def __init__(self, value):
			Object.__init__(self)
			self.value = value
		def __call__(self):
			screen_name, ret_name = pop_ret_names()
			g = globals()
			g[ret_name] = self.value
			hide_screen(screen_name)
			g['menu_item_choosed'] = True
