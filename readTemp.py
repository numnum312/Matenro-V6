from machine import I2C, Pin, ADC
import ssd1306
import utime

# 内蔵温度センサーのピン
TEMP_SENSOR_PIN = 4

# SSD1306の設定
WIDTH = 128
HEIGHT = 64
i2c = I2C(1, sda=Pin(18), scl=Pin(19), freq=400000)
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# 温度センサーの設定
sensor_temp = ADC(TEMP_SENSOR_PIN)
conversion_factor = 3.3 / (65535)

def read_temperature():
    raw_value = sensor_temp.read_u16()
    temperature = 27 - (raw_value - 0.706) / 0.001721
    return temperature

def draw_graph(value):
    oled.fill(0)  # 画面をクリア
    oled.text("Temperature:", 0, 0)
    oled.text("{:.2f} C".format(value), 0, 20)

    # グラフの描画
    bar_height = int(value * (HEIGHT - 30) / 100)  # バーの高さ
    oled.rect(0, 30, WIDTH, HEIGHT - 30, 1)  # 枠
    oled.fill_rect(0, HEIGHT - bar_height, WIDTH, bar_height, 1)  # バー

    oled.show()

while True:
    temperature = read_temperature()
    print('Temperature:', temperature)
    draw_graph(temperature)
    utime.sleep(1)  # 1秒ごとに温度を表示（必要に応じて変更）
