label day1:
	$ was = []
	$ day_num = 1
	
	jump day1_ikarus



#Очнулся в икарусе
label day1_ikarus:
	if "bus" not in was:
		$ was.append("bus")
		
		$ set_location("Икарус", "Сиденье")
		$ me.set_direction(right)
		$ me.set_pose("sit")
		
		window show
		"Я очнулся фиг знает где, и тут теперь икарус"
		
		$ me.set_pose("stance")
		pause 1
		$ me.move_to_place("Перед сиденьем")
		$ me.set_direction(back)
		
		"Управление WASD + Shift (бег)"
		window hide
		
		#Тут игрок выводит Семёна из автобуса


#Вышел из автобуса
label day1_bus_station:
	if "bus_station" not in was:
		$ was.append("bus_station")
		
		$ set_direction("Семён", "back")
		pause 0.5
		$ set_direction("Семён", "right")
		pause 0.5
		$ set_direction("Семён", "left")
		pause 0.5
		$ set_direction("Семён", "back")
		
		window show
		"Теперь мы сделали вид, что поосматривались"
		"Тут ещё пара реплик о том, что мы всё ещё фиг знает где, и вообще - мне надо срочно бежать!"
		window hide
		
		$ move_to_place("Семён", "Выход", True)


#Вышел из лагеря и бежит
label day1_try_escape:
	if "try_escape" not in was:
		$ was.append("try_escape")
		
		window show
		"Пробежка помогает придти в себя, но это не обо мне, ля-ля-ля, я возвращаюсь к автобусу"
		
		$ set_location("Совёнок-Вход", "Выход")
		
		"Мб зайти внутрь?"
		window hide
		
		#Подходит к воротам
	else:
		window show
		me "Я уже пытался бежать, ничего хорошего из этого не выйдет"
		window hide



#Встреча со Славей перед входом
label day1_pre_enter:
	if "pre_enter" not in was:
		$ was.append("pre_enter")
		
		window show
		"Я хотел уже было войти, но показалась девочка"
		window hide
		
		$ show_person("Славя", "Лагерь")
		$ move_to_place("Славя", "Вход", False)
		
		window show
		"Привет, привет, ля-ля-ля... вожатая... всё понял... я ушла..."
		window hide
		
		$ move_to_place("Славя", "Лагерь", False)
		$ hide_person("Славя")
		
		#Заходит за ворота



#Подошёл к зданию клубов
label day1_clubs:
	if "clubs" not in was:
		$ was.append("clubs")
		
		window show
		"Хотел идти дальше, но тут вышла {s}Лена{/s} какая-то девушка"
		
		$ show_person(un, "Дверь")
		$ un.move_to_place("Крыльцо-1", False)
		$ un.set_direction(back)
		
		"Хотел подойти, но тут появилась {s}Ульяна{/s} ещё одна"
		
		$ show_person(us, "Куст")
		$ us.set_direction(left)
		pause 0.2
		$ un.set_direction(right)
		
		"Она подошла к первой"
		$ us.move_to_place("Крыльцо-2", True)
		
		"Начала что-то рассказывать и..."
		show cg d1_grasshopper
		extend " напугала её"
		un "Иииии-ииииииииИИИИИ!!!"
		
		"Первая убежала"
		$ un.move_to_place("Площадь", True)
		$ hide_person(un)
		
		"Вторая посмотрела на меня"
		$ us.set_direction(back)
		extend ", а потом бросилась вслед за ней"
		$ us.move_to_place("Площадь", True)
		$ hide_person(us)
		
		window hide
		
		#Семён идёт в локацию площади



#Семён на площади
label day1_square:
	if "square" not in was:
		$ was.append("square")
		
		window show
		"Так... Я на площади, но {s}где же Алиса{/s} почему же меня никто не ударил?"
		window hide
