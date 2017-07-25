init -1000 python:
	
	sprites_list = []
	
	sprite_can_update = True
	
	screen = Sprite([], [], [], None)
	screen.new_data.xsize, screen.new_data.ysize = 1.0, 1.0
	screen.new_data.real_xsize, screen.new_data.real_ysize = 1.0, 1.0
	
	
	
	def sprites_effects_ended():
		for spr in sprites_list + [screen]:
			if spr.effect is not None:
				return False
		return True
	
	def sprites_effects_to_end():
		for spr in sprites_list + [screen]:
			spr.remove_effect()
	
	
	
	def set_scene(params, show_at):
		global sprites_list
		
		if len(params):
			scene = show_sprite(params, show_at, True)
			
			if screen.effect or scene.effect:
				if screen.effect:
					screen.effect.sprite = False
				else:
					scene.effect.sprite = False
				
				for spr in sprites_list:
					spr.hiding = True
			else:
				sprites_list = []
			sprites_list.insert(0, scene)
		else:
			sprites_list = []
	
	
	def show_sprite(params, show_at, hide_all = False):
		global sprites_list
		
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
		
		if d['behind'] is not None and hide_all:
			d['behind'] = None
		
		
		effect = eval(d['with']) if d['with'] else None
		
		old_sprite = None
		index = 0
		for i in sprites_list:
			if i.as_name == d['as']:
				if not hide_all or not effect:
					sprites_list = sprites_list[0:index] + sprites_list[index+1:]
				if effect:
					old_sprite = i
				break
			index += 1
		
		
		image_name = ' '.join(params)
		decl_at = get_image(image_name)
		
		if d['at'] is not None:
			at = eval(d['at']).actions
		else:
			if old_sprite:
				old_at_sprite_animation = old_sprite.new_animations[1] # [decl_at, --> at <--, show_at]
				at = old_at_sprite_animation.actions
			else:
				at = [] if show_at else center.actions
		
		spr = Sprite(decl_at, at, show_at, effect, old_sprite if not hide_all else False)
		spr.as_name = d['as']
		spr.call_str = params_str
		
		
		if not hide_all:
			if d['behind'] is None:
				sprites_list.insert(index, spr)
			else:
				index = 0
				for i in sprites_list:
					if i.as_name == d['behind']:
						break
					index += 1
				else:
					out_msg('show_sprite', 'Спрайт с именем <' + d['behind'] + '> не найден')
				sprites_list.insert(index, spr)
		
		return spr
	
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
					sprites_list[i] = Sprite([], [], [], effect, spr)
					sprites_list[i].hiding = True
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
					if data.image:
						tmp = Object()
						tmp.image  =  data.image
						tmp.pos    = (data.real_xpos, data.real_ypos)
						tmp.anchor = (data.real_xanchor, data.real_yanchor)
						tmp.xysize = (data.real_xsize, data.real_ysize)
						tmp.crop   = (data.xcrop, data.ycrop, data.xsizecrop, data.ysizecrop)
						tmp.alpha  =  data.real_alpha
						sprites_images.append(tmp)
	
	null:
		pos (screen.new_data.xpos, screen.new_data.ypos)
		anchor (screen.new_data.xanchor, screen.new_data.yanchor)
		xysize (screen.new_data.real_ysize, screen.new_data.real_xsize)
		
		for tmp in sprites_images:
			image tmp.image:
				pos     tmp.pos
				anchor  tmp.anchor
				xysize  tmp.xysize
				crop    tmp.crop
				alpha   tmp.alpha

