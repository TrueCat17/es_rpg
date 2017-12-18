init python:
	set_fps(60)

label start:
	scene bg bus_stop
	while True:
		"back"
		show bg ext_aidpost_day with ImageDissolve("images/masks/diamond_1.png")
		"dv"
		show dv normal pioneer at right with ImageDissolve("images/masks/teleport_1.png")
		"us"
		show us grin dress at left with ImageDissolve("images/masks/teleport_2.png")
		"hide dv & us"
		hide dv
		hide us
		with ImageDissolve("images/masks/drag.png")
		"hide back"
		scene bg bus_stop with ImageDissolve("images/masks/drag.png", ramp = 10)

