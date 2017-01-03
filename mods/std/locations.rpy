init python:
	# Вместо x, y подставить реальные координаты
	x = y = 0
	
	# Повороты персонажа, указываются в register_exit и set_direction
	forward = 3
	back = 0
	left = 1
	right = 2
	
	
	# Квартира
	register_location("Квартира", "images/es2d/locations/flat/", "f", True, 192, 272)
	register_place("Квартира", "Кресло", 82, 130)
	
	# Автобусная остановка в городе
	register_location("Остановка", "images/es2d/locations/station/", "fo", False, 736, 992)
	register_place("Остановка", "Начало", 305, 175)
	register_place("Остановка", "Остановка", 305, 400)
	register_place("Остановка", "Вход в автобус", 390, 450)
	register_place("Остановка", "Место автобуса", 400, 220)
	
	# Лиаз
	register_location("Лиаз", "images/es2d/locations/liaz/", "f", True, 432, 216)
	register_place("Лиаз", "Вход", 342, 196)
	register_place("Лиаз", "Перед сиденьем", 334, 96)
	register_place("Лиаз", "Сиденье", 328, 96)
	
	# Икарус
	register_location("Икарус", "images/es2d/locations/ikarus/", "", True, 478, 154)
	register_place("Икарус", "Вход", 420, 147)
	register_place("Икарус", "Сиденье", 398, 72)
	register_place("Икарус", "Перед сиденьем", 410, 77)
	register_exit("Икарус", "Ворота", "У автобуса", 420, 147)
	
	# Вход в лагерь
	register_location("Ворота", "images/es2d/locations/camp_enter/", "", False, 960, 992)
	register_place("Ворота", "У автобуса", x, y)
	register_place("Ворота", "Выход", x, y)
	register_place("Ворота", "Ворота", x, y)
	register_place("Ворота", "Клубы", x, y)
	register_exit("Ворота", "Клубы", "Ворота", x, y)
	register_exit("Ворота", "Икарус", "Вход", x, y)
	
	# Локация со зданием клубов
	register_location("Клубы", "images/es2d/locations/camp_clubs/", "", False, 1280, 1888)
	register_place("Клубы", "Ворота", x, y)
	register_place("Клубы", "Перед клубами", x, y)
	register_place("Клубы", "Дверь", x, y)
	register_place("Клубы", "Куст", x, y)
	register_place("Клубы", "Крыльцо-1", x, y)
	register_place("Клубы", "Крыльцо-2", x, y)
	register_place("Клубы", "Домики-2", x, y)
	register_exit("Клубы", "Ворота", "Клубы", x, y)
	register_exit("Клубы", "Домики-2", "Клубы", x, y)
	
	# Домики-2
	register_location("Домики-2", "images/es2d/locations/houses_2/", "", False, 2080, 1088)
	register_place("Домики-2", "Клубы", x, y)
	register_place("Домики-2", "Площадь", x, y)
	register_exit("Домики-2", "Клубы", "Домики-2", x, y)
	register_exit("Домики-2", "Площадь", "Домики-2", x, y)
	
	# Площадь
	register_location("Площадь", "images/es2d/locations/camp_square/", "", False, 1824, 1408)
	register_place("Площадь", "Домики-2", x, y)
	# ...
	register_exit("Площадь", "Домики-2", "Площадь", x, y)

