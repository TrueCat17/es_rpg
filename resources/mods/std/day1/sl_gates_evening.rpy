label day1__sl_gates_evening:
	if 'us_running' in was and 'sl_after_us_running' in was:
		return
	if 'mt_escaping' in was and 'sl_after_mt_escaping' in was:
		return
	
	$ set_rpg_control(False)
	$ location_cutscene_on(align='down')
	$ me.move_to_place("before_gates")
	$ me.set_direction(to_forward)
	
	$ sl.set_auto(False)
	$ show_character(sl, 'clubs')
	$ sl.set_direction(to_back)
	$ cam_to(sl, align='up')
	$ sl.move_to_place('behind_gates', wait_time=2)
	
	if 'us_running' in was:
		$ was.append('sl_after_us_running')
		call day1__sl_after_us_running
	if 'mt_escaping' in was:
		$ was.append('sl_after_mt_escaping')
		call day1__sl_after_mt_escaping


label day1__sl_after_us_running:
	sl "Семён? Ну наконец!"
	th "Вот так встреча."
	sl "Я уж думала, что ты заблудился где-нибудь."
	me "На самом деле я бы так не заплутал без таланта Ульяны."
	"Славя улыбнулась."
	sl "Прости, но тут вы оба выдали. Ну, с тобой же всё нормально?"
	me "Так-то да."
	sl "Вот и славно!"
	play sound sfx['stomach_growl']
	"..."
	th "Вот чёрт."
	
	sl "Точно, ты же поесть не успел? Если хочешь, можем по дороге зайти в столовую. Там могло что-то остаться."
	menu:
		"А можно?":
			me "А так... можно?"
			sl "Ну мы же не будем выносить ящиками. В столовой часто остается от тех, кто не съел. Или вожатым, которые не успели пообедать."
			me "Ну, если только не сложно."
			sl "С ложечки кормить не буду, так что нет. Идёшь?"
			me "Иду."
			window hide
			
			$ cam_to(me)
			$ location_cutscene_off()
			
			$ quest_start('sl_it_was_possible')
		
		"Нет, спасибо":
			me "Да, честно говоря, не так уж и голоден. Спасибо."
			sl "Точно?"
			me "Точно. До завтра с голода не умру, по крайней мере."
			"Славя рассмеялась."
			sl "Ну как хочешь. Тогда, наверное, спокойной ночи!"
			me "Спокойной."
			window hide
			
			$ sl.get_actions().allow = ['other_place', 'look_around']
			$ sl.set_auto(True)
			$ signals.add('go_to_sleep', SetDict(sl.get_actions(), 'allow', []), priority=-100)
			
			$ cam_to(me)
			$ location_cutscene_off()
			$ set_rpg_control(True)


label day1__sl_after_mt_escaping:
	sl "Семён?"
	th "Дежавю прям. Разве что в этот раз я без пальто, сейчас вечер и Славю я знаю."
	me "О, привет."
	menu:
		"Гуляешь?":
			"Так как лишних вопросов не хотелось, задал вопрос я сам."
			me "Эм... гуляешь тут?"
			sl "Ну да. Выхожу сюда иногда вечером. Тихо, сверчки, приятный ветерок. И людей нет."
			me "А по тебе не скажешь, что ты любишь безлюдные места."
			"Славя улыбнулась."
			sl "Так и есть. Мне нравится помогать людям, быть с детьми. Но я же тоже человек, верно?"
		"Спросить о вожатой":
			"Может и не стоило этого делать, но я всё же спросил."
			me "Слушай, а вожатая ничего такого не говорила?"
			sl "Хм? В плане, про что?"
			me "Ну, там, про домик её... когда я рядом проходил, мне показалось, она на кого-то кричала."
			th "Не палимся, не палимся. Хах, да я гениален на выдумки."
			sl "Да нет вроде. Разве что при мне жаловалась на окна. Мол, который раз они распахиваются. Хотя при чем тут это..."
			th "Стоп. Судя по её словам, когда вожатая зашла, в домике были просто распахнуты окна. Но я же отчетливо слышал, как она кричала мне."
			th "В этом месте ничего не понятно. И лучше не буду расспрашивать дальше, а то кто знает, на что нарвусь."
	
	sl "Кстати, я тебя на ужине не видела."
	menu:
		"Я там был":
			me "Я просто очень быстро поел."
			"И я соврал."
			sl "Ну ладно... Не буду тогда больше задерживать."
			me "С-спокойной ночи."
			sl "И тебе."
			th "Лучше не рисковать. Да и, если бы я признался, что бы это ей дало? Не пошла бы она меня кормить."
			th "Хотя, кто её знает."
			window hide
			
			$ cam_to(me)
			$ location_cutscene_off()
			
			$ sl.set_auto(True)
			$ set_rpg_control(True)
		
		"Пропустил":
			play sound sfx['stomach_growl']
			"Моё тело ответило за меня."
			me "Я пропустил ужин."
			sl "Зря. Было вкусно."
			sl "Впрочем, нам по дороге. Если хочешь, можем заглянуть в столовую, может, осталось там что."
			me "А это... не противозаконно?"
			sl "Нет конечно, мы же не будем дебоширить или красть ящиками."
			me "Тогда... наверное, не откажусь."
			sl "Хорошо. Идём!"
			window hide
			
			$ cam_to(me)
			$ location_cutscene_off()
			
			$ quest_start('sl_it_was_possible')
