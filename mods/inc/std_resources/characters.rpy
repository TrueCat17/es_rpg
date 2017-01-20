init -1000 python:
    narrator = Character('')
    th = Character('', text_prefix='~', text_postfix='~')
    extend = Character(None)
    
    mt_voice = Character('Голос',       color = '#00EA32')
    odn = Character('Одногруппник',     color = '#FFFFFF')
    message = Character('Сообщение',    color = '#FFFFFF')
    voice = Character('Голос',          color = '#808080')
    dy = Character('Голос из динамика', color = '#FF0000')
    lk = Character('Луркмор-кун',       color = '#FFFFFF')
    pi = Character('Пионер',            color = '#FF0000')
    all = Character('Пионеры',          color = '#FF0000')
    kids = Character('Малышня',         color = '#FFFF00')
    bush = Character('Голос',           color = '#808080')
    voices = Character('Голоса',        color = '#808080')
    
    
    me = Character('Семён',             color = '#D1D0A4')
    dreamgirl = Character('...',        color = '#FFFFFF')
    
    dv = Character('Алиса',             unknown_name = 'Пионерка',          color = '#DF9501')
    un = Character('Лена',              unknown_name = 'Пионерка',          color = '#B956FF')
    sl = Character('Славя',             unknown_name = 'Пионерка',          color = '#F3F301')
    mi = Character('Мику',              unknown_name = 'Пионерка',          color = '#00DEFF')
    us = Character('Ульяна',            unknown_name = 'Пионерка',          color = '#FF3200')
    
    mz = Character('Женя',              unknown_name = 'Пионерка',          color = '#4983F9')
    mt = Character('Ольга Дмитриевна',  unknown_name = 'Вожатая',           color = '#00EA32')
    cs = Character('Виола',             unknown_name = 'Медсестра',         color = '#9B9CEF')
    el = Character('Электроник',        unknown_name = 'Пионер',            color = '#F3F301')
    sh = Character('Шурик',             unknown_name = 'Пионер',            color = '#F3F301')
    uv = Character('Юля',               unknown_name = 'Странная девочка',  color = '#FFFF00')
    
    pm = Character('Пионер', color = '#FFFFFF')
    pf = Character('Пионерка', color = '#FFFFFF')
    
    
    
    
    
	rpg_characters = ('me ' +
					  'sl un us dv mi mt cs mz el sh uv ' +
					  'pm pf').split(' ')
	
	g = globals()
	for name in rpg_characters:
		g[name].make_rpg('images/es2d/characters/' + name + '_', 'pi')
