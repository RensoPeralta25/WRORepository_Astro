from robot_hat import Pin
import time
import os

button = Pin("SW", Pin.IN, Pin.PULL_UP)   # Botón USR (GPIO25)
led = Pin(26, Pin.OUT)                    # LED (GPIO26)

# Ruta del archivo que quieres ejecutar
script_path = "/home/admin/Documents/pruebaAbierta1.py"

while True:
    if button.value() == 1:  # Presionado
       led.on()
        os.system(f"python3 {script_path}")  # Ejecuta el otro script
        time.sleep(0.5)  # Evita que se repita por rebote
    else:
        led.off()
    time.sleep(0.1)
