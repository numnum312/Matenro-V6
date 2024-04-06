#10kΩ可変抵抗を使用
#電圧最低値 0.00119Vほぼ0です
#電圧最大値3.03V ほぼ3.0V

#duty 0<duty<255

from machine import ADC,Pin
import utime

resister = ADC(Pin(26))

while True:
    resister_value = resister.read_u16()

    voltage = (resister_value / (65535*3.2))*10

    duty = int(255 * (voltage / 3.2))

    print("Resister Value -> ",voltage)
    print("voltage % -> ",(voltage / 3.2)*100)
    print("duty->",duty)

    utime.sleep(0.5)