init -1000 python:
	narrator = Character('')
	extend = Character(None)
	th = Character('', text_prefix='~', text_postfix='~')
	
	def add_default_character(alias, name, color = '#FFFFFF'):
		g = globals()
		g[alias] = Character(name, color = color)
	
    add_default_character('mt_voice', 'Голос', '#00EA32')
    add_default_character('odn', 'Одногруппник')
    add_default_character('message', 'Сообщение')
    add_default_character('voice', 'Голос', '#808080')
    add_default_character('dy', 'Голос из динамика', '#FF0000')
    add_default_character('lk', 'Луркмор-кун')
    add_default_character('pi', 'Пионер', '#FF0000')
    add_default_character('all', 'Пионеры', '#FF0000')
    add_default_character('kids', 'Малышня', '#FFFF00')
    add_default_character('bush', 'Голос', '#808080')
    add_default_character('voices', 'Голоса', '#808080')
	
	
	
	me = Character('Семён', color = '#D1D0A4')
	dreamgirl = Character('Девочка', color = '#FFFFFF')
	
	dv = Character('Алиса', color = '#DF9501')
	un = Character('Лена', color = '#B956FF')
	sl = Character('Славя', color = '#F3F301')
	mi = Character('Мику', color = '#00DEFF')
	us = Character('Ульяна', color = '#FF3200')
	
	mz = Character('Женя', color = '#4983F9')
	mt = Character('Ольга Дмитриевна', color = '#00EA32')
	cs = Character('Виола', color = '#9B9CEF')
	el = Character('Электроник', color = '#F3F301')
	sh = Character('Шурик', color = '#F3F301')
	uv = Character('Юля', color = '#FFFF00')
