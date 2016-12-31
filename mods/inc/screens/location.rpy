screen location:
	window:
		if cur_location_name:
			python:
				cur_location.update_pos()
				
				for obj in objects_on_location:
					if obj.update:
						obj.update()
				objects_on_location.sort(key = lambda obj: obj.y)
			
			
			image cur_location.main:
				pos (cur_location.x, cur_location.y)
				
				for obj in objects_on_location:
					image obj.image:
						pos (obj.x, obj.y)
						anchor (obj.xanchor, obj.yanchor)
			
			if cur_location.over:
				image cur_location.over:
					pos (cur_location.x, cur_location.y)
