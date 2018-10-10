init python:
	class CardGameRival:
		def pick_my_card_last(self):
			for i in xrange(n_cards):
				if cards_my[i].interesting:
					x = i
			return x
		
		def allow_to_take(self):
			for card in cards_rival:
				card.allow = True
		def allow_to_defend(self):
			return True
		def want_to_defend(self):
			return True
		
		def what_to_xchange(self):
			i = random.randrange(n_cards)
			j = random.randrange(n_cards)
			while i == j:
				j = random.randrange(n_cards)
			return (i, j)
		
		def give_away_card(self):
			return random.randrange(n_cards)
	
	
	class CardGameRivalUn(CardGameRival):
		def pick_my_card(self):
			while True:
				card = random.choice(cards_my)
				if card.name != card_none and not card.interesting:
					return card.index
		def pick_my_card_last(self):
			return self.pick_my_card()

	class CardGameRivalUs(CardGameRival):
		def pick_my_card(self):
			return None
		
		def allow_to_take(self):
			for card in cards_rival:
				card.allow = False
			while True:
				card = random.choice(cards_rival)
				if not card.hot:
					card.allow = True
					card.interesting = True
					break
		
		def allow_to_defend(self):
			return False
		def want_to_defend(self):
			return False

	class CardGameRivalDv(CardGameRival):
		def pick_my_card(self):
			x_set = []
			for i in xrange(n_cards):
				if cards_my[i].hot and cards_my[i].name != card_none:
					x_set.append(i)
			if x_set:
				return random.choice(x_set)
			while True:
				x = random.randrange(n_cards)
				if cards_my[x].name != card_none:
					return x
		def pick_my_card_last(self):
			return self.pick_my_card()
		def what_to_xchange(self):
			while True:
				i = random.randrange(n_cards)
				if not cards_rival[i].interesting:
					break
			j = random.randrange(n_cards)
			while i == j:
				j = random.randrange(n_cards)
			return (i, j)
	
	
	def get_rival(rival_name):
		global rival_avatar
		rival_avatar = im.Composite((210, 210),
			(0, 0), im.Rect('#CCC', 210, 210),
			(5, 5), 'images/avatars/' + rival_name + '.png'
		)
		
		rivals = {
			'un': CardGameRivalUn,
			'us': CardGameRivalUs,
			'dv': CardGameRivalDv
		}
		return rivals[rival_name]()

