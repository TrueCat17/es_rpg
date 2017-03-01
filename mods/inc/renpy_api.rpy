init -1001 python:
	
	pause_end = 0
	def pause(sec):
		global pause_end
		pause_end = time.time() + sec
	
	
	class Music:
		def register_channel(self, name, mixer, loop):
			_register_channel(name, mixer, loop)
		
		def play(self, file_names, channel, **kwargs):
			fadein = kwargs.get('fadein', 0)
			file_name = file_names if isinstance(file_names, str) else file_names[0]
			_play(channel + ' ' + file_name + ' fadein ' + fadein)
		def stop(self, channel, **kwargs):
			fadeout = kwargs.get('fadeout', 0)
			_stop(channel + ' fadeout ' + fadeout)
		
		def set_volume(self, vol, channel):
			_set_volume(vol, channel)
		def set_mixer_volume(self, vol, mixer):
			_set_mixer_volume(vol, mixer)
	
	
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
		music = Music()
		easy = Easy()
		
		def __init__(self):
			self.random = random
			
			if persistent.has_attr('config'):
				self.config = persistent.config
			else:
				self.config = Object()
				persistent.config = self.config
		
		def pause(self, sec):
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
		
		def play(self, file_names, channel, **kwargs):
			self.music.play(file_name, channel, **kwargs)
		def stop(self, channel, **kwargs):
			self.music.stop(channel, **kwargs)
		
		def has_label(self, label):
			return _has_label(label)
		
		def call_screen(self, screen_name, ret_name, **kwargs):
			global menu_item_choosed
			menu_item_choosed = False
			
			push_ret_names(screen_name, ret_name)
			show_screen(screen_name)

init -999 python:
	renpy = Renpy()
	
	def volume(vol, channel):
		renpy.music.set_volume(vol, channel = channel)
