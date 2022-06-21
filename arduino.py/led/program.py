from pyfirmata import Arduino, util
import time

uno = Arduino('COM5')

while True:
    uno.digital[12].write(1)
    print('LED LIGADO')
    time.sleep(0.5)
    uno.digital[12].write(0)
    print('LED DESLIGADO')
    time.sleep(1)
