#Вместо x, y подставить реальные координаты

init python:
	x = y = 0
	
	# Повороты персонажа, указываются в register_exit и set_direction
	forward = 3
	back = 0
	left = 1
	right = 2
	
	
	#Квартира
	register_location("Квартира", "images/es2d/locations/flat/", "f")
	register_place("Квартира", "Кресло", 82, 130)
	
	#Автобусная остановка
	register_location("Остановка", "images/es2d/locations/station/", "fo")
	register_place("Остановка", "Начало", 305, 175)
	register_place("Остановка", "Остановка", 305, 400)
	register_place("Остановка", "Вход в автобус", 390, 450)
	register_place("Остановка", "Место автобуса", 400, 220)
	
	#Лиаз
	register_location("Лиаз", "images/es2d/locations/liaz/", "f")
	register_place("Лиаз", "Вход", 400, 300)
	register_place("Лиаз", "Перед сиденьем", 392, 200)
	register_place("Лиаз", "Сиденье", 387, 200)
	
	#Икарус
	register_location("Икарус", "images/es2d/locations/ikarus/", "")
	register_place("Икарус", "Вход", 580, 470)
	register_place("Икарус", "Сиденье", 558, 395)
	register_place("Икарус", "Перед сиденьем", 570, 400)
	register_exit("Икарус", "Ворота", "У автобуса", 580, 470)
	
	#Вход в лагерь
	register_location("Ворота", "images/es2d/locations/camp_enter/", "")
	register_place("Ворота", "У автобуса", x, y)
	register_place("Ворота", "Выход", x, y)
	register_place("Ворота", "Ворота", x, y)
	register_place("Ворота", "Клубы", x, y)
	register_exit("Ворота", "Клубы", "Ворота", x, y)
	register_exit("Ворота", "Икарус", "Вход", x, y)
	
	#Локация со зданием клубов
	register_location("Клубы", "images/es2d/locations/camp_clubs/", "")
	register_place("Клубы", "Ворота", x, y)
	register_place("Клубы", "Перед клубами", x, y)
	register_place("Клубы", "Дверь", x, y)
	register_place("Клубы", "Куст", x, y)
	register_place("Клубы", "Крыльцо-1", x, y)
	register_place("Клубы", "Крыльцо-2", x, y)
	register_place("Клубы", "Домики 18-24", x, y)
	register_exit("Клубы", "Ворота", "Клубы", x, y)
	register_exit("Клубы", "Домики 18-24", "Клубы", x, y)
	
	#Домики 18-24
	register_location("Домики 18-24", "images/es2d/locations/houses_18-24/", "")
	register_place("Домики 18-24", "Клубы", x, y)
	register_place("Домики 18-24", "Площадь", x, y)
	register_exit("Домики 18-24", "Клубы", "Домики 18-24", x, y)
	register_exit("Домики 18-24", "Площадь", "Домики 18-24", x, y)
	
	#Площадь
	register_location("Площадь", "images/es2d/locations/camp_square/", "")
	register_place("Площадь", "Домики 18-24", x, y)
	#...
	register_exit("Площадь", "Домики 18-24", "Площадь", x, y)
