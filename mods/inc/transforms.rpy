init -1001 python:
	class Transform:
		def __init__(self, xpos, ypos, xanchor, yanchor):
			self.xpos, self.ypos = xpos, ypos
			self.xanchor, self.yanchor = xanchor, yanchor

init -1000 python:
	fleft  = Transform(0.16,  1.0, 0.5, 1.0)
	left   = Transform(0.28,  1.0, 0.5, 1.0)
	cleft  = Transform(0.355, 1.0, 0.5, 1.0)
	center = Transform(0.50,  1.0, 0.5, 1.0)
	cright = Transform(0.645, 1.0, 0.5, 1.0)
	right  = Transform(0.72,  1.0, 0.5, 1.0)
	fright = Transform(0.84,  1.0, 0.5, 1.0)
	
	true_center = Transform(0.5, 0.5, 0.5, 0.5)
	
