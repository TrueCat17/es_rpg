init 2 python:
	card_down = "images/misc/down.png"
	card_up   = "images/misc/up.png"
	
	
	n_cards    = 7
	n_xchanges = 2
	n_cycles   = 3
	
	types  = ["2ch", "ussr", "utan", "uvao"]
	
	cards_bg = im.Sepia("images/bg/int_dining_hall_day.jpg")
	card_text_bg = im.rect('#444')
	
	
	def update_card_sizes():
		global card_width, card_height, card_indent, arrow_size, small_text_size, big_text_size
		
		card_width  = 210 * get_stage_width()  / 1920
		card_height = 315 * get_stage_height() / 1080
		card_indent = 15 * get_stage_width() / 1920
		
		arrow_size = 50 * get_stage_width() / 1920
		
		small_text_size = max(20 * get_stage_width() / 1920, 15)
		big_text_size   = 30 * get_stage_width() / 1920
	
	
	def get_img(img):
		return "images/cards/" + img + ".png"
	
	card_none = (0, "none")
	
	card_img = {}
	card_img["cover"] = get_img("cover")
	card_img[card_none] = im.rect('#0000')
	
	for i in xrange(1, 14):
		for j in types:
			name = str(i) + '_' + j
			card_img[(i, j)] = get_img(name)
	
	def generate_cards(dialogs, rival_name, name):
		update_card_sizes()
		
		global game_interuptions, rival, cards_game_name
		game_interuptions = dialogs
		rival = get_rival(rival_name)
		cards_game_name = name
		
		global cycles_left, changes_left, cards_state, result_status
		cycles_left = n_cycles
		changes_left = n_xchanges
		cards_state = "init"
		result_status = "in_progress"
		
		cset = []
		while len(cset) < 2 * n_cards:
			name = (random.randint(1, 13), random.choice(types))
			if name not in cset:
				cset.append(name)
		
		global cards_my, cards_rival
		cards_rival = []
		cards_my = []
		for i in xrange(n_cards):
			cards_rival.append(Card(cset[i], False))
			cards_my.append(Card(cset[n_cards + i], True))
		
		cards_rival[0].name = card_none
		cards_my[0].name = card_none
		
		deal_card = "sound/sfx/cardgame/deal_card_" + str(random.randint(1, 4)) + ".ogg"
		renpy.music.play(deal_card, channel="sound")
	
	def rival_cards_show():
		for card in cards_rival:
			card.visible = True
			card.update_view()
	def rival_cards_hide():
		for card in cards_rival:
			card.visible = False
			card.update_view()
	def my_cards_show():
		for card in cards_my:
			card.visible = True
			card.update_view()
	def my_cards_hide():
		for card in cards_my:
			card.visible = False
			card.update_view()


screen cards:
	zorder -4
	
	image cards_bg:
		size (1.0, 1.0)
	
	$ update_card_sizes()
	
	for card in itertools.chain(cards_rival, cards_my):
		$ card.update_pos()
		
		null:
			pos  (card.x, card.y)
			
			button:
				size (card_width, card_height)
				ground card.ground
				hover  card.hover
				mouse  card.mouse
				action card.action
			
			if card.interesting:
				image (card_down if card.is_my else card_up):
					xalign 0.5
					ypos (-arrow_size if card.is_my else card_height)
					size  (arrow_size, arrow_size)
	
	python:
		if      "me" in cards_state:
			card_step = 'Твой'
		elif "rival" in cards_state:
			card_step = 'Чужой'
		else:
			card_step = '---'
		
		if   "defend" in cards_state:
			card_phase = "Защита"
		elif "select" in cards_state:
			card_phase = "Захват"
		elif    "get" in cards_state:
			card_phase = "Вытягивание"
		else:
			card_phase = "Итоги"
		
		if result_status == 'win':
			cards_result = 'Победа'
		elif result_status == 'draw':
			cards_result = 'Ничья'
		elif result_status == 'fail':
			cards_result = 'FAIL'
	
	vbox:
		align (0.97, 0.1)
		
		image rival_avatar size (card_width, card_width)
		
		null ysize small_text_size
		
		image card_text_bg size (card_width, small_text_size + 5) xalign 0.5:
			text "Соперник:" text_size small_text_size align (0.5, 0.5)
		image card_text_bg size (card_width, big_text_size + 5) xalign 0.5:
			text cards_game_name text_size big_text_size align (0.5, 0.5)
	
	vbox:
		align (0.97, 0.97)
		
		image card_text_bg size (card_width, small_text_size + 5):
			text "Чей ход:" text_size small_text_size align (0.5, 0.5)
		image card_text_bg size (card_width, big_text_size + 5):
			text card_step text_size big_text_size align (0.5, 0.5)
		
		null ysize small_text_size
		
		image card_text_bg size (card_width, small_text_size + 5):
			text "Фаза игры:" text_size small_text_size align (0.5, 0.5)
		image card_text_bg size (card_width, big_text_size + 5):
			text card_phase text_size big_text_size align (0.5, 0.5)
			if cards_state in ("me_defend_1", "me_defend_2"):
				textbutton "X":
					text_size small_text_size
					size (big_text_size, big_text_size)
					align (1.0, 0.5)
					action SetVariable('answer', 'end_of_turn')
		
		null ysize small_text_size
		
		image card_text_bg size (card_width, small_text_size + 5):
			text "Кругов оставалось:" text_size small_text_size align (0.5, 0.5)
		image card_text_bg size (card_width, big_text_size + 5):
			text cycles_left text_size big_text_size align (0.5, 0.5)
		
		null ysize small_text_size
		
		image card_text_bg size (card_width, small_text_size + 5):
			text "Обменов оставалось:" text_size small_text_size align (0.5, 0.5)
		image card_text_bg size (card_width, big_text_size + 5):
			text (changes_left if changes_left else "---") text_size big_text_size align (0.5, 0.5)
	
	if result_status != 'in_progress':
		textbutton cards_result:
			align (0.5, 0.5)
			size (300, 40)
			text_size 72
			action [HideScreen('cards'), check_dialogues]


init python:
	def move_buttons(setk, k, setj, j):
		for card in itertools.chain(cards_rival, cards_my):
			card.hot = False
			card.interesting = False
		
		a, b = setk[k], setj[j]
		
		a.hot = b.hot = True
		a.is_my, b.is_my = b.is_my, a.is_my
		a.index, b.index = b.index, a.index
		a.move()
		b.move()
		a.update_view()
		b.update_view()
		
		setk[k], setj[j] = b, a
	
	def xchange_cards():
		cards_my[my_card].visible = False
		cards_rival[rival_card].visible = True
		move_buttons(cards_my, my_card, cards_rival, rival_card)
		
		take_card = "sound/sfx/cardgame/take_card_" + str(random.randint(1, 3)) + ".ogg"
		renpy.music.play(take_card, channel="sound")
	
	def card_value(x):
		if x.name[0] == 1:
			return 14
		return x.name[0]
	
	def sort_cards():
		cards_rival.sort(cmp, card_value)
		cards_my.sort(cmp, card_value)
	
	def check_dialogues():
		position = (cycles_left, cards_state, "call")
		if position in game_interuptions:
			renpy.call(game_interuptions[position])
			del game_interuptions[position]
		position = (cycles_left, cards_state, "jump")
		if position in game_interuptions:
			renpy.jump(game_interuptions[position])
	
	def what_category(cardset):
		ans = []
		summ = 0
		for i in xrange(n_cards):
			cardset[i].interesting = False
		for length in [4, 3, 2]:
			for i in xrange(n_cards-length+1):
				if cardset[i].interesting:
					continue
				val = card_value(cardset[i])
				for j in xrange(i+1, i+length):
					if card_value(cardset[j]) != val:
						break
				else:
					for j in xrange(i, i+length):
						cardset[j].interesting = True
					ans.append([length, val])
					summ += length
		if ans:
			return summ, ans
		
		cardset[-1].interesting = True
		return 1, [[1, card_value(cardset[-1])]]
	
	def cmpset(a, b):
		if b[0] != a[0]:
			return b[0] - a[0]
		return b[1] - a[1]
	
	def compare_sets(result_my, gr_my, result_rival, gr_rival):
		if result_my > result_rival:
			return 'win'
		if result_my < result_rival:
			return 'fail'
		
		if len(gr_my) < len(gr_rival):
			return 'win'
		if len(gr_my) > len(gr_rival):
			return 'fail'
		
		for i in xrange(len(gr_my)):
			if gr_my[i][0] > gr_rival[i][0]:
				return 'win'
			if gr_my[i][0] < gr_rival[i][0]:
				return 'fail'
			
			if gr_my[i][1] > gr_rival[i][1]:
				return 'win'
			if gr_my[i][1] < gr_rival[i][1]:
				return 'fail'
		
		return 'draw'
	
	def count_score():
		result_my, gr_my = what_category(cards_my)
		result_rival, gr_rival = what_category(cards_rival)
		
		gr_my.sort(cmpset)
		gr_rival.sort(cmpset)
		
		return compare_sets(result_my, gr_my, result_rival, gr_rival)

label cards_gameloop:
	scene
	show screen cards
	
	while True:
		python:
			for card in itertools.chain(cards_rival, cards_my):
				card.update_view()
		
		if cards_state == "init":
			$ new_state = "rival_select"
		
		elif cards_state == "rival_select":
			python:
				check_dialogues()
				my_card = rival.pick_my_card()
			if my_card is None:
				$ answer = None
				while answer is None:
					pause 0.1
				$ is_my, my_card = answer
			
			python:
				for i in xrange(n_cards):
					cards_my[i].interesting = False
					cards_rival[i].interesting = False					 
				cards_my[my_card].interesting = True
				
				if rival.allow_to_defend():
					new_state = "me_defend_1"
				else:
					new_state = "rival_get"
		
		elif cards_state == "me_defend_1":
			python:
				renpy.music.play("sound/sfx/cardgame/choose_card_2.ogg", channel="sound")
				check_dialogues()
				answer = None
			while answer is None:
				pause 0.1
			
			python:
				if answer == "end_of_turn":
					new_state = "rival_get"
				else:
					is_my, index = answer
					prev_answer = index
					new_state = "me_defend_2"
		
		elif cards_state == "me_defend_2":
			python:
				renpy.music.play("sound/sfx/cardgame/choose_card_1.ogg", channel="sound")
				check_dialogues()
				answer = None
			while answer is None:
				pause 0.1
			
			python:
				if answer == "end_of_turn":
					new_state = "rival_get"
				else:
					is_my, index = answer
					if prev_answer == index:
						new_state = "me_defend_1"
					else:
						move_buttons(cards_my, prev_answer, cards_my, index)
						changes_left -= 1
						if changes_left == 0:
							new_state = "rival_get"
						else:
							new_state = "rival_select"
		
		elif cards_state == "rival_get":
			python:
				if changes_left == 0:
					my_card = rival.pick_my_card_last()
				for card in itertools.chain(cards_rival, cards_my):
					card.interesting = False
				cards_my[my_card].interesting = True
				
				check_dialogues()
				
				for i in xrange(n_cards):
					if cards_rival[i].name == card_none:
						rival_card = i
				xchange_cards()
				changes_left = n_xchanges
				rival.allow_to_take()
				new_state = "me_select"
		
		elif cards_state == "me_select":
			python:
				renpy.music.play("sound/sfx/cardgame/choose_card_1.ogg", channel="sound")
				check_dialogues()
				answer = None
			while answer is None:
				pause 0.1
			
			python:
				is_my, index = answer
				for card in itertools.chain(cards_rival, cards_my):
					card.interesting = False
				rival_card = index
				cards_rival[index].interesting = True
				new_state = "rival_defend"
		
		elif cards_state == "rival_defend":
			python:
				renpy.music.play("sound/sfx/cardgame/choose_card_1.ogg", channel="sound")
				check_dialogues()
				
				if changes_left == 0 or not rival.want_to_defend():
					changes_left = 0
					new_state = "me_get"
				else:
					changes_left -= 1
					i, j = rival.what_to_xchange()
					move_buttons(cards_rival, i, cards_rival, j)
					new_state = "me_select"
		
		elif cards_state == "me_get":
			python:
				check_dialogues()
				
				for i in xrange(n_cards):
					if cards_my[i].name == card_none:
						my_card = i
				xchange_cards()
				
				cycles_left -= 1
				if cycles_left != 0:
					changes_left = n_xchanges
					new_state = "rival_select"
				else:
					new_state = "results"
		
		elif cards_state == "results":
			python:
				sort_cards()
				rival_cards_show()
				my_cards_show()
				cards_state = result_status = count_score()
			while True:
				pause 0.1
		
		$ cards_state = new_state

