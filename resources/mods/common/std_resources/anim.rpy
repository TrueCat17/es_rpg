init -1000:
	
	$ default_decl_at = []
	
	image anim owl_1 = "images/anim/owl_1.png"
	image anim owl_2 = "images/anim/owl_2.png"
	
	image owl:
		"anim owl_1"
		pause 5
		"anim owl_2"
		pause 0.5
		repeat
	
	
	$ default_decl_at = ["size (1.0, 1.0)"]
	
	
	image anim blink_down = "images/anim/blink_down.png"
	image anim blink_up = "images/anim/blink_up.png"
	
	image anim candle_1 = "images/anim/candle_1.png"
	image anim candle_2 = "images/anim/candle_2.png"
	
	image anim intro_1 = "images/anim/intro_1.jpg"
	image anim intro_2 = "images/anim/intro_2.jpg"
	image anim intro_3 = "images/anim/intro_3.jpg"
	image anim intro_4 = "images/anim/intro_4.jpg"
	image anim intro_5 = "images/anim/intro_5.jpg"
	image anim intro_6 = "images/anim/intro_6.jpg"
	image anim intro_7 = "images/anim/intro_7.jpg"
	image anim intro_8 = "images/anim/intro_8.jpg"
	image anim intro_9 = "images/anim/intro_9.jpg"
	image anim intro_10 = "images/anim/intro_10.jpg"
	image anim intro_11 = "images/anim/intro_11.jpg"
	image anim intro_12 = "images/anim/intro_12.jpg"
	image anim intro_13 = "images/anim/intro_13.jpg"
	image anim intro_14 = "images/anim/intro_14.jpg"
	image anim intro_15 = "images/anim/intro_15.jpg"
	image anim intro_16 = "images/anim/intro_16.jpg"
	
	image anim prolog_1 = "images/anim/prolog_1.jpg"
	image anim prolog_2 = "images/anim/prolog_2.jpg"
	image anim prolog_3 = "images/anim/prolog_3.jpg"
	image anim prolog_4 = "images/anim/prolog_4.jpg"
	image anim prolog_5 = "images/anim/prolog_5.jpg"
	image anim prolog_10 = "images/anim/prolog_10.jpg"
	image anim prolog_11 = "images/anim/prolog_11.jpg"
	image anim prolog_14 = "images/anim/prolog_14.jpg"
	image anim prolog_15 = "images/anim/prolog_15.jpg"
	
	image anim prologue_1 = "images/anim/prologue_1.png"
	image anim prologue_2 = "images/anim/prologue_2.png"
	image anim prologue_3 = "images/anim/prologue_3.png"
	
	image anim prologue_keyboard_1 = im.BlurH(im.Scale("images/anim/prologue_keyboard.jpg", get_stage_width(), get_stage_height()), 75)
	image anim prologue_keyboard_2 = im.BlurH(im.Scale("images/anim/prologue_keyboard.jpg", get_stage_width(), get_stage_height()), 50)
	image anim prologue_keyboard_3 = im.BlurH(im.Scale("images/anim/prologue_keyboard.jpg", get_stage_width(), get_stage_height()), 25)
	image anim prologue_keyboard_4 = im.Scale("images/anim/prologue_keyboard.jpg", get_stage_width(), get_stage_height())
	
	image anim prologue_keyboard_monitor_1 = "images/anim/prologue_keyboard_monitor_1.jpg"
	image anim prologue_keyboard_monitor_2 = "images/anim/prologue_keyboard_monitor_2.jpg"
	image anim prologue_keyboard_monitor_3 = "images/anim/prologue_keyboard_monitor_3.jpg"
	image anim prologue_keyboard_monitor_4 = "images/anim/prologue_keyboard_monitor_4.jpg"
	
	image anim prologue_monitor_1 = im.BlurH(im.Scale("images/anim/prologue_monitor.jpg", get_stage_width(), get_stage_height()), 75)
	image anim prologue_monitor_2 = im.BlurH(im.Scale("images/anim/prologue_monitor.jpg", get_stage_width(), get_stage_height()), 50)
	image anim prologue_monitor_3 = im.BlurH(im.Scale("images/anim/prologue_monitor.jpg", get_stage_width(), get_stage_height()), 25)
	image anim prologue_monitor_4 = im.Scale("images/anim/prologue_monitor.jpg", get_stage_width(), get_stage_height())
	
	image anim stars_1 = "images/anim/stars_1.jpg"
	image anim stars_3 = "images/anim/stars_3.jpg"
	
	image stars:
		size (1.0, 1.0)
		
		contains "anim stars_1"
		contains "anim stars_3":
			linear 1.5 alpha 1.0
			linear 1.5 alpha 0.0
			repeat
	
	
	image prologue_dream:
		size (1.0, 1.0)
		"images/anim/prologue_1.png"
		pause 0.1
		"images/anim/prologue_2.png"
		pause 0.1
		"images/anim/prologue_3.png"
		pause 0.1
		"images/anim/prologue_2.png"
		repeat
	
	image anim 1 _prologue:
		size (1.0, 1.0)
		"anim prologue_keyboard_1"
		pause 6
		"anim prologue_keyboard_2"
		pause 0.1
		"anim prologue_keyboard_3"
		pause 0.1
		"anim prologue_keyboard_4"
		pause 3
		"anim prologue_keyboard_3"
		pause 0.1
		"anim prologue_keyboard_2"
		pause 0.1
		"anim prologue_keyboard_1"
	
	image anim 2 _prologue:
		size (1.0, 1.0)
		"anim prologue_keyboard_monitor_1"
		pause 6
		"anim prologue_keyboard_monitor_2"
		pause 0.1
		"anim prologue_keyboard_monitor_3"
		pause 0.1
		"anim prologue_keyboard_monitor_4"
		pause 3
		"anim prologue_keyboard_monitor_3"
		pause 0.1
		"anim prologue_keyboard_monitor_2"
		pause 0.1
		"anim prologue_keyboard_monitor_1"
	
	image anim 3 _prologue:
		size (1.0, 1.0)
		"anim prologue_monitor_1"
		pause 6
		"anim prologue_monitor_2"
		pause 0.1
		"anim prologue_monitor_3"
		pause 0.1
		"anim prologue_monitor_4"
	
	
	
	image blink:
		size (1.0, 1.0)
		
		contains:
			"anim blink_up"
			ypos -1.0
			ease 1.5 ypos 0.0
		contains:
			"anim blink_down"
			ypos 1.0
			ease 1.5 ypos 0.0
	
	
	image unblink:
		size (1.0, 1.0)
		
		contains:
			"anim blink_up"
			ypos 0
			ease 1.5 ypos -1.0
		contains:
			"anim blink_down"
			ypos 0
			ease 1.5 ypos 1.0
	
	
	image blinking:
		size (1.0, 1.0)
		
		contains:
			"anim blink_up"
			ypos -1.0
			ease 1.5 ypos 0
		contains:
			"anim blink_down"
			ypos 1.0
			ease 1.5 ypos 0
		
		pause 2.0
		
		contains:
			"anim blink_up"
			ypos 0
			ease 1.5 ypos -1.0
		contains:
			"anim blink_down"
			ypos 0
			ease 1.5 ypos 1.0
	
	
	image bg ext_camp_entrance_day_sepia = im.Sepia("images/bg/ext_camp_entrance_day.jpg")
	
	image black_long:
		contains "bg ext_camp_entrance_day_sepia"
		contains "bg black":
			alpha 0.0
			linear 50 alpha 1.0
	
	
	image op_back = "images/misc/op/back.jpg"
	image op_sl = "images/misc/op/sl.png"
	image op_un = "images/misc/op/un.png"
	image op_us = "images/misc/op/us.png"
	image op_dv = "images/misc/op/dv.png"
	image op_mi = "images/misc/op/mi.png"
	image op_uv1 = "images/misc/op/uv1.png"
	image op_uv2 = "images/misc/op/uv2.png"
	image op_uv3 = "images/misc/op/uv3.png"
	
	image op_uv:
		"op_uv1"
		pause 0.5
		"op_uv2"
		pause 0.5
		"op_uv3"
		pause 0.5
		"op_uv2"
		pause 0.5
		"op_uv1"
	
	$ default_decl_at = []

