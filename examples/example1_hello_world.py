#  This is example is for the SparkFun Serial LCD displays.
#  SparkFun sells these at its website: www.sparkfun.com
#  Do you like this library? Help support SparkFun. Buy a board!
#  https://www.sparkfun.com/products/14072
#  https://www.sparkfun.com/products/14073
#  https://www.sparkfun.com/products/14074

"""
 Serial LCD Example 1 - example1_hello_world.py
 Written by Gaston Williams, July 16, 2019
 Based on Arduino code written by Gaston Williams and
 Nathan Seidle @ Sparkfun, August 22, 2018.


 Example 1 - Hello World:
 This program writes Hello, World! to the display,
 then displays a count on the next line.
"""
from time import sleep
import board

# Enable I2C communication
from sparkfun_serlcd import Sparkfun_SerLCD_I2C

i2c = board.I2C()
serlcd = Sparkfun_SerLCD_I2C(i2c)

# Enable SPI communication
#import digitalio
#from sparkfun_serlcd import Sparkfun_SerLCD_SPI
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#
# Set up chip select, CE0 or D8 is labeled CS on Sparkfun Pi Hat
#cs = digitalio.DigitalInOut(board.CE0)
#cs.direction = digitalio.Direction.OUTPUT
#
#serlcd = Sparkfun_SerLCD_SPI(spi, cs)

# Enable UART Serial communication
# SerLCD is connected to the RPi via a USB to TTL 3.3v Serial Cable:
# https://www.sparkfun.com/products/12977
# https://www.adafruit.com/product/954

#import serial
#from sparkfun_serlcd import Sparkfun_SerLCD_UART
#usb0 = serial.Serial(
#        port='/dev/ttyUSB0',
#        baudrate = 9600,
#        parity=serial.PARITY_NONE,
#        stopbits=serial.STOPBITS_ONE,
#        bytesize=serial.EIGHTBITS,
#        timeout=1)
#
#serlcd = Sparkfun_SerLCD_UART(usb0)

print('Example 1: Hello World')
print('Press Ctrl-C to end program.')

serlcd.write("Hello, world!")

i = 0
try:
    while True:
        serlcd.set_cursor(0,1)
        serlcd.write(i)
        i += 1
        sleep(1)

except KeyboardInterrupt:
    pass
