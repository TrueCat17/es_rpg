init -1000 python:
	
	sprites_list = []
	
	screen = Sprite([], [], [], None)
	screen.new_data.xsize, screen.new_data.ysize = 1.0, 1.0
	screen.new_data.real_xsize, screen.new_data.real_ysize = 1.0, 1.0
	screen.call_str = 'screen'
	
	scene = None
	
	
	def sprites_effects_ended():
		for spr in sprites_list + [screen]:
			if spr.effect is not None:
				return False
		return True
	
	def sprites_effects_to_end():
		for spr in sprites_list + [screen]:
			spr.remove_effect()
		remove_hiding_sprites()
	
	def remove_hiding_sprites():
		for spr in list(sprites_list):
			if spr.hiding:
				sprites_list.remove(spr)
			else:
				if spr.effect is not None:
					spr.effect.for_not_hiding()
	
	
	def set_scene(params, show_at):
		global sprites_list, scene
		
		if len(params):
			show_sprite(params, show_at, True)
			
			if screen.effect or scene.effect:
				for spr in sprites_list:	
					if spr is not scene:
						spr.old_data, spr.new_data = spr.new_data, None
						spr.hiding = True
			else:
				sprites_list = [scene]
		else:
			sprites_list = []
			scene = None
	
	
	def show_sprite(params, show_at, is_scene = False):
		global scene
		
		if not has_screen('sprites'):
			show_screen('sprites')
		
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
				out_msg('show_sprite', 'Параметр <' + pname + '> указан несколько раз')
			else:
				d[pname] = pvalue
		if len(params) == 0:
			out_msg('show_sprite', 'Список params не содержит имени спрайта' + '\n' + params_str)
			return
		
		for pname in pnames:
			if not d.has_key(pname):
				d[pname] = None
		if d['as'] is None:
			d['as'] = params[0]
		
		
		effect = eval(d['with']) if d['with'] else None
		
		old_sprite = None
		if is_scene:
			index = len(sprites_list)
		else:
			index = 0
			while index < len(sprites_list):
				spr = sprites_list[index]
				if spr.as_name == d['as']:
					old_sprite = spr
					sprites_list.remove(spr)
					break
				index += 1
		
		
		image_name = ' '.join(params)
		decl_at = get_image(image_name)
		
		if d['at'] is not None:
			at = eval(d['at']).actions
		else:
			if old_sprite and (old_sprite.new_data or old_sprite.old_data):
				at = (old_sprite.new_data or old_sprite.old_data).at.actions or center.actions
			else:
				at = [] if show_at else center.actions
		
		spr = Sprite(decl_at, at, show_at, old_sprite if effect else None)
		spr.as_name = d['as']
		spr.call_str = params_str
		if is_scene or old_sprite is scene:
			scene = spr
		spr.set_effect(effect)
		
		
		if d['behind'] is not None:
			index = 0
			while index < len(sprites_list):
				if sprites_list[index].as_name == d['behind']:
					break
				index += 1
			else:
				out_msg('show_sprite', 'Спрайт с именем <' + d['behind'] + '> не найден')
		
		if scene in sprites_list:
			index = max(index, sprites_list.index(scene) + 1)
		
		sprites_list.insert(index, spr)
	
	def hide_sprite(params):
		if len(params) == 0:
			out_msg('hide_sprite', 'Список params пуст')
			return
		
		global sprites_list
		
		name = params[0]
		
		effect = None
		if len(params) == 3:
			if params[1] != 'with':
				out_msg('hide_sprite', 'Вторым параметром ожидалось with')
				return
			effect = eval(params[2])
		elif len(params) != 1:
			out_msg('hide_sprite', 'Ожидалось 1 или 3 параметра: name ["with" effect]\n' + 'Получено: <' + str(params) + '>')
			return
		
		for i in xrange(len(sprites_list)):
			spr = sprites_list[i]
			if spr.as_name == name:
				if effect is not None:
					spr.old_data, spr.new_data = spr.new_data, None
					
					spr.set_effect(effect)
					spr.hiding = True
				else:
					sprites_list = sprites_list[0:i] + sprites_list[i+1:]
				break
		else:
			out_msg('hide_sprite', 'Спрайт с именем <' + name + '> не найден')

screen sprites:
	zorder -3
	
	python:
		sprites_images = []
		
		for spr in sprites_list + [screen]:
			spr.update()
			
			for spr_data in spr.data_list:
				for data in spr_data.get_all_data():
					tmp_image = data.res_image if data.res_image is not None else data.image
					if tmp_image:
						tmp = Object()
						tmp.image  =  tmp_image
						tmp.pos    = (data.real_xpos,    data.real_ypos)
						tmp.anchor = (data.real_xanchor, data.real_yanchor)
						tmp.size   = (data.real_xsize,   data.real_ysize)
						tmp.crop   = (data.xcrop, data.ycrop, data.xsizecrop, data.ysizecrop)
						tmp.alpha  =  data.real_alpha
						tmp.rotate =  data.real_rotate
						sprites_images.append(tmp)
	
	null:
		pos    (screen.new_data.xpos,       screen.new_data.ypos)
		anchor (screen.new_data.xanchor,    screen.new_data.yanchor)
		size   (screen.new_data.real_ysize, screen.new_data.real_xsize)
		
		for tmp in sprites_images:
			image tmp.image:
				pos    tmp.pos
				anchor tmp.anchor
				size   tmp.size
				crop   tmp.crop
				alpha  tmp.alpha
				rotate tmp.rotate

