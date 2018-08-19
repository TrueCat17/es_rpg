init -1000 python:
	narrator = Character('')
	th = Character('', text_prefix='~', text_postfix='~')
	extend = Character(None)
	
	odn     = Character('Одногруппник',      color = '#FFFFFF')
	lk      = Character('Луркмор-кун',       color = '#FFFFFF')
	message = Character('Сообщение',         color = '#FFFFFF')
	dy      = Character('Голос из динамика', color = '#FF0000')
	bush    = Character('Голос',             color = '#808080')
	voice   = Character('Голос',             color = '#808080')
	voices  = Character('Голоса',            color = '#808080')
	all     = Character('Пионеры',           color = '#FF0000')
	kids    = Character('Малышня',           color = '#FFFF00')
	
	mt_voice = Character('Голос',  color = '#00EE33')
	pi       = Character('Пионер', color = '#FF0000')
	
	me        = Character('Семён', color = '#EEEEAA')
	dreamgirl = Character('...',   color = '#FFFFFF')
	
	dv = Character('Алиса',            unknown_name = 'Пионерка',         color = '#DD9900')
	un = Character('Лена',             unknown_name = 'Пионерка',         color = '#BB55FF')
	sl = Character('Славя',            unknown_name = 'Пионерка',         color = '#EEEE00')
	mi = Character('Мику',             unknown_name = 'Пионерка',         color = '#00DDFF')
	us = Character('Ульяна',           unknown_name = 'Пионерка',         color = '#FF3300')
	
	cs = Character('Виола',            unknown_name = 'Медсестра',        color = '#9999EE')
	mz = Character('Женя',             unknown_name = 'Пионерка',         color = '#4488FF')
	mt = Character('Ольга Дмитриевна', unknown_name = 'Вожатая',          color = '#00EE33')
	sh = Character('Шурик',            unknown_name = 'Пионер',           color = '#EEEE00')
	el = Character('Электроник',       unknown_name = 'Пионер',           color = '#EEEE00')
	uv = Character('Юля',              unknown_name = 'Странная девочка', color = '#FFFF00')
	
	pm = Character('Пионер',   color = '#FFFFFF')
	pf = Character('Пионерка', color = '#FFFFFF')
	
	
	
	rpg_characters = ('me ' +
					  'dv un sl mi us ' +
					  'cs mz mt sh el uv ' +
					  'pm pf').split(' ')
	
	g = globals()
	for name in rpg_characters:
		g[name].make_rpg('images/characters/', name, 'pioneer')
		g['lp_' + name] = 0
	
	
