init python:
	def my_interface_bg():
		iw, ih = inventory.xsize, inventory.ysize
		cache = my_interface_bg.__dict__
		key = (iw, ih)
		if key in cache:
			return cache[key]
		
		back = 'images/gui/menu/pause/back.png'
		leaf = 'images/gui/menu/pause/leaf.png'
		x, y = 5, 15
		w, h = get_image_size(leaf)
		k = w / h
		w = iw / 15
		h = w / k
		
		args = [
			(iw, ih),
			(x, y), im.scale(back, iw - x * 2, ih - y * 2),
			(iw - w, ih - h), im.scale(leaf, w, h),
		]
		cache[key] = im.composite(*args)
		return cache[key]
	gui.inventory_bg = my_interface_bg
	gui.inventory_edge_spacing = 60
	
	def get_borders(w, h, border, color):
		cache = get_borders.__dict__
		key = (w, h, border, color)
		if key in cache:
			return cache[key]
		
		vline = im.rect(color, w, border)
		hline = im.rect(color, border, h - border * 2)
		args = [
			(w, h),
			(0, 0), vline,
			(0, h - border), vline,
			(0, border), hline,
			(w - border, border), hline,
		]
		cache[key] = im.composite(*args)
		return cache[key]
	def my_interface_cell_usual():
		return get_borders(inventory.cell_xsize, inventory.cell_ysize, inventory.cell_xsize / 15, gui.my_inventory_cell_usual_color)
	def my_interface_cell_selected():
		return get_borders(inventory.cell_xsize, inventory.cell_ysize, inventory.cell_xsize / 15, gui.my_inventory_cell_selected_color)
	gui.inventory_cell_usual_over = my_interface_cell_usual
	gui.inventory_cell_selected_over = my_interface_cell_selected
	
	gui.my_inventory_cell_usual_color = '#333'
	gui.my_inventory_cell_selected_color = '#A42'

