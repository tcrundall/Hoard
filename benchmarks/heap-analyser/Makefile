include ../Makefile.inc

TARGET = heap-analyser 

$(TARGET): heap-analyser.cpp
	$(CXX) $(CXXFLAGS) heap-analyser.cpp -o $(TARGET) -lpthread

clean:
	rm -f $(TARGET)
