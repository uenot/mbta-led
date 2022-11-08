#include <iostream>
#include "./matrix/include/led-matrix.h"
#include <unistd.h>
#include "driver.h"
#include <fstream>
#include <tuple>
#include "./json/single_include/nlohmann/json.hpp"

using json = nlohmann::json;
using namespace rgb_matrix;

/*refactor code to use Points*/
struct Point {
    uint8_t x, y, r, g, b;
};

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
    public:
        Matrix();
        void setPixel(const Point p);
        void setText();
        void setOutline();
        std::vector<Point> getJson(std::string fp);
        void clear();
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

std::vector<Point> Matrix::getJson(std::string fp) {
    std::ifstream f;
    f.open(fp);
    json data = json::parse(f);
    std::vector<Point> points;
    for (json::iterator iter = data.begin(); iter != data.end(); ++iter) {
        Point p = iter.value().get<Point>();
        points.push_back(p);
    }
    f.close();

    return points;
}

void Matrix::setPixel(const Point p) {
	m->SetPixel(p.x, p.y, p.r, p.g, p.b);
}

void Matrix::setText() {
    std::vector<Point> points = this->getJson("../data/text.json");
    for (Point p : points) {
        this->setPixel(p);
        usleep(5*1000);
    }
}

void Matrix::setOutline() {
    std::vector<Point> points = this->getJson("../data/outline.json");
    for (Point p : points) {
        this->setPixel(p);
        usleep(1*1000);
    }
}

void Matrix::clear() {
    m->Clear();
}

int main(int argc, char *argv[]) {
	Matrix mat;
    mat.setText();
    mat.setOutline();
	sleep(3);
    mat.clear();
    sleep(1);
    mat.setText();
    mat.setOutline();
	sleep(3);
    mat.clear();
}

