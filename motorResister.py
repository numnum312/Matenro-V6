#とりあえず可変抵抗の値を見てduty調整
#LCDにsin波を表示する事には成功した
#プログラムの構造を再設定してコーディングする
#LCDのUIを整える
from machine import ADC,Pin,PWM
import machine
import utime
import ssd1306
import math
import sys

resister = ADC(Pin(26))
motor = PWM(Pin(9,Pin.OUT))

i2c = machine.I2C(1,sda=machine.Pin(18),scl=machine.Pin(19),freq=400000)
try:
    print("ADDR -> ",hex(i2c.scan()[0]))
except:
    print("ADDR BUFFER LENGTH -> ",len(i2c.scan()))
    print("CONNECTING ERROR")

display = ssd1306.SSD1306_I2C(128,64,i2c)

#三角関数を描画
y = []
A = 0
x = list(range(33))

#周波数を設定
motor.freq(1500)  #10000Hzに設定

led = Pin(25,Pin.OUT)
led1 = Pin(10,Pin.OUT)
led2 = Pin(11,Pin.OUT)
led.value(1)
led2.value(1)
led1.value(1)

while True:
    display.fill(0)
    for i in range(33):
            ans = 16*math.sin((2*math.pi*(i/32))-A) + 16
            y.append(round(ans))

    for i in range(31):
        display.line(x[i],y[i],x[i+1],y[i+1],1)

    display.show()

    if A <=6.3:
        A+= 0.04
    else:
        A = 0
    y.clear()
    
    resister_value = resister.read_u16()

    voltage = (resister_value / (65535*3.2))*10

    duty_value = (voltage / 3.2)

    duty = int(duty_value * 65536)
    motor.duty_u16(duty)

    print("duty->",duty)
    

    utime.sleep(0.01)