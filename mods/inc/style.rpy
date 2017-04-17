init -1001 python:
	Style = Object # class
	
	
	# Важно!
	# В style.* обязательно:
	# 	использовать отдельно x- и y- свойства,
	# 	не использовать *align
	
	style = Object()
	
	style.key = Style()
	style.key.first_delay = 0.333
	style.key.delay = 0.01
	
	style.default = Style()
	style.default.xpos = 0
	style.default.ypos = 0
	style.default.xanchor = 0
	style.default.yanchor = 0
	style.default.xsize = 1.0
	style.default.ysize = 1.0
	style.default.spacing = 0
	style.default.crop = (0, 0, 1.0, 1.0)
	style.default.alpha = 1
	
	style.screen = Style(style.default)
	style.screen.modal = False
	style.screen.zorder = 0
	
	style.vbox = Style(style.default)
	style.vbox.xsize = 0
	style.vbox.ysize = 0
	
	style.hbox = Style(style.vbox)
	style.null = Style(style.vbox)
	
	style.text = Style(style.default)
	style.text.xsize = -1
	style.text.ysize = -1
	style.text.size = 20
	style.text.color = '#FFFFFF'
	style.text.font = 'Calibri'
	style.text.text_align = 'left' 				# left | center | right
	style.text.text_valign = 'top' 				# top  | center |  down
# Пока без поддержки:
#	style.text.bold = False
#	style.text.italic = False
#	style.text.underline = False
	
	style.textbutton = Style(style.text)
	style.textbutton.text_align = 'center'		# left | center | right
	style.textbutton.text_valign = 'center'		# top  | center |  down
	style.textbutton.xsize = 175
	style.textbutton.ysize = 25
	style.textbutton.size = 15
	style.textbutton.ground = 'images/es2d/gui/std/btn/usual.png'
	style.textbutton.hover = ''
	
	style.button = Style(style.default)
	style.button.xsize = 175
	style.button.ysize = 25
	style.button.ground = 'images/es2d/gui/std/btn/usual.png'
	style.button.hover = ''
	
	style.image = Style(style.default)
	style.image.xsize = -1
	style.image.ysize = -1
	
	style.imagemap = Style(style.default)
	style.imagemap.ground = ''
	style.imagemap.hover = ''
