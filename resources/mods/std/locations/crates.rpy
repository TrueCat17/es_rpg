init 2 python:
	inventory.set_size(16, rpg_locations['house_mt'].places['cupboard'])
	inventory.set_size(8, rpg_locations['house_mt'].places['exit_table'])
	
	inventory.set_size(6, rpg_locations['house_mt'].places['bedside_table'])
	inventory.add('towel', 1, obj = rpg_locations['house_mt'].places['bedside_table'])
	
	
	inventory.set_size(8, rpg_locations['hospital'].places['enter_table'])
	
	inventory.set_size(12, rpg_locations['radio_storeroom'].places['cupboard'])
