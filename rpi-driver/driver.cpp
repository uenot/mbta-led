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
    RGBMatrix *m;
    public:
        Matrix();
        void setPixel(int x, int y, int r, int g, int b);
        void setText();
        std::vector<std::tuple<int, int>> getJson(std::string fp);
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

std::vector<std::tuple<int, int>> Matrix::getJson(std::string fp) {
    std::ifstream f;
    f.open(fp);
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

void Matrix::setText() {
    std::vector<std::tuple<int, int>> points = this->getJson("data/text.json");
    for (std::tuple<int, int> point : points) {
        this->setPixel(std::get<0>(point), std::get<1>(point), 255, 255, 255);
    }
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
    mat.setText();
	sleep(3);
}

