from rgbmatrix import RGBMatrix, RGBMatrixOptions

class Matrix:
	def __init__(self):
		options = RGBMatrixOptions()
		options.rows = 64
		options.cols = 64
		self.matrix = RGBMatrix(options=options)
		self.canvas = self.matrix.CreateFrameCanvas()

	def set_pixel(self, x, y, r, g, b):
		self.matrix.setPixel(x, y, r, g, b)

	def clear(self):
		self.matrix.Clear()
