init -1000:
	
	$ default_decl_at = ["size (1.0, 1.0)"]
	
	python:
		prologue_pause = 1
	
	image prologue_sleep:
		"images/anim/prologue/sleep1.png"
		prologue_pause
		"images/anim/prologue/sleep2.png"
		prologue_pause
		repeat
	
	image prologue_wake:
		"images/anim/prologue/wake1.png"
		prologue_pause
		"images/anim/prologue/wake2.png"
		prologue_pause
		repeat
	
	image prologue_keyboard:
		"images/anim/prologue/keyboard1.png"
		prologue_pause
		"images/anim/prologue/keyboard2.png"
		prologue_pause
		repeat
	
	image prologue_monitor:
		"images/anim/prologue/monitor1.png"
		prologue_pause
		"images/anim/prologue/monitor2.png"
		prologue_pause
		repeat
	
	image prologue_message:
		"images/anim/prologue/message1.png"
		prologue_pause
		"images/anim/prologue/message2.png"
		prologue_pause
		repeat
	
	$ default_decl_at = []

