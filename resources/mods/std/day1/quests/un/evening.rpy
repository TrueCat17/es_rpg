init 20 python:
	un_evening__name = 'Унесённые вечером'
	
	def day1_un_read_book(character, state):
		actions = character.get_actions()
		
		if state == 'start':
			actions.interruptable = False
			
			character.move_to_place(['square', 'bench_left_pos-2', (+20, -10)])
			return 'moving'
		
		if state == 'moving':
			if character.ended_move_waiting():
				bench = get_location_objects('square', 'bench_left_pos-2', 'bench_left')[0]
				if not character.sit_down(bench): # on failure: try again later
					return 'moving'
				character.start_animation('book_right', -1)
				return 'reading'
			return 'moving'
		
		if state == 'reading':
			if (clock.hours, clock.minutes) >= (21, 50):
				return 'end'
			return 'reading'
		
		if state == 'end':
			character.remove_animation()
			character.stand_up()
			actions.sit_start_time = get_game_time()
			return 'end'
	
	def day1_un_start_read_book():
		if un.get_actions():
			un.get_actions().start(day1_un_read_book)
	signals.add('clock-1-20:47:00', day1_un_start_read_book, times = 1)
	
	
	def un_evening__check_start():
		if un.get_actions().cur_action != day1_un_read_book or un.get_actions().state != 'reading':
			return
		if rpg_event != 'sit_down':
			return
		if 'un_evening' in was:
			return
		if get_dist(un.x, un.y, me.x, me.y) > 100:
			return
		
		quest_start('un_evening')
		return True


label day1__square__before_genda:
	if rpg_event != 'enter':
		return
	if un.get_actions().cur_action != day1_un_read_book or un.get_actions().state != 'reading':
		return
	
	if 'un_evening_prompt' in was or 'un_evening' in was:
		return
	$ was.append('un_evening_prompt')
	
	$ set_rpg_control(False)
	
	"На площади ещё оставались несколько групп пионеров, но все они, похоже, о чём-то воодушевлённо беседовали или шли по своим делам."
	th "Даже если бы я был смелее, я не стал бы вмешиваться в их разговоры. Похоже, делать тут нечего."
	"Я уже собрался уходить, как..."
	
	$ me.rotate_to(un)
	pause 0.5
	$ cam_to(un, align = (0.2, 0.7))
	
	extend " заметил одиноко сидящую девушку на лавочке."
	th "Эй, да она же из моего отряда! Лена, вроде?"
	th "Хм-м... может, познакомиться поближе? Вроде и пересекались пару раз сегодня, да как-то это было... скомкано."
	
	window hide
	$ cam_to(me, align = 'center')
	$ set_rpg_control(True)

label day1__square__unknown:
	$ un_evening__check_start()


label un_evening__start:
	$ was.append('un_evening')
	
	$ set_rpg_control(False)
	
	"Я аккуратно сел на другую сторону скамейки, но остался незамеченным. По крайней мере, на минуту, потому как через это время Лена вдруг ойкнула и посмотрела на меня."
	un "!!!"
	me "Извини... не хотел тебя напугать."
	"Она смущённо улыбнулась."
	un "Н-ничего."
	me "Мы как-то и не познакомились сегодня нормально... Меня Семён зовут."
	un "Лена..."
	"На этом наш \"диалог\" закончился. Даже эти, казалось бы, стандартные вопросы, дались мне с трудом. Поэтому, чтобы прервать неловкое молчание, я задал не менее тривиальный вопрос."
	me "А ты это... что читаешь?"
	"Лена молча показала обложку книги. Это были \"Унесённые ветром\"."
	me "И как... интересно?"
	"Вообще, я впервые слышал об этой книге, так что подумал, что этот вопрос не будет лишним."
	un "Угу..."
	"Лена замолчала примерно на полминуты, после чего будто опомнилась и добавила:"
	un "Она романтическая. Может... поэтому и интересно."
	"Снова наступило молчание."
	"..."
	"Ситуация становилась неприятной. Да, мы вроде обменялись всего парой фраз, но в воздухе витала тягучая атмосфера."
	th "Я, конечно, никуда не спешу, но сидеть на похоронах веселее, чем в такой тишине. Нужно либо аккуратно ретироваться, либо попытаться её разговорить."
	
	menu:
		"Уйти":
			$ me.stand_up()
			$ me.rotate_to(un)
			"Я встал со скамейки и обратился к Лене."
			me "Ладно, не буду больше мешать чтению. Приятного вечера."
			"На последних словах я попытался улыбнуться."
			un "М... ладно."
			me "Пока?"
			un "Пока."
			$ me.set_direction(to_forward)
			th "Наконец... последние слова вообще пришлось вытягивать. Не думал, что вообще когда-нибудь в жизни придётся таким заниматься."
		"Попытаться разговорить":
			me "А тебе нравится здесь?"
			"Лена задумчиво посмотрела на звёздное небо и сказала:"
			un "Да, наверное... Здесь тихо, спокойно."
			me "Ага. Я тоже так думаю."
			me "И люди здесь... под стать месту."
			"Я посмотрел на Лену. Почувствовав мой взгляд, она на несколько секунд оторвала свой взгляд от книги, посмотрела на меня и снова уткнулась в книгу."
			"Меня это немного рассмешило."
			"Лена опять сделала паузу, после чего сказала уже более серьёзным тоном:"
			un "Не стриги всех под одну гребёнку. Все люди совершенно разные."
			"После этих слов я даже стал чувствовать себя неловко."
			me "Ну... наверно, да."
			"..."
			me "Поздно уже..."
			un "Ага..."
			me "Я пойду, пожалуй."
			$ me.stand_up()
			pause 0.5
			$ me.set_direction(to_forward)
			"Лена просто молчала. Однако, когда я повернулся, я услышал тихое:"
			un "{size=-8}Спокойной ночи.{/size}"
			me "И тебе."
			$ un.rp += 1
	
	window hide
	$ set_rpg_control(True)
	
	$ set_timeout(un.get_actions().stop, 10)
	$ quest_end('un_evening')
