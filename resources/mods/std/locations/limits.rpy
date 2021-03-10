init 20 python:
	
	def limit_camp_out():
		ban_exit_destination('forest_path-3', 'houses_2')
		ban_exit_destination('forest_path-5', 'stadium')
		ban_exit_destination('enter', 'clubs')
	
	def limit_rooms():
		ban_exit_destination('radio_club', 'clubs')
		for character in (sh, el, sm):
			character.allow_exit_destination('radio_club', 'clubs')
		
		ban_exit_destination('mus_club', 'clubs')
		for character in (mi, dv, sm):
			character.allow_exit_destination('mus_club', 'clubs')
		
		ban_exit_destination('hospital', 'library_and_hospital')
		for character in (cs, mt, sl, un, sm):
			character.allow_exit_destination('hospital', 'library_and_hospital')
		
		ban_exit_destination('canteen', 'square')
		for character in (cs, mt, sl):
			character.allow_exit_destination('canteen', 'square')
	
	def unlimit_all(character):
		for name in rpg_locations:
			character.allow_exit_destination(name)
