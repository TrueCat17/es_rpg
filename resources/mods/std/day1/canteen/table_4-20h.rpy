init python:
	def day1_us_running(character, state):
		if state == 'start':
			lineup.skip.append(character)
			character.get_actions().interruptable = False
			character.move_to_places([('houses_1', 'square'), ('forest_path-8', 'tennis'), ('forest_path-8', 'forest_path-7')], run=True)
			return 'moving'
		
		if state == 'moving':
			if not character.ended_move_waiting():
				if character.location.name.startswith('forest_path'):
					character.set_pose('run')
					character.speed *= 1.1
				elif me.location is character.location:
					dist = get_dist(me.x, me.y, character.x, character.y)
					if dist < 150:
						character.set_pose('run')
						character.speed *= 1.1
					elif dist > 250:
						character.set_pose('walk')
				return 'moving'
			return 'end'
		
		if state == 'end':
			lineup.skip.remove(character)
			show_character(character, 'houses_2', 'house_dv')
			return 'end'


label day1__canteen__table-4-time20h:
	$ canteen.wait(us)
	
	th "Котлета и пюре. Вроде же на обед было то же самое?"
	th "Хотя, нашёл к чему придираться. Кормят бесплатно. И вкусно. И пока что не травили."
	$ clock.add(2 * 60)
	
	if canteen.finished(us):
		return
	
	th "Ладно, что-то я задумался. Ну-с, приятного аппе..."
	"Котлеты не было."
	"Зато была Ульяна, настолько неудачно сдерживающая смех, что даже не то что сомнений - мыслей о том, что это сделала не она, не было."
	me "Эм... как бы..."
	us "А что? В большой семье клювом не щёлкай!"
	menu:
		"Смириться":
			"На всякие глупые разборки меня не тянуло."
			me "Ну и подавись этой котлетой."
			us "Бе-бе-бе."
			$ clock.add(3 * 60)
		"Пригрозить":
			me "Отдай. Котлету."
			us "Какую ещё? У меня ничего нет, смотри!"
			"Ульяна демонстративно вытянула вперёд руки и засмеялась."
			me "Смотри. Видишь там Ольгу Дмитриевну? Так вот, через некоторое время она может очень \"обрадоваться\" историям о твоих выходках."
			us "Ничего не знаю, я чиста как... как белый кот."
			th "Вот зараза..."
			me "А вот Лена знает. Ты же не забыла, что было до обеда? Да и я присоединюсь."
			"Ульяна посмотрела на Лену, потом нахмурилась и перевела взгляд куда-то в пол."
			us "Ладно уж, держи свою котлету, голодающий! Как ребёнок, ей-богу..."
			"Ульяна переложила целую котлету со своей тарелки на мою."
			"Справедливость восторжествовала!"
			$ us.rp += 1
			$ clock.add(3 * 60)
		"Отнять силой":
			$ was.append('us_running')
			me "Сейчас ты будешь кое-чем щёлкать, если не вернёшь чужое!"
			us "А ты попробуй, догони!"
			$ us.get_actions().start(day1_us_running)
			th "Ну уж нет, чёрта с два я оставлю всё как есть!"
			$ me.stand_up()
