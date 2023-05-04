# signals (params for all: character, topic):
#  before-conversation
#  after-conversation
#  conversation - only for topics in character.spec_topics

init -1 python:
	def conversation__get_bg():
		sw, sh = get_stage_size()
		cache = conversation__get_bg.__dict__
		key = (sw, sh)
		if key in cache:
			return cache[key]
		
		r, g, b, a = renpy.easy.color(conversation.edge_color)
		
		path = os.path.dirname(get_filename(0))
		corner = im.recolor(os.path.join(path, 'corner.png'), r, g, b)
		hline = im.recolor(os.path.join(path, 'line.png'), r, g, b)
		vline = im.rotozoom(hline, 90)
		
		r, g, b, a = renpy.easy.color(conversation.bg_color)
		corner_bg = im.recolor(os.path.join(path, 'corner_bg.png'), r, g, b, a)
		
		w = int(get_absolute(conversation.xsize, sw))
		h = int(get_absolute(conversation.ysize, sh))
		
		cw, ch = get_image_size(corner)
		segment_size, segment_wide = get_image_size(hline)
		
		w -= cw
		h -= ch
		w -= w % segment_size
		h -= h % segment_size
		xcount = w // segment_size
		ycount = h // segment_size
		
		args = [(cw * 2 + w, ch * 2 + h)]
		
		args.extend([(0,      0),      corner])
		args.extend([(0,      ch + h), im.flip(corner, False, True)])
		args.extend([(cw + w, ch + h), im.flip(corner, True,  True)])
		args.extend([(cw + w, 0),      im.flip(corner, True, False)])
		
		args.extend([(0,      0),      corner_bg])
		args.extend([(0,      ch + h), im.flip(corner_bg, False, True)])
		args.extend([(cw + w, ch + h), im.flip(corner_bg, True,  True)])
		args.extend([(cw + w, 0),      im.flip(corner_bg, True, False)])
		
		args.extend([(cw, 0), im.rect(conversation.bg_color, w, ch)])
		args.extend([(0, ch), im.rect(conversation.bg_color, cw * 2 + w, h)])
		args.extend([(cw, ch + h), im.rect(conversation.bg_color, w, ch)])
		
		for line in (0, 1):
			for i in range(xcount):
				args.extend([(cw + segment_size * i, (ch * 2 + h - segment_wide) * line), hline])
		for line in (0, 1):
			for i in range(ycount):
				args.extend([((cw * 2 + w - segment_wide) * line, ch + segment_size * i), vline])
		
		cache[key] = im.composite(*args)
		return cache[key]
	
	def conversation__show(character):
		set_rpg_control(False)
		me.rotate_to(character)
		character.rotate_to(me)
		conversation.was_auto = character.get_auto()
		character.set_auto(False)
		conversation.spec_topics = character.spec_topics or []
		
		conversation.character = character
		conversation.show_time = get_game_time()
		conversation.hide_time = None
		
		show_screen('conversation')
	
	def conversation__end(topic):
		conversation.topic = topic
		conversation.hide_time = get_game_time()
		renpy.call('conversation__processing')
	
	
	def conversation__get_need(character, topic):
		res = 40 + character.conversation_count[topic] * 10 - me.topic_knowledges[topic] * 10 - character.rp * 2
		
		if topic in character.liked_topics:
			res -= 10
		if topic in character.disliked_topics:
			res += 10
		
		if dirty_points > 33:
			res += dirty_points - 33
		
		if food_points < 67:
			res += 67 - dirty_points
		
		if water_points < 67:
			res += 67 - water_points
		
		return res
	
	def conversation__get_end():
		character = conversation.character
		topic = conversation.topic
		
		rnd = random.randint(-50, 50)
		need = conversation.get_need(character, topic)
		
		if rnd >= need:
			result = 'good'
			diff = 1
		else:
			result = 'bad'
			diff = -1
		if topic in character.liked_topics or topic in character.disliked_topics:
			diff *= 2
		character.rp += diff
		
		all_ends = []
		for tag in list(character.conversation_tags or []) + ['common']:
			ends = conversation[result + '_ends'][tag]
			if ends:
				all_ends.extend(ends)
		
		return random.choice(all_ends)
	
	
	def conversation__check():
		if not conversation.enable: return
		if not get_rpg_control(): return
		
		min_dist = conversation.max_dist + 1
		near_character = None
		for character in characters:
			if character.location is not cur_location: continue
			if character is me: continue
			
			dist = get_dist(me.x, me.y, character.x, character.y)
			if dist < min_dist:
				min_dist = dist
				near_character = character
		
		if min_dist <= conversation.max_dist:
			if near_character.conversation_tags is None:
				renpy.call('conversation__no')
			elif near_character.today_conversations == conversation.count_in_day and not near_character.spec_topics:
				renpy.call('conversation__too_many')
			else:
				conversation.show(near_character)
	
	config.keymap['conversation'] = ['C']
	config.underlay.append(renpy.Keymap(
		conversation = conversation__check,
	))
	
	
	build_object('conversation')
	conversation.enable = True
	
	conversation.xsize = 0.9
	conversation.ysize = 150
	
	conversation.xalign = 0.5
	conversation.yalign = 0.9
	
	conversation.max_dist = std_sit_dist
	conversation.count_in_day = 2
	conversation.one_conversation_time = 60 * 15
	
	conversation.edge_color = '#F92'
	conversation.bg_color = '#0006'
	
	conversation.btn_ground_color = '#48E'
	conversation.btn_hover_color  = '#5AF'
	conversation.btn_text_font = 'FixEx3'
	conversation.btn_text_color = 0xFFFFFF
	
	conversation.topics_xcount = 4
	conversation.topics_ycount = 3
	conversation.btn_xspacing = 20
	conversation.btn_yspacing = 15
	conversation.btn_edge_indent = 40
	
	conversation.appearance_time = 0.4
	conversation.disappearance_time = 0.4
	
	conversation.topics = [
		 'Спорт', 'Погода', 'Книги', 'Рисование',
		 'Музыка', 'Игры', 'Наука', 'Лагерь',
		 'Природа', 'Работа', 'Шутки',
	]
	conversation.spec_topics = []


label conversation__no:
	$ set_rpg_control(False)
	"Как-то неловко просто так заводить разговор с незнакомым человеком."
	window hide
	$ set_rpg_control(True)

label conversation__too_many:
	$ set_rpg_control(False)
	"Не хочу быть слишком навязчивым. Мы уже достаточно говорили сегодня."
	window hide
	$ set_rpg_control(True)


label conversation__processing:
	show bg black with Dissolve(conversation.appearance_time)
	hide bg with Dissolve(conversation.disappearance_time)
	
	$ signals.send('before-conversation', conversation.character, conversation.topic)
	
	if conversation.topic in conversation.spec_topics:
		$ signals.send('conversation', conversation.character, conversation.topic)
	else:
		python:
			conversation.character.today_conversations += 1
			end = conversation.get_end()
			if type(end) is str:
				end = [end]
			i = 0
		while i < len(end):
			python:
				item = end[i]
				i += 1
				if type(item) is str:
					character, text = conversation.character, item
				else:
					character, text = item
				renpy.say(character, text)
		$ clock.add(conversation.one_conversation_time)
	
	$ signals.send('after-conversation', conversation.character, conversation.topic)
	
	$ conversation.character.set_auto(conversation.was_auto)
	window hide
	$ set_rpg_control(True)


screen conversation:
	python:
		conversation.alpha = min((get_game_time() - conversation.show_time) / conversation.appearance_time, 1)
		conversation.hiding = conversation.hide_time is not None
		if conversation.hiding:
			conversation.alpha = 1 - min((get_game_time() - conversation.hide_time) / conversation.disappearance_time, 1)
			if conversation.alpha == 0:
				hide_screen('conversation')
	alpha conversation.alpha
	
	$ conversation.image = conversation.get_bg()
	$ conversation.w, conversation.h = get_image_size(conversation.image)
	image conversation.image:
		size  (conversation.w, conversation.h)
		align (conversation.xalign, conversation.yalign)
		
		$ conversation.btn_xsize = get_stage_width() // 8
		$ conversation.btn_ysize = in_bounds(get_stage_height() // 30, 18, 28)
		$ conversation.text_size = conversation.btn_ysize - 2
		
		$ conversation.ground = im.round_rect(conversation.btn_ground_color, conversation.btn_xsize, conversation.btn_ysize, 4)
		$ conversation.hover  = im.round_rect(conversation.btn_hover_color,  conversation.btn_xsize, conversation.btn_ysize, 4)
		
		vbox:
			xpos conversation.btn_edge_indent
			yalign 0.5
			alpha 1 if conversation.character.today_conversations < conversation.count_in_day else 0
			spacing conversation.btn_yspacing
			
			for y in range(conversation.topics_ycount):
				hbox:
					spacing conversation.btn_xspacing
					
					for x in range(conversation.topics_xcount):
						$ index = y * conversation.topics_xcount + x
						if index >= len(conversation.topics):
							break
						
						textbutton _(conversation.topics[index]):
							size (conversation.btn_xsize, conversation.btn_ysize)
							ground conversation.ground
							hover  conversation.hover if not conversation.hiding else conversation.ground
							font  conversation.btn_text_font
							color conversation.btn_text_color
							text_size conversation.text_size
							mouse  not conversation.hiding
							action conversation.end(conversation.topics[index]) if not conversation.hiding else None
		
		$ conversation.btn_xsize = conversation.btn_xsize * 3 // 2
		$ conversation.ground = im.round_rect(conversation.btn_ground_color, conversation.btn_xsize, conversation.btn_ysize, 4)
		$ conversation.hover  = im.round_rect(conversation.btn_hover_color,  conversation.btn_xsize, conversation.btn_ysize, 4)
		null:
			xpos conversation.w - conversation.btn_edge_indent
			xanchor 1.0
			ysize (conversation.btn_ysize + conversation.btn_yspacing) * conversation.topics_ycount - conversation.btn_yspacing
			yalign 0.5
			
			vbox:
				spacing conversation.btn_yspacing
				
				for spec_topic in conversation.spec_topics:
					textbutton _(spec_topic):
						size (conversation.btn_xsize, conversation.btn_ysize)
						ground conversation.ground
						hover  conversation.hover if not conversation.hiding else conversation.ground
						font  conversation.btn_text_font
						color conversation.btn_text_color
						text_size conversation.text_size
						mouse  not conversation.hiding
						action conversation.end(spec_topic) if not conversation.hiding else None
