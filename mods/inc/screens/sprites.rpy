init -1000 python:
	spr_background = None
	
	sprite_list = []
	def set_scene(params, child_params):
		global sprite_list, spr_background
		sprite_list = []
		
		spr_background = None
		if len(params):
			add_sprite_to_showlist(params, child_params)
			if len(sprite_list):
				spr_background = sprite_list[0]
	
	
	def add_sprite_to_showlist(params, child_params):
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
		
		new = False
		spr = None
		for i in sprite_list:
			if i.as_name == d['as']:
				if d['behind'] is None:
					spr = i
				else:
					sprite_list.remove(i)
				break
		
		if spr is None:
			new = True
			spr = Object()
		
		spr.image_name = ' '.join(params)
		if not new and d['at'] is not None:
			spr.params = eval(d['at'])
		
		if new:
			spr.as_name = d['as']
			spr.params = center if d['at'] is None else eval(d['at'])
			
			if d['behind'] is None:
				sprite_list.append(spr)
			else:
				index = 0
				for i in sprite_list:
					index += 1
					if i.as_name == d['behind']:
						index -= 1
						break
				else:
					out_msg('add_sprite_to_showlist', 'Спрайт с именем <' + d['behind'] + '> не найден')
				sprite_list.insert(index, spr)
	
	def remove_sprite_from_showlist(name):
		global sprite_list
		
		for i in xrange(len(sprite_list)):
			spr = sprite_list[i]
			if spr.as_name == name:
				sprite_list = sprite_list[0:i] + sprite_list[i + 1:]
				break
		else:
			out_msg('remove_sprite_from_showlist', 'Спрайт с именем <' + name + '> не найден')

screen sprites:
	zorder -3
	
	if spr_background:
		image get_image(spr_background.image_name):
			xysize (1.0, 1.0)
	
	$ spr_start = 1 if len(sprite_list) > 0 and sprite_list[0] is spr_background else 0
	for spr in sprite_list[spr_start:]:
		image get_image(spr.image_name):
			pos (spr.params.xpos, spr.params.ypos)
			anchor (spr.params.xanchor, spr.params.yanchor)

