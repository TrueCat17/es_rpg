init -1000 python:
	Style = Object # class
	
	
	style = Object()
	def get_styles():
		return style.get_props()
	def get_style_props(name):
		return style.__dict__[name].get_props()
	
	
	
	# Важно!
	# В style.default обязательно
	# 	использовать отдельно x- и y- свойства,
	# 	не использовать *align
	
	style.default = Style()
	style.default.xpos = 0
	style.default.ypos = 0
	style.default.xanchor = 0
	style.default.yanchor = 0
	style.default.xsize = 1
	style.default.ysize = 1
	
	style.window = Style(style.default)
	
	style.vbox = Style(style.default)
	style.vbox.xsize = 0
	style.vbox.ysize = 0
	
	style.hbox = Style(style.vbox)
	
	style.text = Style(style.default)
	style.text.xsize = -1
	style.text.ysize = -1
	style.text.size = 30
	style.text.color = '#FFFFFF'
	style.text.font = 'Arial'
	style.text.bold = False
	style.text.italic = False
	style.text.underline = False
	style.text.text_align = 'left' 				# left | center | right
	
	style.textbutton = Style(style.text)
	style.textbutton.text_align = 'center'		# left | center | right
	style.textbutton.xsize = 0.1
	style.textbutton.ysize = 0.05
	style.textbutton.background = 'images/es2d/gui/std/btn/usual.png'
	style.textbutton.hover_background = ''
	
	style.button = Style(style.default)
	style.button.xsize = 0.1
	style.button.ysize = 0.05
	style.button.background = 'images/es2d/gui/std/btn/usual.png'
	style.button.hover_background = ''
	
	style.image = Style(style.default)
	style.image.xsize = 0.25
	style.image.ysize = 0.25
	
	style.imagemap = Style(style.default)
	style.imagemap.ground = ''
	style.imagemap.hover_background = ''
