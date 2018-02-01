init -1000 python:
	
	quests = []
	
	
	def quest_start(quest):
		name = globals().get(quest + "__name", quest)
		quests.append((quest, name))
		
		if renpy.has_label(quest + '__start'):
			renpy.call(quest + '__start')
	
	def quest_end(quest):
		name = globals().get(quest + "__name", quest)
		quests.remove((quest, name))
		
		if renpy.has_label(quest + '__end'):
			renpy.call(quest + '__end')
	
	def quest_get_labels(location_name, place_name):
		res = []
		
		for quest, name in quests:
			label = quest + '__on__' + location_name + '__' + place_name
			
			if renpy.has_label(label):
				res.append((name, label))
		
		return res

