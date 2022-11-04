#include <iostream>
#include <fstream>
#include <tuple>
#include "./json/single_include/nlohmann/json.hpp"

using json = nlohmann::json;

static void getJson() {
        std::ifstream f;
        f.open("../data/text.json");
        json data = json::parse(f);
        for (json::iterator iter = data.begin(); iter != data.end(); ++iter) {
            json points = iter.value();
            std::tuple<int, int> x = points.get<std::tuple<int, int>>();
            std::cout << "(" << std::get<0>(x) << " x " << std::get<1>(x) << ")" << "\n";
        }
        f.close();
}

int main() {
	getJson();
}