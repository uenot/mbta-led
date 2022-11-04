#include <iostream>
#include "./matrix/include/led-matrix.h"
#include <unistd.h>
#include "driver.h"
#include <fstream>
#include <tuple>
#include "./json/single_include/nlohmann/json.hpp"

using json = nlohmann::json;
using namespace rgb_matrix;

class Matrix {
    public:
        RGBMatrix *m;
        Matrix();
        void setPixel(int x, int y, int r, int g, int b);
};

Matrix::Matrix() {
    RGBMatrix::Options defaultOptions;
    defaultOptions.rows = 64;
    defaultOptions.cols = 64;
    defaultOptions.hardware_mapping = "adafruit-hat";
    defaultOptions.chain_length = 1;
    defaultOptions.parallel = 1;
    defaultOptions.show_refresh_rate = true;

    m = RGBMatrix::CreateFromOptions(defaultOptions, RuntimeOptions());
}

static std::vector<std::tuple<int, int>> getJson() {
    std::ifstream f;
    f.open("data/text.json");
    json data = json::parse(f);
    std::vector<std::tuple<int,int>> points;
    for (json::iterator iter = data.begin(); iter != data.end(); ++iter) {
        std::tuple<int, int> point = iter.value().get<std::tuple<int, int>>();
        points.push_back(point);
    }
    f.close();

    return points;
}

void Matrix::setPixel(int x, int y, int r, int g, int b) {
	m->SetPixel(x, y, r, g, b);
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
	Matrix mat;
    mat.setPixel(32, 32, 255, 0, 0);
}

