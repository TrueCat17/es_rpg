init -1001 python:
	class Transform:
		def __init__(self, xpos, ypos, xanchor, yanchor):
			self.xpos, self.ypos = xpos, ypos
			self.xanchor, self.yanchor = xanchor, yanchor

init -1000 python:
	fleft  = Transform(0.10, 1, 0.10, 1)
	left   = Transform(0.25, 1, 0.25, 1)
	cleft  = Transform(0.40, 1, 0.40, 1)
	center = Transform(0.50, 1, 0.50, 1)
	cright = Transform(0.60, 1, 0.60, 1)
	right  = Transform(0.75, 1, 0.75, 1)
	fright = Transform(0.90, 1, 0.90, 1)
	
	true_center = Transform(0.5, 0.5, 0.5, 0.5)
	
