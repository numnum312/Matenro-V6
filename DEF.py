#Program for 摩天楼v6
"""
      ■                           ■    
 ■■■■■■■■■■■  ■■■■■■■■■■■   ■   ■ ■ ■  
 ■■  ■   ■         ■        ■   ■ ■    
 ■■■■■■■■■■■       ■       ■■■■■■■■■■■ 
 ■■ ■■  ■■■        ■        ■    ■■■   
 ■■■ ■ ■ ■ ■   ■■■■■■■■■    ■■ ■■ ■ ■■ 
 ■■  ■ ■■■■        ■       ■■■■  ■     
 ■     ■          ■ ■      ■■ ■■■■■■■■ 
 ■ ■■■■■■■■■      ■ ■■    ■ ■   ■■  ■  
 ■■■■■■■■■■■     ■   ■■     ■   ■■ ■   
 ■     ■       ■■     ■■■   ■     ■■■  
     ■■■      ■■            ■  ■■■  ■■ 
"""


import machine
from machine import PWM,Pin,ADC
import ssd1306
import utime
import math

#####variables#####################
#LCD
LCD_FLAG = True
try:
    lcd = machine.I2C(1,sda=machine.Pin(18),scl=machine.Pin(19),freq=400000)
    display = ssd1306.SSD1306_I2C(128,64,lcd)
except:
    print("LCD connect error")
    LCD_FLAG = False

#motor
PWM_FREQ = 1700
motor = PWM(Pin(9,Pin.OUT))
motor.freq(PWM_FREQ) #PWM frequency set to 1700 Hz

#Variable resistance
resister = ADC(Pin(26))
resisterVoltage = 0

#temperature sensor
temp_sensor = ADC(4)
convert_num = 3.3 / 65535
temp_ans = 0

#LED
led = Pin(25,Pin.OUT)
led1 = Pin(10,Pin.OUT)
led2 = Pin(11,Pin.OUT)

led.value(1)
led2.value(1)
led1.value(1)

#####################################
#sin wave animation
y = []
A = 0
x = list(range(33))

#motor control
duty_value = 0
send_duty_num = None

#####################################

#main function
def init():
    if LCD_FLAG:
        display.fill(1)
        display.show()
        utime.sleep(1.2)
        init_screen()

        #init motor
        display.fill(0)
        display.text("PWM signal init...",0,0,1)
        display.show()
        utime.sleep(0.5)

        display.fill(0)
        display.text("ALL VITAL GERRN",0,0,1)
        display.text("FREQ->1700Hz",0,12,1)
        display.text("2SK4017..OK",0,24,1)
        display.text("MAIN FUNC START",0,36,1)
        display.show()
        utime.sleep(1)


def init_screen():
    if LCD_FLAG:
        display.fill(0)
        display.fill_rect(0, 0, 32, 32, 1)
        display.fill_rect(2, 2, 28, 28, 0)
        display.vline(9, 8, 22, 1)
        display.vline(16, 2, 22, 1)
        display.vline(23, 8, 22, 1)
        display.fill_rect(26, 24, 2, 4, 1)
        display.text('MicroPython', 40, 0, 1)
        display.text('SSD1306', 40, 12, 1)
        display.text('INITED....', 40, 24, 1)
        display.show()
        utime.sleep(2)

def readResisterVol(): #read variable resister and calc duty value
    global duty_value
    global resisterVoltage
    resister_value = resister.read_u16() #read Variable resistance
    voltage = (resister_value / (65535*3.2))*10 #V
    resisterVoltage = voltage
    
    #set duty value
    duty_value = (voltage / 3.2)

def turnMotor(): #control motor
    global duty_value
    global send_duty_num
    duty = int(duty_value * 65536)
    send_duty_num = duty
    motor.duty_u16(duty)

def readTemp():
    global temp_sensor
    global convert_num
    global temp_ans
    read = temp_sensor.read_u16() * convert_num
    temp = 27 - ((read - 0.706) / 0.001721 ) - 3
    temp_ans = int(temp)

def mainRoopLCD():
    if LCD_FLAG:
        display.fill(0)

        showInfo()
        sinWaveGraph()

        display.show()

def showInfo():
    global send_duty_num
    global duty_value
    global resisterVoltage
    global temp_ans

    send_duty_num = duty_value
    duty_percent = math.floor(send_duty_num*100)

    duty_per_str = "DUTY%->" + str(duty_percent) + "%"
    duty_str = "Duty->" + str(send_duty_num)
    resister_str = "Rvol->" + str(math.floor(resisterVoltage)) + "V"
    temp_str = "CPU TEMP->" + str(math.floor(temp_ans)) + " C"

    if LCD_FLAG:
        display.text(duty_per_str,40,0,1)
        display.text(duty_str,40,12,1)
        display.text(resister_str,40,24,1)
        display.text(temp_str,0,40,1)
        display.text("PWM ->1700Hz",0,52,1)


def sinWaveGraph():
    if LCD_FLAG:
        global A
        display.fill_rect(0, 0, 33, 33, 1)
        display.fill_rect(2, 2, 30, 30, 0)
        for i in range(33):
                ans = 16*math.sin((2*math.pi*(i/32))-A) + 16
                y.append(round(ans))

        for i in range(31):
            display.line(x[i],y[i],x[i+1],y[i+1],1)

        if A <=6.3:
            A+= 0.04
        else:
            A = 0
        y.clear()