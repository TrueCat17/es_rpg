init python:
	db_font = 'FixEx3'
	
	day_num = 0
	
	def can_exit_to(to_location_name, to_place_name):
		day_func = globals()['day' + str(day_num) + '_can_exit_to']
		return day_func(to_location_name, to_place_name)
	
	def get_place_label():
		return 'day' + str(day_num) + '__' + cur_location_name + '__' + cur_place_name


label start:
	call day0_start
	
	while True:
		call rpg_update
		pause 0.2

