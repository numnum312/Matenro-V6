from machine import PWM
from machine import ADC
from machine import Pin
import utime

#とりあえずモーター動かす
print("program start")

#GPIO12番をPWM出力Pinに設定
motor = PWM(Pin(9,Pin.OUT))
#可変抵抗を26版pinに設定
resister = ADC(Pin(26))

#周波数を設定
motor.freq(1500)  #10000Hzに設定

while True:
#モーター回転
    duty_value = 1 #duty比50%で駆動
    resister_value = resister.read_u16()

    voltage = (resister_value / (65535*3.2))*10

    duty_value = (voltage / 3.2)
    
    duty = int(duty_value * 65536)
    motor.duty_u16(duty)

    utime.sleep(0.01)

    print("duty -> ",duty)