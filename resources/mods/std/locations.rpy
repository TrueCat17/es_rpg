init python:
	
	register_location("admin", "images/locations/admin/", False, 1376, 1344)
	register_place(   "admin", "clubs"         , 20, 990, 20, 120)
	register_exit(    "admin", "clubs", "admin", 0, 990, 20, 120)
	register_place(   "admin", "square"         , 1336, 990, 20, 120)
	register_exit(    "admin", "square", "admin", 1356, 990, 20, 120)
	
	register_location("bath", "images/locations/bath/", False, 647, 1000)
	register_place(   "bath", "forest_path-6"        , 180, 960, 190, 20)
	register_exit(    "bath", "forest_path-6", "bath", 180, 980, 190, 20)
	
	register_location("beach", "images/locations/beach/", False, 1792, 1408)
	register_place(   "beach", "stadium"         , 800, 20, 350, 20)
	register_exit(    "beach", "stadium", "beach", 800, 0, 350, 20)
	register_place(   "beach", "tennis"         , 1752, 320, 20, 400)
	register_exit(    "beach", "tennis", "beach", 1772, 320, 20, 400)
	
	register_location("board_station", "images/locations/board_station/", False, 1536, 1664)
	register_place(   "board_station", "houses_2"                 , 20, 540, 20, 320)
	register_exit(    "board_station", "houses_2", "board_station", 0, 540, 20, 320)
	register_place(   "board_station", "square"                 , 370, 20, 90, 20)
	register_exit(    "board_station", "square", "board_station", 370, 0, 90, 20)
	
	register_location("canteen", "images/locations/canteen/", False, 1152, 832)
	register_place(   "canteen", "square"           , 750, 792, 100, 20)
	register_exit(    "canteen", "square", "canteen", 750, 812, 100, 20)
	
	register_location("clubs", "images/locations/clubs/", False, 1152, 1664)
	register_place(   "clubs", "musclub_column_pos-1", 774, 400, 2, 2)
	register_place(   "clubs", "musclub_column_pos-2", 836, 400, 2, 2)
	register_place(   "clubs", "musclub_column_pos-3", 899, 400, 2, 2)
	register_place(   "clubs", "musclub_column_pos-4", 962, 400, 2, 2)
	register_place(   "clubs", "musclub_column_pos-5", 1025, 400, 2, 2)
	register_place(   "clubs", "musclub_rails_pos-1", 804, 400, 2, 2)
	register_place(   "clubs", "musclub_rails_pos-2", 867, 400, 2, 2)
	register_place(   "clubs", "musclub_rails_pos-3", 930, 400, 2, 2)
	register_place(   "clubs", "musclub_rails_pos-4", 1056, 400, 2, 2)
	register_place(   "clubs", "admin"         , 1112, 1190, 20, 130)
	register_exit(    "clubs", "admin", "clubs", 1132, 1190, 20, 130)
	register_place(   "clubs", "enter"         , 20, 1190, 20, 130)
	register_exit(    "clubs", "enter", "clubs", 0, 1190, 20, 130)
	register_place(   "clubs", "forest_path-7"         , 620, 20, 130, 20)
	register_exit(    "clubs", "forest_path-7", "clubs", 620, 0, 130, 20)
	register_place(   "clubs", "houses_2"         , 780, 1624, 100, 20)
	register_exit(    "clubs", "houses_2", "clubs", 780, 1644, 100, 20)
	register_place(   "clubs", "musclub"         , 970, 355, 50, 15)
	register_exit(    "clubs", "musclub", "clubs", 970, 340, 50, 15)
	register_place(   "clubs", "radio_club"         , 390, 1135, 120, 15)
	register_exit(    "clubs", "radio_club", "clubs", 390, 1120, 120, 15)
	
	register_location("enter", "images/locations/enter/", False, 960, 992)
	register_place(   "enter", "before_gates", 415, 290, 130, 50)
	register_place(   "enter", "behind_gates", 415, 250, 130, 10)
	register_place(   "enter", "gate_left_pos", 449, 279, 2, 2)
	register_place(   "enter", "gate_right_pos", 509, 279, 2, 2)
	register_place(   "enter", "ikarus_pos", 293, 590, 2, 2)
	register_place(   "enter", "clubs"         , 410, 20, 140, 20)
	register_exit(    "enter", "clubs", "enter", 410, 0, 140, 20)
	register_place(   "enter", "forest_path-5"         , 920, 565, 20, 160)
	register_exit(    "enter", "forest_path-5", "enter", 940, 565, 20, 160)
	register_place(   "enter", "forest_path-9"         , 20, 555, 20, 160)
	register_exit(    "enter", "forest_path-9", "enter", 0, 555, 20, 160)
	register_place(   "enter", "ikarus"         , 400, 600, 40, 15)
	register_exit(    "enter", "ikarus", "enter", 400, 585, 40, 15)
	
	register_location("flat", "images/locations/flat/", True, 192, 272)
	register_place(   "flat", "flat_out", 20, 252, 40, 20)
	
	register_location("forest_path-1", "images/locations/forest_path-1/", False, 1088, 832)
	register_place(   "forest_path-1", "left_exit", 20, 690, 20, 90)
	register_place(   "forest_path-1", "right_exit", 1048, 120, 20, 60)
	register_place(   "forest_path-1", "forest_path-2"                 , 720, 20, 120, 20)
	register_exit(    "forest_path-1", "forest_path-2", "forest_path-1", 720, 0, 120, 20)
	register_place(   "forest_path-1", "old_camp"                 , 605, 792, 110, 20)
	register_exit(    "forest_path-1", "old_camp", "forest_path-1", 605, 812, 110, 20)
	register_exit("forest_path-1", "forest_path-1", "left_exit", 1068, 120, 20, 60)
	register_exit("forest_path-1", "forest_path-1", "right_exit", 0, 690, 20, 90)
	
	register_location("forest_path-2", "images/locations/forest_path-2/", False, 768, 576)
	register_place(   "forest_path-2", "forest_path-1"                 , 120, 536, 80, 20)
	register_exit(    "forest_path-2", "forest_path-1", "forest_path-2", 120, 556, 80, 20)
	register_place(   "forest_path-2", "forest_path-3"                 , 728, 270, 20, 90)
	register_exit(    "forest_path-2", "forest_path-3", "forest_path-2", 748, 270, 20, 90)
	
	register_location("forest_path-3", "images/locations/forest_path-3/", False, 640, 416)
	register_place(   "forest_path-3", "forest_path-2"                 , 20, 310, 20, 60)
	register_exit(    "forest_path-3", "forest_path-2", "forest_path-3", 0, 310, 20, 60)
	register_place(   "forest_path-3", "houses_2"                 , 500, 20, 90, 20)
	register_exit(    "forest_path-3", "houses_2", "forest_path-3", 500, 0, 90, 20)
	
	register_location("forest_path-4", "images/locations/forest_path-4/", False, 544, 416)
	register_place(   "forest_path-4", "forest_path-5"                 , 120, 20, 180, 20)
	register_exit(    "forest_path-4", "forest_path-5", "forest_path-4", 120, 0, 180, 20)
	register_place(   "forest_path-4", "forest_path-9"                 , 120, 376, 180, 20)
	register_exit(    "forest_path-4", "forest_path-9", "forest_path-4", 120, 396, 180, 20)
	
	register_location("forest_path-5", "images/locations/forest_path-5/", False, 544, 416)
	register_place(   "forest_path-5", "enter"                 , 120, 20, 180, 20)
	register_exit(    "forest_path-5", "enter", "forest_path-5", 120, 0, 180, 20)
	register_place(   "forest_path-5", "forest_path-4"                 , 120, 376, 180, 20)
	register_exit(    "forest_path-5", "forest_path-4", "forest_path-5", 120, 396, 180, 20)
	register_place(   "forest_path-5", "forest_path-7"                 , 504, 215, 20, 145)
	register_exit(    "forest_path-5", "forest_path-7", "forest_path-5", 524, 215, 20, 145)
	
	register_location("forest_path-6", "images/locations/forest_path-6/", False, 544, 416)
	register_place(   "forest_path-6", "forest_path-8-2", 20, 120, 20, 80)
	register_place(   "forest_path-6", "bath"                 , 310, 20, 90, 20)
	register_exit(    "forest_path-6", "bath", "forest_path-6", 310, 0, 90, 20)
	register_place(   "forest_path-6", "forest_path-7"                 , 150, 376, 90, 20)
	register_exit(    "forest_path-6", "forest_path-7", "forest_path-6", 150, 396, 90, 20)
	register_place(   "forest_path-6", "forest_path-8"                 , 504, 210, 20, 90)
	register_exit(    "forest_path-6", "forest_path-8", "forest_path-6", 524, 210, 20, 90)
	register_exit("forest_path-6", "forest_path-8", "forest_path-6-2", 0, 120, 20, 80)
	
	register_location("forest_path-7", "images/locations/forest_path-7/", False, 544, 416)
	register_place(   "forest_path-7", "clubs"                 , 220, 376, 80, 20)
	register_exit(    "forest_path-7", "clubs", "forest_path-7", 220, 396, 80, 20)
	register_place(   "forest_path-7", "forest_path-5"                 , 20, 180, 20, 90)
	register_exit(    "forest_path-7", "forest_path-5", "forest_path-7", 0, 180, 20, 90)
	register_place(   "forest_path-7", "forest_path-6"                 , 210, 20, 90, 20)
	register_exit(    "forest_path-7", "forest_path-6", "forest_path-7", 210, 0, 90, 20)
	register_place(   "forest_path-7", "forest_path-8"                 , 504, 80, 20, 90)
	register_exit(    "forest_path-7", "forest_path-8", "forest_path-7", 524, 80, 20, 90)
	
	register_location("forest_path-8", "images/locations/forest_path-8/", False, 544, 416)
	register_place(   "forest_path-8", "forest_path-6-2", 400, 20, 100, 20)
	register_place(   "forest_path-8", "forest_path-6"                 , 20, 210, 20, 90)
	register_exit(    "forest_path-8", "forest_path-6", "forest_path-8", 0, 210, 20, 90)
	register_place(   "forest_path-8", "forest_path-7"                 , 210, 376, 90, 20)
	register_exit(    "forest_path-8", "forest_path-7", "forest_path-8", 210, 396, 90, 20)
	register_place(   "forest_path-8", "tennis"                 , 504, 120, 20, 90)
	register_exit(    "forest_path-8", "tennis", "forest_path-8", 524, 120, 20, 90)
	register_exit("forest_path-8", "forest_path-6", "forest_path-8-2", 400, 0, 100, 20)
	
	register_location("forest_path-9", "images/locations/forest_path-9/", False, 544, 416)
	register_place(   "forest_path-9", "enter"                 , 120, 376, 180, 20)
	register_exit(    "forest_path-9", "enter", "forest_path-9", 120, 396, 180, 20)
	register_place(   "forest_path-9", "forest_path-4"                 , 120, 20, 180, 20)
	register_exit(    "forest_path-9", "forest_path-4", "forest_path-9", 120, 0, 180, 20)
	
	register_location("hospital", "images/locations/hospital/", True, 224, 256)
	register_place(   "hospital", "library_and_hospital"            , 90, 216, 100, 20)
	register_exit(    "hospital", "library_and_hospital", "hospital", 90, 236, 100, 20)
	
	register_location("house_dv", "images/locations/house_dv/", False, 512, 512)
	register_place(   "house_dv", "houses_2"            , 250, 385, 50, 15)
	register_exit(    "house_dv", "houses_2", "house_dv", 250, 400, 50, 15)
	
	register_location("house_mt", "images/locations/house_mt/", True, 544, 416)
	register_place(   "house_mt", "houses_1"            , 230, 320, 50, 15)
	register_exit(    "house_mt", "houses_1", "house_mt", 230, 335, 50, 15)
	
	register_location("house_sl", "images/locations/house_sl/", False, 512, 512)
	register_place(   "house_sl", "houses_1"            , 235, 378, 50, 15)
	register_exit(    "house_sl", "houses_1", "house_sl", 235, 393, 50, 15)
	
	register_location("house_un", "images/locations/house_un/", False, 512, 512)
	register_place(   "house_un", "houses_1"            , 235, 378, 50, 15)
	register_exit(    "house_un", "houses_1", "house_un", 235, 393, 50, 15)
	
	register_location("houses_1", "images/locations/houses_1/", False, 1632, 1152)
	register_place(   "houses_1", "lib_and_hosp-up", 1592, 700, 20, 70)
	register_place(   "houses_1", "house_mt"            , 1090, 365, 60, 15)
	register_exit(    "houses_1", "house_mt", "houses_1", 1090, 350, 60, 15)
	register_place(   "houses_1", "house_sl"            , 1410, 675, 60, 15)
	register_exit(    "houses_1", "house_sl", "houses_1", 1410, 660, 60, 15)
	register_place(   "houses_1", "house_un"            , 190, 355, 70, 15)
	register_exit(    "houses_1", "house_un", "houses_1", 190, 340, 70, 15)
	register_place(   "houses_1", "library_and_hospital"            , 1592, 1020, 20, 110)
	register_exit(    "houses_1", "library_and_hospital", "houses_1", 1612, 1020, 20, 110)
	register_place(   "houses_1", "square"            , 827, 1112, 520, 20)
	register_exit(    "houses_1", "square", "houses_1", 827, 1132, 520, 20)
	register_exit("houses_1", "library_and_hospital", "houses_1-up", 1612, 700, 20, 70)
	
	register_location("houses_2", "images/locations/houses_2/", False, 2112, 1920)
	register_place(   "houses_2", "board_station"            , 2072, 1080, 20, 170)
	register_exit(    "houses_2", "board_station", "houses_2", 2092, 1080, 20, 170)
	register_place(   "houses_2", "clubs"            , 540, 20, 130, 20)
	register_exit(    "houses_2", "clubs", "houses_2", 540, 0, 130, 20)
	register_place(   "houses_2", "forest_path-3"            , 160, 1880, 100, 20)
	register_exit(    "houses_2", "forest_path-3", "houses_2", 160, 1900, 100, 20)
	register_place(   "houses_2", "house_dv"            , 1180, 355, 70, 15)
	register_exit(    "houses_2", "house_dv", "houses_2", 1180, 340, 70, 15)
	register_place(   "houses_2", "square"            , 1921, 20, 130, 20)
	register_exit(    "houses_2", "square", "houses_2", 1921, 0, 130, 20)
	
	register_location("ikarus", "images/locations/ikarus/", True, 478, 154)
	register_place(   "ikarus", "before_sit_place", 409, 76, 2, 2)
	register_place(   "ikarus", "sit_place", 397, 71, 2, 2)
	register_place(   "ikarus", "enter"          , 407, 124, 30, 15)
	register_exit(    "ikarus", "enter", "ikarus", 407, 139, 30, 15)
	
	register_location("liaz", "images/locations/liaz/", True, 432, 216)
	register_place(   "liaz", "lias_enter", 320, 196, 70, 20)
	register_place(   "liaz", "sit_place", 325, 85, 2, 2)
	
	register_location("library", "images/locations/library/", True, 382, 510)
	register_place(   "library", "library_and_hospital"           , 215, 470, 100, 20)
	register_exit(    "library", "library_and_hospital", "library", 215, 490, 100, 20)
	
	register_location("library_and_hospital", "images/locations/library_and_hospital/", False, 1408, 1312)
	register_place(   "library_and_hospital", "houses_1-up", 20, 725, 20, 80)
	register_place(   "library_and_hospital", "hospital"                        , 633, 910, 50, 20)
	register_exit(    "library_and_hospital", "hospital", "library_and_hospital", 633, 890, 50, 20)
	register_place(   "library_and_hospital", "houses_1"                        , 20, 1050, 20, 110)
	register_exit(    "library_and_hospital", "houses_1", "library_and_hospital", 0, 1050, 20, 110)
	register_place(   "library_and_hospital", "library"                        , 1120, 470, 60, 20)
	register_exit(    "library_and_hospital", "library", "library_and_hospital", 1120, 450, 60, 20)
	register_place(   "library_and_hospital", "scene"                        , 510, 20, 70, 20)
	register_exit(    "library_and_hospital", "scene", "library_and_hospital", 510, 0, 70, 20)
	register_exit("library_and_hospital", "houses_1", "lib_and_hosp-up", 0, 725, 20, 80)
	
	register_location("musclub", "images/locations/musclub/", False, 224, 272)
	register_place(   "musclub", "clubs"           , 140, 242, 50, 15)
	register_exit(    "musclub", "clubs", "musclub", 140, 257, 50, 15)
	
	register_location("old_camp", "images/locations/old_camp/", False, 2070, 1740)
	register_place(   "old_camp", "forest_path-1"            , 1160, 1700, 150, 20)
	register_exit(    "old_camp", "forest_path-1", "old_camp", 1160, 1720, 150, 20)
	
	register_location("radio_club", "images/locations/radio_club/", True, 310, 247)
	register_place(   "radio_club", "clubs"              , 215, 217, 60, 15)
	register_exit(    "radio_club", "clubs", "radio_club", 215, 232, 60, 15)
	register_place(   "radio_club", "radio_storeroom"              , 280, 185, 15, 30)
	register_exit(    "radio_club", "radio_storeroom", "radio_club", 295, 185, 15, 30)
	
	register_location("radio_storeroom", "images/locations/radio_storeroom/", False, 162, 247)
	register_place(   "radio_storeroom", "radio_club"                   , 80, 217, 50, 15)
	register_exit(    "radio_storeroom", "radio_club", "radio_storeroom", 80, 232, 50, 15)
	
	register_location("scene", "images/locations/scene/", False, 960, 992)
	register_place(   "scene", "library_and_hospital"         , 400, 952, 150, 20)
	register_exit(    "scene", "library_and_hospital", "scene", 400, 972, 150, 20)
	
	register_location("square", "images/locations/square/", False, 1824, 1344)
	register_place(   "square", "admin"          , 20, 940, 20, 120)
	register_exit(    "square", "admin", "square", 0, 940, 20, 120)
	register_place(   "square", "board_station"          , 310, 1304, 100, 20)
	register_exit(    "square", "board_station", "square", 310, 1324, 100, 20)
	register_place(   "square", "canteen"          , 1187, 655, 80, 10)
	register_exit(    "square", "canteen", "square", 1187, 665, 80, 10)
	register_place(   "square", "houses_1"          , 190, 20, 510, 20)
	register_exit(    "square", "houses_1", "square", 190, 0, 510, 20)
	register_place(   "square", "houses_2"          , 20, 1304, 100, 20)
	register_exit(    "square", "houses_2", "square", 20, 1324, 100, 20)
	register_place(   "square", "stadium"          , 1784, 940, 20, 120)
	register_exit(    "square", "stadium", "square", 1804, 940, 20, 120)
	
	register_location("stadium", "images/locations/stadium/", False, 2080, 1536)
	register_place(   "stadium", "beach"           , 530, 1496, 330, 20)
	register_exit(    "stadium", "beach", "stadium", 530, 1516, 330, 20)
	register_place(   "stadium", "square"           , 20, 1340, 20, 100)
	register_exit(    "stadium", "square", "stadium", 0, 1340, 20, 100)
	register_place(   "stadium", "tennis"           , 1000, 20, 100, 20)
	register_exit(    "stadium", "tennis", "stadium", 1000, 0, 100, 20)
	
	register_location("station", "images/locations/station/", False, 736, 992)
	register_place(   "station", "station_enter", 270, 0, 70, 20)
	
	register_location("tennis", "images/locations/tennis/", False, 992, 670)
	register_place(   "tennis", "beach"          , 430, 20, 100, 20)
	register_exit(    "tennis", "beach", "tennis", 430, 0, 100, 20)
	register_place(   "tennis", "forest_path-8"          , 20, 330, 20, 80)
	register_exit(    "tennis", "forest_path-8", "tennis", 0, 330, 20, 80)
	register_place(   "tennis", "stadium"          , 270, 630, 100, 20)
	register_exit(    "tennis", "stadium", "tennis", 270, 650, 100, 20)
	
	
	
	locations["admin"].x, locations["admin"].y = 732, 356
	locations["bath"].x, locations["bath"].y = 526, 2
	locations["beach"].x, locations["beach"].y = 1234, 498
	locations["board_station"].x, locations["board_station"].y = 868, 490
	locations["canteen"].x, locations["canteen"].y = 986, 344
	locations["clubs"].x, locations["clubs"].y = 481, 352
	locations["enter"].x, locations["enter"].y = 344, 416
	locations["flat"].x, locations["flat"].y = None, None
	locations["forest_path-1"].x, locations["forest_path-1"].y = 336, 750
	locations["forest_path-2"].x, locations["forest_path-2"].y = 400, 650
	locations["forest_path-3"].x, locations["forest_path-3"].y = 532, 628
	locations["forest_path-4"].x, locations["forest_path-4"].y = 68, 326
	locations["forest_path-5"].x, locations["forest_path-5"].y = 68, 227
	locations["forest_path-6"].x, locations["forest_path-6"].y = 482, 136
	locations["forest_path-7"].x, locations["forest_path-7"].y = 470, 244
	locations["forest_path-8"].x, locations["forest_path-8"].y = 618, 126
	locations["forest_path-9"].x, locations["forest_path-9"].y = 68, 428
	locations["hospital"].x, locations["hospital"].y = 1140, 276
	locations["house_dv"].x, locations["house_dv"].y = 690, 682
	locations["house_mt"].x, locations["house_mt"].y = 886, 16
	locations["house_sl"].x, locations["house_sl"].y = 870, 128
	locations["house_un"].x, locations["house_un"].y = 750, -2
	locations["houses_1"].x, locations["houses_1"].y = 818, 278
	locations["houses_2"].x, locations["houses_2"].y = 626, 504
	locations["ikarus"].x, locations["ikarus"].y = 264, 568
	locations["liaz"].x, locations["liaz"].y = None, None
	locations["library"].x, locations["library"].y = 1158, 136
	locations["library_and_hospital"].x, locations["library_and_hospital"].y = 1034, 236
	locations["musclub"].x, locations["musclub"].y = 606, 274
	locations["old_camp"].x, locations["old_camp"].y = 300, 858
	locations["radio_club"].x, locations["radio_club"].y = 332, 294
	locations["radio_storeroom"].x, locations["radio_storeroom"].y = 244, 300
	locations["scene"].x, locations["scene"].y = 1022, 96
	locations["square"].x, locations["square"].y = 870, 384
	locations["stadium"].x, locations["stadium"].y = 1258, 374
	locations["station"].x, locations["station"].y = None, None
	locations["tennis"].x, locations["tennis"].y = 1278, 276

