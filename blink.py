import utime
from machine import Pin

print("pprogram start")

led = Pin(25,Pin.OUT)
led1 = Pin(10,Pin.OUT)
led2 = Pin(11,Pin.OUT)


while True:
    led.value(1)
    led2.value(1)
    led1.value(1)
    print(utime.time())
    utime.sleep(0.1)
    led.value(0)
    led2.value(0)
    led1.value(0)
    utime.sleep(0.1)