#include <iostream>
#include "led-matrix.h"
#include <unistd.h>

using namespace rgb_matrix;

static void draw(Canvas *canvas) {
	canvas->SetPixel(32, 32, 255, 215, 0);
	sleep(5);
}

static int createCanvasAndDraw(int x, int y, int r, int g, int b) {
	RGBMatrix::Options defaultOptions;
        defaultOptions.rows = 64;
        defaultOptions.cols = 64;
        defaultOptions.hardware_mapping = "adafruit-hat";
        defaultOptions.chain_length = 1;
        defaultOptions.parallel = 1;
        defaultOptions.show_refresh_rate = true;

        Canvas *canvas = RGBMatrix::CreateFromOptions(defaultOptions, RuntimeOptions());
        if (canvas == NULL) return 1;
        canvas->SetPixel(x, y, r, g, b);
	sleep(3);
        canvas->Clear();
        delete canvas;
	return 0;
}

int main(int argc, char *argv[]) {
	createCanvasAndDraw(32, 32, 255, 0, 255);
}

