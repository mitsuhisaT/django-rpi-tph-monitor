
TARGET=lcd
O=main.o LCDAQM.o
H=LCDAQM.h

$(TARGET) : $(O) $(H)
	g++ -o $(TARGET) $(O) -I/usr/local/include -L/usr/local/lib -lwiringPi

.SUFFIXES:.o .cpp
.cpp.o:
	g++ -c $<

.PHONY:clean
clean:
	rm -f $(TARGET)
	rm -f $(O)
