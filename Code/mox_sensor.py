# I2C has to be active on Pi to work with this

""" 
Install Commands:
pip3 install adafruit-blinka
pip3 install adafruit-circuitpython-ens160
"""

# IMPORTS
import time
import board
import adafruit_ens160

# INIT I2C BUS
i2c = board.I2C()
ens = adafruit_ens160.ENS160(i2c)

# PRINT SENSOR DATA
while True:
    print("AQI:", ens.aqi)
    print("TVOC: {} ppb".format(ens.tvoc))
    print("eCO2: {} ppm".format(ens.eco2))
    print("-" * 20)
    time.sleep(1)
