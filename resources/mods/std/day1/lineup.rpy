init python:
	def day1_mt_lineup_ending(character, state):
		actions = character.get_actions()
		
		if state == 'start':
			character.move_to_place(['admin', 'closed-1'])
			actions.block = ['to_friend']
			return 'moving'
		
		if state == 'moving':
			if not character.ended_move_waiting():
				return 'moving'
			character.set_direction(to_back)
			return 'waiting'
		
		if state == 'waiting': # state changing directly in scenario
			return 'waiting'
		
		if state == 'moving_without_waiting':
			if not character.ended_move_waiting():
				return 'moving_without_waiting'
			return 'continue'
		
		if state == 'continue':
			hide_character(mt)
			actions.waiting_end_time = get_game_time() + 15
			return 'in_admin_building'
		
		if state == 'in_admin_building':
			if actions.waiting_end_time > get_game_time():
				return 'in_admin_building'
			return 'end'
		
		if state == 'end':
			show_character(mt, 'closed-1', 'admin')
			actions.waiting_end_time = None
			actions.block = []
			return 'end'


label day1__lineup_conversation:
	$ was.append('lineup')
	$ set_rpg_control(False)
	
	if clock.minutes <= 31:
		python:
			while clock.minutes < 30:
				clock.add(10)
		mt "Итак, вроде все собрались."
	elif clock.minutes <= 33:
		mt "Семён, опаздываешь!"
		mt "Быстрее вставай в строй."
	else:
		mt "Семён, ну ты где там ходишь?"
		mt "Линейка уже почти закончена!"
	
	python:
		was_meet = {
			'sl': get_name('sl') == 'Славя',
			'el_sh': get_name('el') == 'Электроник' and get_name('sh') == 'Шурик',
			'mz': get_name('mz') == 'Женя',
			'dv_us': get_name('dv') == 'Алиса' and get_name('us') == 'Ульяна',
		}
	
	python:
		x, y = lineup.get_place(me)
		me.move_to_place({'x': x, 'y': y}, run=True)
	$ me.set_direction(to_right)
	$ cam_to(me, align=(0.5, 0.7))
	
	if clock.minutes <= 33:
		"Когда основная масса пионеров прибыла на линейку и построилась, вожатая начала вещание."
		mt "Сегодня мы подводим итоги очередного дня в нашем пионерлагере!"
		"Она достала список, в котором что-то смотрела."
		mt "Итак, сегодня отличились..."
		"В списке отличившихся числиться я не мог, планы на будущее меня не интересовали, так что вместо того, чтобы слушать выступление, я смотрел на вечернее небо и деревья вокруг."
		"Атмосфера вечернего лагеря не могла не поглощать."
		"..."
		mt "Итак, все победители награждены. Выдающегося пионера у нас сегодня, увы и ах, нету."
		mt "Ну что же, завтра будет насыщенный день. Дадим слово, что будем стараться на мероприятиях и стремиться к победе на соревнованиях!"
		pioneers "Да! Ура!"
		"После крики смешались и деформировались в громкий гул."
		$ clock.add(5 * 60)
	
	python:
		for ch in lineup.characters:
			if ch not in lineup.skip:
				ch.move_to_end()
	
	mt "Внимание!"
	"Хотя пионеры и поутихли, одного раза было недостаточно."
	mt "Кхм. ВНИМАНИЕ!"
	"Строгий окрик Ольги Дмитриевны на этот раз заставил всех замолчать."
	
	# здесь предполагался торжественный спуск флага Славей, но у нас нет никакого флага
	
	mt "Как вы могли заметить, а некоторые - и познакомиться, у нас в отряде прибавление."
	mt "Задерживать всех не буду, да и утром уже все обсуждали, но прошу всех по очереди представиться Семёну."
	$ mt.set_direction(to_back)
	$ me.set_direction(to_forward)
	
	python:
		old_auto_values = [(ch, ch.get_auto()) for ch in lineup.characters]
		for ch in lineup.characters:
			if ch not in lineup.skip:
				ch.set_auto(False)
	
	$ sl.move_to_place({'x': sl.x + 10, 'y': sl.y})
	$ sl.set_direction(to_back)
	sl "Ну, меня ты знаешь. Славя."
	$ set_name('sl', 'Славя')
	$ sl.move_to_place({'x': sl.x - 10, 'y': sl.y})
	$ sl.set_direction(to_right)
	
	$ el.move_to_place({'x': el.x + 20, 'y': el.y})
	$ el.set_direction(to_back)
	$ sh.move_to_place({'x': sh.x + 10, 'y': sh.y})
	$ sh.set_direction(to_back)
	if get_name('el') != 'Электроник' or get_name('sh') != 'Шурик':
		el "Я Сергей."
		sh "Саша. Можно Шурик."
		el "Ну, тогда меня можно Электроник."
		$ set_name('el', 'Электроник')
		$ set_name('sh', 'Шурик')
	else:
		el "Электроник. Шурик."
		sh "Шурик. Да."
	python:
		el.move_to_place({'x': el.x - 20, 'y': el.y})
		sh.move_to_place({'x': sh.x - 10, 'y': sh.y})
	$ el.set_direction(to_right)
	$ sh.set_direction(to_right)
	
	python:
		dv.move_to_place({'x': dv.x + 30, 'y': dv.y})
		us.move_to_place({'x': us.x + 15, 'y': us.y})
	$ dv.set_direction(to_back)
	$ us.set_direction(to_back)
	if get_name('dv') != 'Алиса' or get_name('us') != 'Ульяна':
		dv "Ох. Ну, Алиса."
		us "Как фамилия Ленина."
		mt "Не выпендривайся."
		us "Ц... Ульяна."
		$ set_name('dv', 'Алиса')
		$ set_name('us', 'Ульяна')
	else:
		us "Ульяна. А эта дама - Алиса."
		dv "Я и сама говорить умею!"
	python:
		dv.move_to_place({'x': dv.x - 30, 'y': dv.y})
		us.move_to_place({'x': us.x - 15, 'y': us.y})
	$ dv.set_direction(to_right)
	$ us.set_direction(to_right)
	
	mz "Женя."
	$ set_name('mz', 'Женя')
	
	un "Л-лена..."
	$ set_name('un', 'Лена')
	
	$ mi.set_direction(to_back)
	mi "А я Мику! Это..."
	$ set_name('mi', 'Мику')
	"Мику уже собралась что-то говорить, но Ольга Дмитриевна, будто предвидя это, перебила её."
	mt "Вот и хорошо."
	$ mi.set_direction(to_right)
	$ me.set_direction(to_right)
	extend " Завтра побольше пообщаетесь, а сейчас у вас еще немного времени, чтобы навести марафет и лежать у себя в кроватях."
	$ mt.set_direction(to_left)
	extend " И без всяких выходок!"
	us "А чего это вы на меня смотрите?"
	mt "Пока что ничего. Главное, чтобы не стало \"чего\" до ночи!"
	mt "Я пойду по делам. Семён, пройдись со мной."
	
	python:
		for ch, old_state in old_auto_values:
			if ch not in lineup.skip:
				ch.set_auto(old_state)
	$ lineup.end()
	
	$ mt.get_actions().start(day1_mt_lineup_ending)
	pause 2
	$ me.get_actions().start('follow', mt)
	
	$ cam_to(me, align=(0.5, 0.5))
	me "Так... Что-то важное?"
	mt "Нет. Просто хотела спросить, как день провёл. Не обижали хоть?"
	"Я даже не успел ответить, как она сама рассмеялась."
	mt "Шучу. С кем-нибудь из ребят общался?"
	
	$ name_for_variant_no = ['Нет', 'И больше ни с кем']
	$ menu_iter = 0
	while menu_iter < 2:
		menu:
			"Со Славей" if was_meet['sl'] else None:
				$ was_meet['sl'] = None
				me "Да, со Славей. Она такая... добрая. И ответственная."
				mt "Ну да. Даже не знаю, как бы мне было без нее. Уж с неё точно можешь брать пример!"
			"С кибернетиками" if was_meet['el_sh'] else None:
				$ was_meet['el_sh'] = None
				me "У робототехников был. Довольно необычно."
				mt "Но очень интересно, правда? Если понравилось, то завтра сможешь записаться к ним в кружок."
			"С Женей" if was_meet['mz'] else None:
				$ was_meet['mz'] = None
				me "Ну... библиотека тут такая. Уютная, вот."
				mt "Тяга к знаниям даже в лагере? Уважаю. Взял что-нибудь почитать?"
				me "Ага."
			"С Алисой и Ульяной" if was_meet['dv_us'] else None:
				$ was_meet['dv_us'] = None
				me "Познакомился с Алисой и... Ульяной. Вот."
				mt "Это хорошо. Только не хулигань с ними! Лучше наоборот, если задумают что-нибудь, попытайся отговорить их."
			name_for_variant_no[menu_iter]:
				if menu_iter == 0:
					me "Да как-то не получилось особо."
					mt "Ну ладно, только первый день. Но чтоб завтра без дела не слонялся! Понял?"
					me "Да."
					mt "Молодец."
				else:
					me "И всё."
				break
			
		$ menu_iter += 1
	
	voice "Оля!"
	mt "Иду!"
	mt "Все, давай. К отбою чтоб был в домике!"
	me "Хорошо."
	"Мы подошли к зданию администрации."
	mt "И чтоб из лагеря не убегал! И в лес далеко не заходил!"
	me "...Ладно."
	window hide
	
	python:
		actions = mt.get_actions()
		if actions.state == 'waiting':
			actions.state = 'continue'
		else:
			actions.state = 'moving_without_waiting'
		me.set_auto(False)
	
	pause 1
	"Итак. У меня есть ещё немного времени."
	"Думаю, можно немного прогуляться по лесу, раз уж ничего конкретного всё равно нет."
	th "Только, если уж и идти в лес, то в тот, что рядом с библиотекой, которая недалеко от моего домика. Через весь лагерь не особо хочется возвращаться."
	"С другой стороны, можно было бы пообщаться с кем-нибудь на площади. Если смелости хватит. Вдруг что-нибудь узнаю."
	me "А может, ну его... можно и сразу спать идти."
	"Неинтересно, но сердито. Ладно, по дороге решу."
	window hide
	
	$ set_rpg_control(True)
