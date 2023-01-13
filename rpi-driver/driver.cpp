#include <iostream>
#include "./matrix/include/led-matrix.h"
#include <unistd.h>
#include "driver.h"
#include <fstream>
#include <tuple>
#include "./json/single_include/nlohmann/json.hpp"

using json = nlohmann::json;
using namespace rgb_matrix;

struct Point {
    uint8_t x, y, r, g, b;
};

typedef std::vector<Point> Points; 

void to_json(json& j, const Point& p) {
    j = json{{p.x}, {p.y}, {p.r}, {p.g}, {p.b}};
}

void from_json(const json& j, Point& p) {
    j.at(0).get_to(p.x);
    j.at(1).get_to(p.y);
    try {
        j.at(2).get_to(p.r);
    } catch (json::out_of_range& e) {
        p.r = 255;
    }
    try {
        j.at(3).get_to(p.g);
    } catch (json::out_of_range& e) {
        p.g = 255;
    }
    try {
        j.at(4).get_to(p.b);
    } catch (json::out_of_range& e) {
        p.b = 255;
    }
}

class Matrix {
    RGBMatrix *m;
    FrameCanvas *baseCanvas;
    FrameCanvas *mainCanvas;
    FrameCanvas *altCanvas;
    bool currentCanvas;
    public:
        Matrix();
        void drawToBase(const Points points);
        void setCanvasesToBase();
        void drawToMain(const Points points);
        void swap();
        void swapToMain();
        void swapToAlt();
        void setText();
        void setOutline();
        Points getJson(std::string fp);
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

    baseCanvas = m->CreateFrameCanvas();
    mainCanvas = m->CreateFrameCanvas();
    altCanvas = m->CreateFrameCanvas();
    currentCanvas = false;
}

Points Matrix::getJson(std::string fp) {
    std::ifstream f;
    f.open(fp);
    json data = json::parse(f);
    Points points;
    for (json::iterator iter = data.begin(); iter != data.end(); ++iter) {
        Point p = iter.value().get<Point>();
        points.push_back(p);
    }
    f.close();

    return points;
}

void Matrix::drawToBase(const Points points) {
    for (Point p : points) {
        baseCanvas->SetPixel(p.x, p.y, p.r, p.g, p.b);
    }
}

void Matrix::setCanvasesToBase() {
    mainCanvas->CopyFrom(baseCanvas);
    altCanvas->CopyFrom(baseCanvas);
}

void Matrix::swapToMain() {
    m->SwapOnVSync(mainCanvas);
    currentCanvas = true;
}

void Matrix::swapToAlt() {
    m->SwapOnVSync(altCanvas);
    currentCanvas = false;
}

void Matrix::swap() {
    if (currentCanvas) {
        this->swapToAlt
    } else {
        this->swapToMain
    }
}

void Matrix::setText() {
    Points points = this->getJson("../data/text.json");
    this->drawToBase(points)
}

void Matrix::setOutline() {
    Points points = this->getJson("../data/outline.json");
    this->drawToBase(points);
}

void Matrix::drawToMain(const Points points) {
    for (Point p : points) {
        mainCanvas->SetPixel(p.x, p.y, p.r, p.g, p.b);
    }
}

int main(int argc, char *argv[]) {
	Matrix mat;
    mat.setText();
    mat.setOutline();
    Points ps;
    Point p = {32, 32, 255, 0, 255};
    ps.push_back(p);
    mat.drawToMain(ps);
    for (int i=0; i<3; i++) {
        mat.swapToMain();
        sleep(3);
        mat.swap();
        sleep(3);
    }
}

