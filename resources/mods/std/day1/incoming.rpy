label day1__enter__ikarus:
	if 'first_out' in was:
		return
	$ was.append('first_out')
	
	$ set_rpg_control(False)
	"Вот те раз."
	"Внешний мир встречает меня теплом и зелёными деревьями."
	"Остановка явно не моя."
	"И что вообще здесь происходит?"
	"Может быть наша планета приближается к Солнцу, а за то время, пока я спал, весь снег растаял?"
	"Какая глупость."
	"Хотелось было ударить себя по лицу, но кое-что вспомнил."
	"Точно, телефон!"
	"Нет сигнала."
	"Всё равно попробую позвонить..."
	"Тишина. Ни гудков, ни даже голоса, сообщающем о том, что я нахожусь вне зоны покрытия сети."
	"Ладно, может, позже ещё раз попробую."
	window hide
	$ set_rpg_control(True)

label day1__enter__before_gates:
	if 'before_gates' in was:
		return
	$ was.append('before_gates')
	
	$ set_rpg_control(False)
	$ location_cutscene_on(align='down')
	$ me.move_to_place("before_gates")
	$ me.set_direction(to_forward)
	
#	"'Пионерлагерь <Совёнок>' - гласила надпись на воротах."
#	"Сразу вспомнилось детство и рассказы старших друзей о подобных местах."
#	"Сам я в пионерлагерях не был и знал лишь одно - в моё время они все закрыты!"
	
	"..."
	
	"Ещё какое-то время я рассматривал причудливые ворота и статуи детей по обе стороны от них, как с другой стороны ворот послышались быстрые шаги."
	$ sl.set_auto(False)
	$ show_character(sl, 'clubs')
	$ sl.set_direction(to_back)
	$ cam_to(sl, align='up')
	$ sl.start_animation('hello', -1)
	$ sl.move_to_place('behind_gates', wait_time=2)
	$ sl.remove_animation()
	
#	"Не успев испугаться, я увидел девушку у ворот."
#	"Сначала она немного выглядывала наружу, а потом, заметив меня, улыбнулась и показалась в полный рост."
#	
#	sl "О, вот и ты! Се... Сергей, да?"
#	me "С-Семён я."
#	sl "Извини, перепутала... а меня Славя зовут."
#	$ meet('sl', 'Славя')
	sl "Так, вожатая сказала идти тебе сразу к ней. Пошли, я объясню как дойти."
	
	python:
		x, y = get_place_center(rpg_locations['clubs'].places['enter'])
		sl.move_to_place(['clubs', {'x': x + 30, 'y': y}])
		me.move_to_place(['clubs', 'enter'])
	$ sl.set_direction(to_left)
	
	sl "Смотри, сейчас идёшь вперёд до площади, там будет памятник, идёшь к нему. За ним домики."
	sl "Они стоят в три ряда, тебе надо в последний, потом направо и до конца. Вокруг домика вожатой много сирени, так что не ошибёшься."
	"Однако, посмотрев на мой ошеломлённый взгляд, она задала логичный вопрос."
	sl "Наверное, не понял?"
	"Ещё бы!"
	"Однако язык будто бы сам сказал совершенно иное."
	me "Эм... да вроде понял."
	sl "Смотри... ну если что, лагерь небольшой. Да и можешь у кого-нибудь спросить, где домик Ольги Дмитриевны - тебе подскажут."
	me "Ладно."
	
	"Перед уходом Славя посмотрела на меня ещё раз."
	sl "Сейчас жарко. Тут прямо за клубами умывальники, там вода как раз прохладная, можешь освежиться."
	"Будет очень кстати, умираю от жары!"
	sl "Ладно я побежала. Увидимся!"
	window hide
	
	$ sl.move_to_places([['boat_station', 'pier_start'], 'sand_down'], run=True, wait_time=0)
	$ cam_to(me)
	
	$ location_cutscene_off()
	$ set_rpg_control(True)

label day1__clubs__before_clubs:
	if 'before_clubs' in was:
		return
	$ was.append('before_clubs')
	
	$ location_cutscene_on(align='down')
	$ set_rpg_control(False)
	$ me.move_to_place("before_porch")
	$ me.set_direction(to_forward)
	
	"Слева от входа в здание с надписью 'Клубы' стояла девочка. Она будто ждала кого-то."
	window hide
	
	$ un.move_to_place(['clubs', 'porch'])
	
	$ us.start_animation("cricket", 0, 0.7)
	$ us.move_to_place("porch_cleft")
	
	$ un.set_direction(to_left)
	$ un.x += 10
	pause 1
	
	$ us.remove_animation()
	$ us.move_to_place({'x': us.x, 'y': us.y + 40}, run=True)
	$ us.get_actions().start('other_place', 'stadium', run=True)
	$ us.set_auto(True)
	pause 1.5
	
	$ un.set_direction(to_back)
	pause 0.5
	$ un.get_actions().start('home')
	$ un.set_auto(True)
	
	"Забавная сцена. Хотя не хотелось бы быть на месте второй девушки. Неприятно."
	window hide
	
	$ location_cutscene_off()
	$ set_rpg_control(True)

label day1__stadium__forest_path-5:
	if rpg_event == 'no_exit':
		$ set_rpg_control(False)
		"Не думаю, что покидать этот лагерь сейчас - хорошая идея."
		"Сначала нужно во всём разобраться."
		window hide
		$ set_rpg_control(True)
		if 'stadium_from_forest' not in was:
			$ was.append('stadium_from_forest')
	
	if 'stadium_from_forest' in was:
		return
	$ was.append('stadium_from_forest')
	
	if 'before_clubs' not in was:
		$ un.set_auto(True)
		$ us.set_auto(True)
		$ set_rpg_control(False)
		"Ну вот. Что же, раз уж я всё равно зашёл в этот лагерь, то стоит его хотя бы осмотреть."
		window hide
		$ set_rpg_control(True)


label too_hot:
	if random.random() > 0.25:
		return
	
	narrator random.choice([
		"Уфф... жара невыносимая. Было бы неплохо освежиться!",
		"Славя говорила про умывальники. Сейчас как никогда хочется сполоснуться",
	])
	window hide
	
	
