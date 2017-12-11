init python:
	
	# Квартира
	register_location("flat", "images/locations/flat/", True, 192, 272)
	register_place("flat", "sit_place", 82, 130, 0, 0)
	
	# Автобусная остановка в городе
	register_location("station", "images/locations/station/", False, 736, 992)
	register_place("station", "start", 305, 175, 0, 0)
	register_place("station", "station", 305, 400, 0, 0)
	register_place("station", "bus_enter", 390, 450, 0, 0)
	register_place("station", "bus_pos", 400, 535, 0, 0)
	
	# Лиаз
	register_location("liaz", "images/locations/liaz/", True, 432, 216)
	register_place("liaz", "enter", 342, 196, 0, 0)
	register_place("liaz", "before_sit_place", 334, 96, 0, 0)
	register_place("liaz", "sit_place", 328, 96, 0, 0)
	
	# Икарус
	register_location("ikarus", "images/locations/ikarus/", True, 478, 154)
	register_place("ikarus", "sit_place", 398, 72, 0, 0)
	register_place("ikarus", "before_sit_place", 410, 77, 0, 0)
	register_place("ikarus", "enter", 407, 140, 30, 10)
	register_exit("ikarus", "enter", "bus_enter", 407, 134, 30, 20)
	
	# Вход в лагерь, ворота
	register_location("enter", "images/locations/camp_enter/", False, 960, 992)
	register_place("enter", "bus_pos", 120, 540, 0, 0)
	register_place("enter", "bus_enter", 400, 530, 35, 25)
	register_place("enter", "out", 480, 980, 0, 0)
	register_place("enter", "behind_enter", 490, 240, 0, 0)
	register_place("enter", "enter", 480, 270, 25, 35)
	register_place("enter", "clubs", 410, 0, 150, 10)
	register_exit("enter", "clubs", "enter", 410, 0, 150, 20)
	register_exit("enter", "ikarus", "enter", 400, 530, 35, 25)
	
	# Локация с клубами
	register_location("clubs", "images/locations/camp_clubs/", False, 1280, 1888)
	register_place("clubs", "before_clubs", 700, 1420, 70, 120)
	register_place("clubs", "door", 720, 1355, 0, 0)
	register_place("clubs", "cluster", 515, 1390, 0, 0)
	register_place("clubs", "porch_1", 720, 1440, 0, 0)
	register_place("clubs", "porch_2", 680, 1440, 0, 0)
	register_place("clubs", "enter", 0, 1410, 20, 130)
	register_place("clubs", "admin", 1260, 1420, 20, 120)
	register_place("clubs", "houses_2", 950, 1868, 110, 20)
	register_exit("clubs", "enter", "clubs", 0, 1410, 20, 130)
	register_exit("clubs", "admin", "clubs", 1260, 1420, 20, 120)
	register_exit("clubs", "houses_2", "clubs", 950, 1868, 110, 20)
	
	# Домики-2
	register_location("houses_2", "images/locations/houses_2/", False, 2112, 1920)
	register_place("houses_2", "clubs", 530, 0, 120, 20)
	register_place("houses_2", "square", 1930, 0, 120, 20)
	register_place("houses_2", "board_station", 2092, 1070, 20, 170)
	register_exit("houses_2", "clubs", "houses_2", 530, 0, 120, 20)
	register_exit("houses_2", "square", "houses_2", 1930, 0, 120, 20)
	register_exit("houses_2", "board_station", "houses_2", 2092, 1070, 20, 170)
	
	# Администрация
	register_location("admin", "images/locations/admin/", False, 1376, 1344)
	register_place("admin", "clubs", 0, 990, 20, 120)
	register_place("admin", "square", 1356, 990, 20, 20)
	register_exit("admin", "clubs", "admin", 0, 990, 20, 120)
	register_exit("admin", "square", "admin", 1356, 990, 20, 120)
	
	# Площадь
	register_location("square", "images/locations/camp_square/", False, 1824, 1344)
	register_place("square", "admin", 0, 940, 20, 120)
	register_place("square", "houses_1", 200, 0, 500, 20)
	register_place("square", "houses_2", 30, 1324, 85, 20)
	register_place("square", "board_station", 315, 1324, 85, 20)
	register_exit("square", "admin", "square", 0, 940, 20, 120)
	register_exit("square", "houses_1", "square", 200, 0, 500, 20)
	register_exit("square", "houses_2", "square", 30, 1324, 85, 20)
	register_exit("square", "board_station", "square", 315, 1324, 85, 20)
	
	# Лодочная станция
	register_location("board_station", "images/locations/board_station/", False, 1536, 1664)
	register_place("board_station", "houses_2", 0, 550, 20, 300)
	register_place("board_station", "square", 385, 0, 60, 20)
	register_exit("board_station", "houses_2", "board_station", 0, 550, 20, 300)
	register_exit("board_station", "square", "board_station", 385, 0, 60, 20)
	
	# Домики-1
	register_location("houses_1", "images/locations/houses_1/", False, 1632, 1152)
	register_place("houses_1", "square", 820, 1132, 520, 20)
#	register_place("houses_1", "clubs", 530, 0, 120, 20)
#	register_place("houses_1", "board_station", 2092, 1070, 20, 170)
	register_exit("houses_1", "square", "houses_1", 820, 1132, 520, 20)
#	register_exit("houses_1", "clubs", "houses_1", 530, 0, 120, 20)
#	register_exit("houses_1", "board_station", "houses_1", 2092, 1070, 20, 170)
	
	
	
