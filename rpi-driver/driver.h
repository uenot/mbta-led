#include <pybind11/pybind11.h>

static int createCanvasAndDraw(int x, int y, int r, int g, int b);

namespace py = pybind11;

PYBIND11_MODULE(example, mod) {
    mod.def("create_canvas_and_draw", &createCanvasAndDraw, "test desc");
}
