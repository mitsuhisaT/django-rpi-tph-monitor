# [RPi TPH Monitor Rev2][rtm]  
RPi TPH Monitor Rev2 can

* control some electric devices via infrared LED
* learn infrared control command infrared receive unit
* connect [BME280][bme280] what is integrated environmental sensor
  * monitor temperature, pressure and humidity

![RPi TPH Monitor Rev2][rtmimg]  

You can buy from 
[Indoor Corgi][ids] or [Switch Science][ss].

## Sample program
Get from
[RPi TPH Monitor Rev2][rtm]

| sample code | language | about program |
|:-- |:-- |:-- |
| [bme280i2c][bme280i2c] | Python3, C++ | Display temperature, pressure and humidity get from BME280 sensor which connected P2, P3 and P4 channels. Save log use -l option. |
| [infrared][infrared] | C++ | Display received infrared command and re-send same command via infrared LEDs. Only support NEC and AEHA format. |
| [lcd][lcd] | Python3, C++ | Display characters, turn on and off LEDs and input from switches. |

-----
[rtm]: https://www.indoorcorgielec.com/products/rpi-tph-monitor-rev2/
[bme280]: https://www.bosch-sensortec.com/bst/products/all_products/bme280
[rtmimg]: https://www.indoorcorgielec.com/wp-content/uploads/products/rpi-tph-monitor-rev2/part-comment-1024x645.jpg
[ids]: https://www.indoorcorgielec.com/product/rpi-tphmonitor-rev2/
[ss]: https://www.switch-science.com/catalog/3025/
[bme280i2c]: https://www.indoorcorgielec.com/wp-content/uploads/products/rpi-tph-monitor-rev2/bme280i2c.zip
[infrared]: https://www.indoorcorgielec.com/wp-content/uploads/products/rpi-tph-monitor-rev2/infrared-sample.zip
[lcd]: https://www.indoorcorgielec.com/wp-content/uploads/products/rpi-tph-monitor-rev2/lcd.zip