# Circuit Playground Temperature
# Reads the on-board temperature sensor and prints the value
import time
from adafruit_circuitplayground import cp


while True:
    temp_c = cp.temperature
    temp_f = cp.temperature * 9 / 5 + 32
    if temp_c>35:
        print("Risk of wildfire in area")
        cp.play_tone(4000, 1)

    else:
        print("Temperature : %f C / %f F, No risk of Fire" % (temp_c, temp_f))

    time.sleep(0.25)