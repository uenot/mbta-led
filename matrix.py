import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions

class Matrix:
	def __init__(self):
		options = RGBMatrixOptions()
		options.rows = 64
		options.cols = 64
		self.matrix = RGBMatrix(options=options)
		self.base_canvas = self.matrix.CreateFrameCanvas()
		self.flash_canvas = self.matrix.CreateFrameCanvas()

	def set_pixel(self, x, y, r, g, b, flash=False):
		if not flash:
			self.flash_canvas.SetPixel(x, y, r, g, b)
		self.base_canvas.SetPixel(x, y, r, g, b)

	def run_cycle(self):
		for _ in range(3):
			self.matrix.SwapOnVSync(self.flash_canvas)
			time.sleep(1)
			self.matrix.SwapOnVSync(self.base_canvas)
			time.sleep(1)

	def clear(self):
		self.matrix.Clear()
