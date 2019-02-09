init -1000 python:
	odn     = Character('Одногруппник',      color = 0xFFFFFF)
	lk      = Character('Луркмор-кун',       color = 0xFFFFFF)
	message = Character('Сообщение',         color = 0xFFFFFF)
	dy      = Character('Голос из динамика', color = 0xFF0000)
	bush    = Character('Голос',             color = 0x808080)
	voice   = Character('Голос',             color = 0x808080)
	voices  = Character('Голоса',            color = 0x808080)
	all     = Character('Пионеры',           color = 0xFF0000)
	kids    = Character('Малышня',           color = 0xFFFF00)
	
	mt_voice = Character('Голос',  color = 0x00EE33)
	pi       = Character('Пионер', color = 0xFF0000)
	
	me        = Character('Семён', color = 0xEEEEAA)
	dreamgirl = Character('...',   color = 0xFFFFFF)
	
	dv = Character('Алиса',            unknown_name = 'Пионерка',         color = 0xDD9900)
	un = Character('Лена',             unknown_name = 'Пионерка',         color = 0xBB55FF)
	sl = Character('Славя',            unknown_name = 'Пионерка',         color = 0xEEEE00)
	mi = Character('Мику',             unknown_name = 'Пионерка',         color = 0x00DDFF)
	us = Character('Ульяна',           unknown_name = 'Пионерка',         color = 0xFF3300)
	
	cs = Character('Виола',            unknown_name = 'Медсестра',        color = 0x9999EE)
	mz = Character('Женя',             unknown_name = 'Пионерка',         color = 0x4488FF)
	mt = Character('Ольга Дмитриевна', unknown_name = 'Вожатая',          color = 0x00EE33)
	sh = Character('Шурик',            unknown_name = 'Пионер',           color = 0xEEEE00)
	el = Character('Электроник',       unknown_name = 'Пионер',           color = 0xEEEE00)
	uv = Character('Юля',              unknown_name = 'Странная девочка', color = 0xFFFF00)
	
	pm = Character('Пионер',   color = 0xFFFFFF)
	pf = Character('Пионерка', color = 0xFFFFFF)
	
	
	
	rpg_characters = ('me ' +
					  'dv un sl mi us ' +
					  'cs mz mt sh el uv ' +
					  'pm pf').split(' ')
	
	g = globals()
	for name in rpg_characters:
		g[name].make_rpg('images/characters/', name, 'pioneer')
		g['lp_' + name] = 0
	
	
