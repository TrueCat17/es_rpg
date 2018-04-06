label day1_start:
	python:
		was = []
		day_num = 1
		
		day1_bus = True
		
		me.set_dress('winter')
		us.set_dress('sport')
		
		set_location("ikarus", "sit_place")
		me.set_direction(to_right)
		me.set_pose("sit")
		
		control = False
	
	window show
	"Я очнулся фиг знает где, и тут теперь икарус."
	
	$ me.set_pose("stance")
	pause 1
	$ me.move_to_place("before_sit_place")
	$ me.set_direction(to_back)
	
	"Управление WASD/стрелки + Ctrl/Shift (бег)."
	window hide
	$ control = True


label day1__enter__bus_enter:
	if "bus_out" not in was:
		$ was.append("bus_out")
		
		$ control = False
		$ me.move_kind = 'stay'
		
		$ me.set_direction(to_back)
		pause 0.5
		$ me.set_direction(to_right)
		pause 0.5
		$ me.set_direction(to_left)
		pause 0.5
		$ me.set_direction(to_back)
		
		window show
		"Теперь мы сделали вид, что поосматривались."
		"Тут ещё пара реплик о том, что мы всё ещё фиг знает где, и вообще - надо срочно бежать!"
		window hide
		
		$ control = True
#		$ me.move_to_place("out", True)


# Пока не используется
label day1_try_escape:
	if "try_escape" not in was:
		$ was.append("try_escape")
		
		window show
		"Пробежка помогает придти в себя, но это не обо мне, ля-ля-ля, я возвращаюсь к автобусу."
		
		$ set_location("Совёнок-Вход", "Выход")
		
		"Мб мне лучше всё-таки зайти за ворота?"
		window hide
	else:
		window show
		me "Я уже пытался бежать, ничего хорошего из этого не выйдет."
		window hide


label day1__enter__enter:
	if "enter_welcome" not in was:
		$ was.append("enter_welcome")
		
		$ control = False
		$ me.move_kind = 'stay'
		$ me.set_direction(to_forward)
		
		window show
		"Я хотел уже было войти, но показалась девочка."
		window hide
		
		$ show_character(sl, "clubs")
		$ sl.move_to_place("behind_enter", False)
		
		window show
		sl "Привет, ля-ля-ля...вожатая...всё понял...я ушла..."
		window hide
		
		$ sl.move_to_place("clubs")
		$ hide_character(sl)
		
		$ control = True


label day1__clubs__before_clubs:
	if "clubs" not in was:
		$ was.append("clubs")
		
		$ control = False
		$ me.move_kind = 'stay'
		
		window show
		"Хотел идти дальше, но тут вышла {s}{color=" + un.color + "}Лена{/color}{/s} какая-то девушка."
		
		$ me.set_direction(to_forward)
		$ show_character(un, "door")
		$ un.move_to_place("porch_1")
		
		"Хотел подойти, но тут появилась {s}{color=" + us.color + "}Ульяна{/color}{/s} ещё одна."
		
		$ show_character(us, "cluster")
		$ us.set_direction(to_right)
		pause 0.2
		$ un.set_direction(to_left)
		
		"Она подошла к первой."
		$ us.move_to_place("porch_2", True)
		
		"Начала что-то рассказывать и..."
		scene cg d1_grasshopper
		extend "напугала её!"
		un "Иииии-ииииииииИИИИИ!!!"
		scene
		
		"Первая убежала."
		$ un.set_direction(to_right)
		$ un.move_to_place("admin", True, 0.5)
		
		"Вторая посмотрела на меня"
		$ us.set_direction(to_back)
		extend ", а потом бросилась вслед за ней."
		$ me.set_direction(to_right)
		$ us.move_to_place("admin", True)
		$ hide_character(un)
		$ hide_character(us)
		
		window hide
		
		$ control = True


label day1__square__clubs:
	if "square" not in was:
		$ was.append("square")
		
		$ control = False
		$ me.move_kind = 'stay'
		
		window show
		"Так... Я на площади, но {s}где же Алиса{/s} почему же меня никто не ударил..?"
		window hide
		
		$ control = True
		
