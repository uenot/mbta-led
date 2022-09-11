CXXFLAGS=-O3
OBJECTS=driver.o
BINARIES=driver
LIBS=driver.so

RGB_LIB_DISTRIBUTION=matrix
RGB_INCDIR=$(RGB_LIB_DISTRIBUTION)/include
RGB_LIBDIR=$(RGB_LIB_DISTRIBUTION)/lib
RGB_LIBRARY_NAME=rgbmatrix
RGB_LIBRARY=$(RGB_LIBDIR)/lib$(RGB_LIBRARY_NAME).a
LDFLAGS+=-L$(RGB_LIBDIR) -l$(RGB_LIBRARY_NAME) -lrt -lm -lpthread

PYBIND_LIB=$(shell python3 -m pybind11 --includes)

driver.so:
	c++ -O3 -Wall -shared -std=c++11 -fPIC $(LDFLAGS) -I$(RGB_INCDIR) $(PYBIND_LIB) $(RGB_LIBRARY) driver.h  driver.cpp -o driver.so

$(RGB_LIBRARY):
	$(MAKE) -C $(RGB_LIBDIR)

driver: $(OBJECTS) $(RGB_LIBRARY)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $@ $(LDFLAGS)

driver.o: driver.cpp
	$(CXX) -I$(RGB_INCDIR) $(PYBIND_LIB) $(CXXFLAGS) -c -o $@ $<

clean:
	rm -f $(OBJECTS) $(BINARIES) $(LIBS)
