init -10000 python:
	
	# 2-й и последующие байты в 2-чном представлении в UTF-8 начинаются с 10 (0b10xxxxxx)
	def is_first_byte(c):
		c = ord(c)
		return not(c & 128) or bool(c & 64)
	
	def len_unicode(s):
		res = 0
		for c in s:
			if is_first_byte(c):
				res += 1
		return res
