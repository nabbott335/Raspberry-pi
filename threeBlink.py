import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(21, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(18, gpio.OUT)
i = 0
while i < 5:
    gpio.output(21, True)
    time.sleep(2)
    gpio.output(11, True)
    gpio.output(21, False)
    time.sleep(2)
    gpio.output(18, True)
    gpio.output(11, False)
    time.sleep(2)
    gpio.output(18, False)
    i += 1
    
gpio.cleanup()

    
