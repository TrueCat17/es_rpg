init python:
	def day1_can_exit_to(to_location_name, to_place_name):
		if to_location_name == 'ikarus' and not day1_bus:
			return False
		return True
