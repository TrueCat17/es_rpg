init 20 python:
	
	def limit_camp_out():
		ban_exit('houses_2', 'forest_path-3')
		ban_exit('stadium', 'forest_path-5')
		ban_exit('clubs', 'enter')
	
	def limit_rooms():
		ban_exit('clubs', 'radio_club')
		for character in (sh, el, sm):
			character.allow_exit('clubs', 'radio_club')
		
		ban_exit('clubs', 'mus_club')
		for character in (mi, dv, sm):
			character.allow_exit('clubs', 'mus_club')
		
		ban_exit('library_and_hospital', 'hospital')
		for character in (cs, mt, sl, un, sm):
			character.allow_exit('library_and_hospital', 'hospital')
		
		ban_exit('square', 'canteen')
		for character in (cs, mt, sl):
			character.allow_exit('square', 'canteen')
	
	def unlimit_all(character):
		for name in rpg_locations:
			character.allow_exit(name)
