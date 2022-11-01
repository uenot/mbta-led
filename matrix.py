import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions

class Matrix:
	def __init__(self, default=None):
		options = RGBMatrixOptions()
		options.rows = 64
		options.cols = 64
		self.matrix = RGBMatrix(options=options)
		self.base_canvas = self.matrix.CreateFrameCanvas()
		self.flash_canvas = self.matrix.CreateFrameCanvas()
		self.empty_canvas = self.matrix.CreateFrameCanvas()
		self.default = default

	def set_pixel(self, x, y, r, g, b, flash=False):
		if not flash:
			self.flash_canvas.SetPixel(x, y, r, g, b)
		self.base_canvas.SetPixel(x, y, r, g, b)

	def set_defaults(self):
		if self.default is not None:
			for x, y in self.default:
				self.set_pixel(x, y, 255, 255, 255, flash=True)
				self.set_pixel(x, y, 255, 255, 255, flash=False)

	def run_cycle(self):
		for _ in range(2):
			self.matrix.SwapOnVSync(self.flash_canvas)
			time.sleep(1)
			self.matrix.SwapOnVSync(self.base_canvas)
			time.sleep(1)
		self.matrix.SwapOnVSync(self.flash_canvas)
		time.sleep(0.5)
		self.base_canvas.Clear()
		self.set_defaults()
		time.sleep(0.5)
		self.matrix.SwapOnVSync(self.base_canvas)
		time.sleep(0.5)
		self.flash_canvas.Clear()
		self.set_defaults()
		time.sleep(0.5)

	def clear_canvases(self):
		self.matrix.SwapOnVSync(self.empty_canvas)
		self.flash_canvas.Clear()
		self.base_canvas.Clear()
		self.set_defaults()

	def clear(self):
		self.matrix.Clear()
