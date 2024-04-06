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
"""
#                    _  __ _           _   _             
#___ _ __   ___  ___(_)/ _(_) ___ __ _| |_(_) ___  _ __  
/ __| '_ \ / _ \/ __| | |_| |/ __/ _` | __| |/ _ \| '_ \ 
\__ \ |_) |  __/ (__| |  _| | (_| (_| | |_| | (_) | | | |
|___/ .__/ \___|\___|_|_| |_|\___\__,_|\__|_|\___/|_| |_|
    |_|                                                  
Real-time information display by LCD
Stepless regulation using variable resistors
PWM speed control using MOSFETs
"""

import machine
import utime
import DEF


def main():
    print("main program start")
    DEF.init()

    #main roop
    while True:
        #resister calc duty value
        DEF.readResisterVol()
        #turn motor
        DEF.turnMotor()
        #read CPU temp
        DEF.readTemp()
        #show info on LCD
        DEF.mainRoopLCD()


if __name__ == "__main__":
    main()