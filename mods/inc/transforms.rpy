init -1001 python:
	class Transform:
		def __init__(self, xpos, ypos, xanchor, yanchor):
			self.xpos, self.ypos = xpos, ypos
			self.xanchor, self.yanchor = xanchor, yanchor

init -1000 python:
	fleft  = Transform(0.10, 1.0, 0.10, 1.0)
	left   = Transform(0.25, 1.0, 0.25, 1.0)
	cleft  = Transform(0.40, 1.0, 0.40, 1.0)
	center = Transform(0.50, 1.0, 0.50, 1.0)
	cright = Transform(0.60, 1.0, 0.60, 1.0)
	right  = Transform(0.75, 1.0, 0.75, 1.0)
	fright = Transform(0.90, 1.0, 0.90, 1.0)
	
	true_center = Transform(0.5, 0.5, 0.5, 0.5)
	
