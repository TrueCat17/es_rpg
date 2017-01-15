screen location:
	zorder -4
	
	if cur_location_name:
		python:
			update_location_scale()
			cur_location.update_pos()
			
			for obj in objects_on_location:
				if obj.update:
					obj.update()
			objects_on_location.sort(key = lambda obj: obj.y)
		
		
		image cur_location.main:
			pos (cur_location.x, cur_location.y)
			xysize (cur_location.width * location_scale, cur_location.height * location_scale)
			
			for obj in objects_on_location:
				python:
					obj_x, obj_y = obj.x * location_scale, obj.y * location_scale
					obj_width, obj_height = obj.width * location_scale, obj.height * location_scale
					
					obj_xanchor = obj.xanchor if obj.xanchor <= 1 else obj.xanchor * location_scale
					obj_yanchor = obj.yanchor if obj.yanchor <= 1 else obj.yanchor * location_scale
				
				image obj.image:
					pos 	(obj_x, obj_y)
					anchor 	(obj_xanchor, obj_yanchor)
					xysize 	(obj_width, obj_height)
		
		if cur_location.over:
			image cur_location.over:
				pos (cur_location.x, cur_location.y)
				xysize (cur_location.width * location_scale, cur_location.height * location_scale)
