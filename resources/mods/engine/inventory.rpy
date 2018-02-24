init -1000 python:
	
	inventory_size = 30
	
	inventory = [None] * inventory_size
	
	
	def add_to_inventory(obj_name, count):
		if not location_objects.has_key(obj_name):
			out_msg('add_to_inventory', 'Объект с именем <' + obj_name + '> не зарегистрирован')
			return count
		obj = location_objects[obj_name]
		
		while count > 0:
			index = -1
			for i in xrange(inventory_size):
				element = inventory[i]
				if element is not None and element[0] == obj_name and element[1] < obj['max_in_inventory_cell']:
					index = i
					break
			else:
				for i in xrange(inventory_size):
					if inventory[i] is None:
						index = i
						break
			
			if index == -1:
				break
			
			if inventory[index] is None:
				inventory[index] = [obj_name, 0]
			
			element = inventory[index]
			d = min(obj['max_in_inventory_cell'] - element[1], count)
			
			element[1] += d
			count -= d
		
		return count
	
	def has_in_inventory(obj_name, count):
		if not location_objects.has_key(obj_name):
			out_msg('add_to_inventory', 'Объект с именем <' + obj_name + '> не зарегистрирован')
			return False
		
		t = 0
		for element in inventory:
			if element[0] == obj_name:
				t += element[1]
				if t >= count:
					return True
		return False
	
	def remove_from_inventory(obj_name, count):
		if not location_objects.has_key(obj_name):
			out_msg('add_to_inventory', 'Объект с именем <' + obj_name + '> не зарегистрирован')
			return count
		
		while count > 0:
			index = -1
			for i in xrange(inventory_size):
				element = inventory[i]
				if element[0] == obj_name and element[1] < obj['max_in_inventory_cell']:
					index = i
					break
			else:
				break
			
			element = inventory[index]
			if element[1] > count:
				element[1] -= count
			else:
				count -= element[1]
				inventory[index] = None
		
		return count
		
	
