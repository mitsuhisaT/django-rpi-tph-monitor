
TARGET=bme280i2c
O=main.o BME280I2C.o
H=BME280I2C.h

$(TARGET) : $(O) $(H)
	g++ -o $(TARGET) $(O) -I/usr/local/include -L/usr/local/lib -lwiringPi

.SUFFIXES:.o .cpp
.cpp.o:
	g++ -c $<

.PHONY:clean
clean:
	rm -f $(TARGET)
	rm -f $(O)
