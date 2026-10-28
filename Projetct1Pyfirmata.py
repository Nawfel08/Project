from pyfirmata import Arduino
import time

# Connexion à la carte Arduino
board = Arduino('COM3')  # Remplace COM3 par ton port Arduino

# Association des broches aux LED
led_e = board.get_pin('d:2:o')
led_d = board.get_pin('d:3:o')
led_c = board.get_pin('d:4:o')
led_b = board.get_pin('d:5:o')
led_a = board.get_pin('d:6:o')
led_f = board.get_pin('d:7:o')
led_g = board.get_pin('d:8:o')

led_0 = {led_a,led_b,led_c,led_d,led_e,led_f}
led_1 = {led_b,led_c}
led_2 = {led_a,led_b,led_g,led_e,led_d}
led_3 = {led_a,led_b,led_g,led_c,led_d}
led_4 = {led_f,led_g,led_b,led_c}
led_5 = {led_a,led_f,led_g,led_c,led_d}
led_6 = {led_a,led_f,led_g,led_c,led_d,led_e}
led_7 = {led_a,led_b,led_c}
led_8 = {led_a,led_b,led_c,led_d,led_e,led_f,led_g}
led_9 = {led_a,led_b,led_c,led_d,led_f,led_g}

try:
    while True:
        #allumer les led de 1 à 9
        for led in [led_0, led_1, led_2, led_3, led_4, led_5, led_6, led_7, led_8, led_9]:
            for pin in led:
                pin.write(1)
            time.sleep(1)
            for pin in led:
                pin.write(0)
            time.sleep(0.5)


except KeyboardInterrupt:
    for led in [led_0, led_1, led_2, led_3, led_4, led_5, led_6, led_7, led_8, led_9]:
        for pin in led:
            pin.write(0)

    board.exit()