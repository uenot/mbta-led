import ctypes
import os

clib_path = os.path.dirname(os.path.realpath(__file__)) + "/rpi-driver/driver.so"
clib = ctypes.CDLL(clib_path)

clib.createCanvasAndDraw(32, 32, 255, 0, 0)