#  This is example is for the SparkFun Serial LCD displays.
#  SparkFun sells these at its website: www.sparkfun.com
#  Do you like this library? Help support SparkFun. Buy a board!
#  https://www.sparkfun.com/products/14072
#  https://www.sparkfun.com/products/14073
#  https://www.sparkfun.com/products/14074

"""
 Serial LCD Example 2 - example2_backlight.py
 Written by Gaston Williams, July 14th, 2019
 Based on Arduino code written by Gaston Williams and
 Nathan Seidle @ Sparkfun, August 22, 2018.


 Example 2 - Backlight:
 This program changes the backlight of the display through a cycle
 of colors by setting the red, green and blue values individually.
 This example works with the original version of SerLCD. See
 Example 13 FastBacklight for version 1.1 and later.
"""
from time import sleep
import board
from sparkfun_serlcd  import Sparkfun_SerLCD_I2C

i2c = board.I2C()
serlcd = Sparkfun_SerLCD_I2C(i2c)

print("Example 2: Backlight.")
print("Press Ctrl-C to end program.")

try:
    while True:
        serlcd.set_backlight_rgb(0, 0, 0) # black is off
        serlcd.clear()
        serlcd.write("Black (off)")
        sleep(3)

        serlcd.set_backlight_rgb(255, 0, 0) #bright red
        serlcd.clear()
        serlcd.write("Red")
        sleep(3)

        serlcd.set_backlight(0xFF8C00) #orange
        serlcd.clear()
        serlcd.write("Orange")
        sleep(3)

        serlcd.set_backlight_rgb(255, 255, 0) #bright yellow
        serlcd.clear()
        serlcd.write("Yellow")
        sleep(3)

        serlcd.set_backlight_rgb(0, 255, 0) #bright green
        serlcd.clear()
        serlcd.write("Green")
        sleep(3)

        serlcd.set_backlight_rgb(0, 0, 255) #bright blue
        serlcd.clear()
        serlcd.write("Blue")
        sleep(3)

        serlcd.set_backlight(0x4B0082) #indigo, a kind of dark purplish blue
        serlcd.clear()
        serlcd.write("Indigo")
        sleep(3)

        serlcd.set_backlight(0xA020F0) #violet
        serlcd.clear()
        serlcd.write("Violet")
        sleep(3)

        serlcd.set_backlight(0x808080) #grey
        serlcd.clear()
        serlcd.write("Grey")
        sleep(3)

        serlcd.set_backlight_rgb(255, 255, 255) #bright white
        serlcd.clear()
        serlcd.write("White")
        sleep(3)

except KeyboardInterrupt:
    pass
