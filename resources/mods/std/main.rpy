init python:
	set_fps(60)
	db_font = 'FixEx3'
	
	day_num = 0
	
	cur_place_name = None
	
	def can_exit_to(to_location_name, to_place_name):
		day_func = globals()['day' + str(day_num) + '_can_exit_to']
		return day_func(to_location_name, to_place_name)


label start:
	call day1_start
	
	while True:
		call on_update
		pause 0.2


label on_update:
	$ exit = get_location_exit()
	if exit and can_exit_to(exit.to_location_name, exit.to_place_name):
		$ set_location(exit.to_location_name, exit.to_place_name)
		call on_change_location
	
	$ cur_place_name = get_location_place()
	if cur_place_name:
		call on_change_place


label on_change_location:
	if renpy.has_label('on__' + cur_location_name):
		call expression 'on__' + cur_location_name

label on_change_place:
	$ cur_label = 'day' + str(day_num) + '__' + cur_location_name + '__' + cur_place_name
	$ cur_exec_label = cur_location_name + '__' + cur_place_name
	
	if renpy.has_label(cur_label):
		call expression cur_label
	if exec_action and renpy.has_label(cur_exec_label):
		call expression cur_exec_label

