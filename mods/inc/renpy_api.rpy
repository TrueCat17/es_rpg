init -1003 python:
	def pause(sec):
		sleep(int(sec * 1000), False)
	
	
	class Music:
		def register_channel(self, name, mixer, loop):
			register_channel(name, mixer, loop)
	
	
	class Easy:
		def color(self, c):
			if isinstance(c, tuple) or isinstance(c, list):
				r, g, b = c[0], c[1], c[2]
				if len(c) == 4:
					a = c[4]
				else:
					a = 255
			
			elif isinstance(c, basestring):
				if c[0] == '#':
					c = c[1:]
				elif c[0:2] == '0x':
					c = c[2:]
				
				if len(c) == 6:
					r = int(c[0]+c[1], 16)
					g = int(c[2]+c[3], 16)
					b = int(c[4]+c[5], 16)
					a = 255
				elif len(c) == 8:
					r = int(c[0]+c[1], 16)
					g = int(c[2]+c[3], 16)
					b = int(c[4]+c[5], 16)
					a = int(c[6]+c[7], 16)
				elif len(c) == 3:
					r = int(c[0], 16) * 0x11
					g = int(c[1], 16) * 0x11
					b = int(c[2], 16) * 0x11
					a = 255
				elif len(c) == 4:
					r = int(c[0], 16) * 0x11
					g = int(c[1], 16) * 0x11
					b = int(c[2], 16) * 0x11
					a = int(c[3], 16) * 0x11
				else:
					out_msg('renpy.ease.color', 'Неожидаемый размер строки (ожидалось: 3, 4, 6 или 8; получено: ' + str(len(c)) + ', c = "' + c + '")')
					r = g = b = 0
					a = 255
			else:
				out_msg('renpy.ease.color', 'Неожидаемый тип аргумента (ожидалось: list, tuple или basestring; получено: ' + str(type(c)) + ')')
				r = g = b = 0
				a = 255
			
			return r, g, b, a
	
	
	class Renpy:
		config = Object()
		music = Music()
		easy = Easy()
		
		def __init__(self):
			self.random = random
		
		def pause(self, sec):
			out_msg('renpy.pause', 'Использовать renpy.pause не рекомендуется, см. resources/mods/ReadMe.txt')
			pause(sec)
		
		def say(self, who, what):
			if who is None:
				who = narrator
			
			if isinstance(who, str):
				g = globals()
				if g.has_key(who):
					who = g[who]
				else:
					out_msg('renpy.say', 'Персонаж <' + who + '> не существует')
					return
			who(what)
		
		def call_screen(self, screen_name, ret_name, **kwargs):
			global read
			read = False
			
			push_ret_names(screen_name, ret_name)
			show_screen(screen_name)
	
	renpy = Renpy()
