#include <iostream>
#include "led-matrix.h"
#include <unistd.h>

using namespace rgb_matrix;

static void draw(Canvas *canvas) {
	canvas->Fill(0, 0, 255);
	std::cout << "test";
	sleep(5);
}

int main(int argc, char *argv[]) {
	RGBMatrix::Options defaultOptions;
	defaultOptions.rows = 64;
	defaultOptions.cols = 64;
	defaultOptions.hardware_mapping = "adafruit-hat";
	defaultOptions.chain_length = 1;
	defaultOptions.parallel = 1;
	defaultOptions.show_refresh_rate = true;

	Canvas *canvas = RGBMatrix::CreateFromFlags(&argc, &argv, &defaultOptions);
	if (canvas == NULL) return 1;
	canvas->Fill(0, 0, 255);
	sleep(3);
	canvas->Clear();
	delete canvas;
}

