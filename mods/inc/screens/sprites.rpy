init -1000 python:
	
	sprites_show_list = []
	sprites_hide_list = []
	
	sprite_can_update = True
	
	screen = Sprite([], [], [], None)
	screen.new.xsize, screen.new.ysize = 1.0, 1.0
	screen.new.real_xsize, screen.new.real_ysize = 1.0, 1.0
	
	
	
	def sprites_effects_ended():
		for spr in sprites_show_list + sprites_hide_list + [screen]:
			if spr.with_at is not None:
				return False
		return True
	
	def sprites_effects_to_end():
		for spr in sprites_show_list + sprites_hide_list + [screen]:
			spr.remove_with_at()
	
	
	
	def set_scene(params, show_at):
		global sprites_show_list, sprites_hide_list
		
		if len(params):
			scene = add_sprite_to_showlist(params, show_at, True)
			if screen.with_at or scene.with_at:
				if screen.with_at:
					screen.with_at.sprite = False
				else:
					scene.with_at.sprite = False
				sprites_hide_list += sprites_show_list
			else:
				sprites_hide_list = []
			sprites_show_list = [scene]
		else:
			sprites_show_list = []
			sprites_hide_list = []
	
	
	def add_sprite_to_showlist(params, show_at, hide_all = False):
		global sprites_show_list
		
		if len(params) == 0:
			out_msg('add_sprite_to_showlist', 'Список params пуст')
			return
		
		params_str = ' '.join(params)
		
		pnames = ('at', 'with', 'behind', 'as')
		
		d = dict()
		while len(params) > 2 and (params[-2] in pnames):
			pname, pvalue = params[-2], params[-1]
			params = params[0:-2]
			if d.has_key(pname):
				out_msg('add_sprite_to_showlist', 'Параметр <' + pname + '> указан несколько раз')
			else:
				d[pname] = pvalue
		if len(params) == 0:
			out_msg('add_sprite_to_showlist', 'Список params не содержит имени спрайта' + '\n' + params_str)
			return
		
		for pname in pnames:
			if not d.has_key(pname):
				d[pname] = None
		if d['as'] is None:
			d['as'] = params[0]
		
		if d['behind'] is not None and hide_all:
			d['behind'] = None
		
		old_sprite = None
		index = 0
		for i in sprites_show_list:
			if i.as_name == d['as']:
				if not hide_all:
					sprites_show_list = sprites_show_list[0:index] + sprites_show_list[index+1:]
				old_sprite = i
				break
			index += 1
		
		
		image_name = ' '.join(params)
		decl_at = get_image(image_name)
		
		if d['at'] is not None:
			at = eval(d['at']).actions
		else:
			at = [] if show_at else center.actions
		
		with_at = eval(d['with']) if d['with'] is not None else None
		
		spr = Sprite(decl_at, at, show_at, with_at, old_sprite if not hide_all else False)
		spr.old_at = bool(old_sprite) and (at == old_sprite.at.actions)
		spr.as_name = d['as']
		spr.call_str = params_str
		
		
		if not hide_all:
			if d['behind'] is None:
				sprites_show_list.insert(index, spr)
			else:
				index = 0
				for i in sprites_show_list:
					if i.as_name == d['behind']:
						break
					index += 1
				else:
					out_msg('add_sprite_to_showlist', 'Спрайт с именем <' + d['behind'] + '> не найден')
				sprites_show_list.insert(index, spr)
		
		return spr
	
	def add_sprite_to_hidelist(params):
		global sprites_show_list
		
		if len(params) == 0:
			out_msg('add_sprite_to_hidelist', 'Список params пуст')
			return
		
		with_at = None
		if len(params) == 3:
			if params[1] != 'with':
				out_msg('add_sprite_to_hidelist', 'Вторым параметром ожидалось with')
				return
			with_at = eval(params[2])
		elif len(params) != 1:
			out_msg('add_sprite_to_hidelist', 'Ожидалось 1 или 3 параметра: name ["with" effect]\n' + 'Получено: ' + str(params))
			return
		
		name = params[0]
		
		for i in xrange(len(sprites_show_list)):
			spr = sprites_show_list[i]
			if spr.as_name == name:
				sprites_show_list = sprites_show_list[0:i] + sprites_show_list[i+1:]
				
				if with_at is not None:
					new_spr = Sprite([], [], [], with_at, spr)
					sprites_hide_list.append(new_spr)
				break
		else:
			out_msg('add_sprite_to_hidelist', 'Спрайт с именем <' + name + '> не найден')

screen sprites:
	zorder -3
	
	python:
		sprites_images = []
		
		for spr in sprites_show_list + sprites_hide_list + [screen]:
			spr.update()
			
			for high_level_trans in spr.new_old_ordered:
				for trans in high_level_trans.get_all_transforms():
					if trans.image is not None:
						tmp = Object()
						tmp.image  =  trans.image
						tmp.pos    = (trans.real_xpos, trans.real_ypos)
						tmp.anchor = (trans.real_xanchor, trans.real_yanchor)
						tmp.xysize = (trans.real_xsize, trans.real_ysize)
						tmp.crop   = (trans.xcrop, trans.ycrop, trans.xsizecrop, trans.ysizecrop)
						tmp.alpha  =  trans.real_alpha
						sprites_images.append(tmp)
	
	null:
		pos (screen.new.xpos, screen.new.ypos)
		anchor (screen.new.xanchor, screen.new.yanchor)
		xysize (screen.new.real_ysize, screen.new.real_xsize)
		
		for tmp in sprites_images:
			image tmp.image:
				pos     tmp.pos
				anchor  tmp.anchor
				xysize  tmp.xysize
				crop    tmp.crop
				alpha   tmp.alpha

