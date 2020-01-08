import RPi.GPIO as gpio
import time

echo = 37
trig = 5

gpio.setmode(gpio.BCM)

gpio.setup(echo, gpio.IN)
gpio.setup(trig, gpio.OUT)
try:
    gpio.output(trig, False)
    time.sleep(0.1)
    gpio.output(trig, True)
    time.sleep(0.0001)
    gpio.output(trig, False)
    
    start = 0
    end = 0
    print(1)

    while gpio.input(echo) == 0:
        start = time.time()
    
    print(2)    

    while gpio.input(echo) == 1:
        #end = time.time()
        #print(time.time())
    end = time.time()
    print(3)
    
    
    timer = end - start
    print(timer, end, start)
    dist = timer * 17150

    print("Distance is {} cm" .format(dist))

    gpio.cleanup()

except KeyboardInterrupt:
    print("\nClean up time")
    gpio.cleanup()
    
    