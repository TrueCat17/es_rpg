init python:
	sl_beauty__name = 'Славянская красота'

label sl_beauty__start:
	$ set_rpg_control(False)
	$ me.move_to_place('pier_start_before_sit')
	$ me.x, me.y = get_place_center(me.location.places['pier_start_sit'])
	$ me.set_direction(to_right)
	$ me.set_pose('sit')
	
	"Смотря на сверкающую отражениями лучей воду, я подумал, что можно поплескать в ней ноги. Тем более, особо никуда я не спешил."
	me "Какой кайф..."
	
	scene bg black with dissolve
	"..."
	sl "Эй, так тебе не сюда!"
	python:
		sl.move_to_place(None)
		show_character(sl, 'pier_start')
		sl.x += 20
		sl.y -= 50
		sl.set_dress('swim')
		sl.set_direction(to_back)
	hide bg with dissolve
	
	"Я повернул голову и стал созерцателем прекрасного вида на прекрасную девушку."
	sl "Ты вообще в другую сторону забрёл!"
	me "..."
	sl "..."
	sl "Ладно, пошли вместе, мне по дороге. Только ещё переоденусь."
	"Я с неохотой встал и пошёл за девушкой."
	window hide
	
	python:
		sl.move_to_place('closed-1')
		me.x, me.y = get_place_center(cur_location.places['pier_start_before_sit'])
		me.move_to_place([None, 'closed-1', (-50, +50)], wait_time = 0)
	
	$ hide_character(sl)
	pause 2
	$ show_character(sl, 'closed-1')
	$ sl.set_direction(to_back)
	
	python:
		sl.set_dress('pioneer')
		sl.move_to_place(['houses_1', 'square'], wait_time = 0)
	pause 2
	python:
		x, y = get_place_center(rpg_locations['houses_1'].places['house_mt'])
		sl.move_to_place(['houses_1', 'house_mt', (+20, +30)])
		me.move_to_place(['houses_1', 'house_mt', (-20, +30)])
	
	# TODO: Славя идёт к домику ОД, ГГ должен не отставать
	# Если отстаёт 1 раз, Славя спрашивает, чего он отстаёт
	# Dо второй же раз ГГ отвечает, что как-нибудь потом доберётся сам (тогда -1 к отношениям)
	
	$ sl.set_direction(to_left)
	"Мы подошли к домику, окруженному пышной цветущей сиренью."
	sl "Твоя остановочка!"
	me "С-Спасибо."
	"Славяна мило улыбнулась и пошла в своем направлении."
	window hide
	$ sl.get_actions().start('interesting_place')
	$ quest_end('sl_beauty')
	
	call day1__houses_1__house_mt
