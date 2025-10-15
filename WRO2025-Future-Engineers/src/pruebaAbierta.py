from astro import Astro
import serial
import time

SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE   = 115200


DISCR_DIST  = 3
REDIR_ANGLE = 6


try:
	ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
	time.sleep(2)  # Waiting for Arduino to restart
	
	

	def sensor_comm(command):

		ser.write((command + "\n").encode('utf-8'))

		tiempo_espera = 0.7 
		inicio = time.time()

		while True:
			if ser.in_waiting > 0:
				respuesta = ser.readline().decode("utf-8", errors="ignore").strip()
				return respuesta
			if time.time() - inicio > tiempo_espera:
				break
				
		return "0"
				
				
	def to_nums_rgb(arg):
		try:
			parts = arg.split('-')
			return int(parts[0]), int(parts[1]), int(parts[2])
		except (IndexError, ValueError):
			return 0, 0, 0
		
	
	
	# main
	
	bot = Astro()
	line_count = 0
	
	bot.stop()
	time.sleep(5)
	
	while True:
		
		bot.forward(50)
		
		
		# Redirecting
		
		left_dist  = int(sensor_comm("ub"))
		right_dist = int(sensor_comm("uf"))
		
		if left_dist >= right_dist + DISCR_DIST:
			bot.set_dir_servo_angle(-REDIR_ANGLE)
		elif right_dist >= left_dist + DISCR_DIST:
			bot.set_dir_servo_angle(REDIR_ANGLE)
		else:
			bot.set_dir_servo_angle(0)
			
			
		# Line counting
		
		r, g, b = to_nums_rgb(sensor_comm("c"))
		
		if min(r,min(g,b)) == r and r <= min(g,b):
			line_count += 1
			bot.set_dir_servo_angle(20)
			time.sleep(2.5)
			bot.set_dir_servo_angle(0)
		
			
		
		
		if line_count >= 12:
			time.sleep(3)
			break
			
			
	bot.stop()
	
	
				
				

except serial.SerialException as e:
	print(f"ERROR al abrir el puerto: {e}")
except KeyboardInterrupt:
	print("\nLectura detenida por el usuario.")
finally:
	if 'ser' in locals() and ser.is_open:
		ser.close()
