from astro import Astro
import serial
import time
import cv2
from picamera2 import Picamera2

SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE   = 9600


DISCR_DIST  = 3
REDIR_ANGLE = 40
CENTER = 70

MAX_ANGLE = 40

picam2 = Picamera2()

# Configura la resolución que quieras; aquí un preview razonable
config = picam2.create_preview_configuration({"size": (640, 480)})
picam2.configure(config)

picam2.start()
time.sleep(0.2) 

def constrain(x, mn, mx):
    return max(mn, min(mx, x))

try:
	ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
	time.sleep(2)  # Waiting for Arduino to restart

	def sensor_comm(command):

		ser.write((command + "\n").encode('utf-8'))
		
		#if command.isnumeric():
		#	return "0"

		#tiempo_espera = 0.7
		#inicio = time.time()

		#while True:
		#	if ser.in_waiting > 0:
		#		respuesta = ser.readline().decode("utf-8", errors="ignore").strip()
		#		return respuesta
		#	if time.time() - inicio > tiempo_espera:
		#		break
				
		#return "0"
				
				
	def to_nums_rgb(arg):
		try:
			parts = arg.split('-')
			return int(parts[0]), int(parts[1]), int(parts[2])
		except (IndexError, ValueError):
			return 0, 0, 0
			
			
	def read_vals():
		linea = ser.readline().decode().strip()
		usl_str, usr_str, r_str, g_str, b_str = linea.split("|")
		return float(usl_str), float(usr_str), float(r_str), float(g_str), float(b_str)
		
	def leer_datos():
		linea = ser.readline().decode().strip()
		print(linea)
		if "|" in linea:
			usl_str, usr_str, r_str, g_str, b_str = linea.split("|")
			
			if usl_str == "":
				usl_str = "0.0"
			
			usl = float(usl_str)
			usr = float(usr_str)
			r = float(r_str)
			g = float(g_str)
			b = float(b_str)
			return usl, usr, r, g, b
		return None
		
		
		
	def leer_datos2(timeout_seconds=1.0):
		start = time.time()
		while True:
			linea = ser.readline().decode(errors="ignore").strip()
			if not linea:
				if time.time() - start > timeout_seconds:
					raise ValueError("Timeout: no llegaron datos por serial")
				continue

			print("RAW:", linea)  # útil para depuración

			if "|" not in linea:
				# línea no en el formato esperado -> seguir leyendo
				if time.time() - start > timeout_seconds:
					raise ValueError(f"Línea mal formada: {linea!r}")
				continue

			# split correctamente
			partes = [p.strip() for p in linea.strip("|").split("|")]

			# eliminar campos vacíos (si quieres mantener vacío, quita el filtro)
			partes = [p for p in partes if p != ""]

			# rellenar con ceros si faltan campos
			while len(partes) < 5:
				partes.append("0")

			usl_str, usr_str, r_str, g_str, b_str = partes[:5]

			try:
				usl = float(usl_str)
				usr = float(usr_str)
				r = float(r_str)
				g = float(g_str)
				b = float(b_str)
				return usl, usr, r, g, b
			except ValueError:
				# conversión falló; intentar siguiente línea (o lanzar si timeout)
				if time.time() - start > timeout_seconds:
					raise
				continue
	
	def leer_datos3(timeout_seconds=1.0):
 
		start = time.time()

		while True:
			linea = ser.readline().decode(errors="ignore").strip()

			# Si no llegó nada, esperar hasta timeout
			if not linea:
				if time.time() - start > timeout_seconds:
					raise ValueError("Timeout: no llegaron datos por serial")
				continue

			# Verificar separador
			if "|" not in linea:
				if time.time() - start > timeout_seconds:
					raise ValueError(f"Línea mal formada: {linea!r}")
				continue

			# Dividir en partes
			partes = linea.split("|")

			# Rellenar si faltan datos
			while len(partes) < 5:
				partes.append("0")

			# Tomar solo 5
			usl_str, usr_str, r_str, g_str, b_str = partes[:5]

			try:
				usl = float(usl_str)
				usr = float(usr_str)
				r   = float(r_str)
				g   = float(g_str)
				b   = float(b_str)
				return usl, usr, r, g, b
			except ValueError:
				# línea con valores no convertibles
				if time.time() - start > timeout_seconds:
					raise
				continue
	
	
	# main
	
	bot = Astro()
	line_count = 0
	
	bot.stop()
	time.sleep(5)
	
	last_l = 0
	last_r = 0
	
	real_l = 0
	real_r = 0
			
	left_dist, right_dist, r, g, b = leer_datos3()
	Sum_Initial = left_dist+right_dist
	
	while True:
		
		bot.forward(90)
		
		# Redirecting
		
		left_dist, right_dist, r, g, b = leer_datos3()
		
		
		
		img = picam2.capture_array()
		img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
		cv2.imshow("CSI Camera (Picamera2 -> OpenCV)", img_bgr)
		
	
		
		Sum_Temp = left_dist+right_dist
		print(f"Distancia izquierda: {left_dist}")
		print(f"Distancia izquierda: {right_dist}")
		print(f"Sumatoria Inicial: {Sum_Initial}")
		print(f"Sumatoria: {Sum_Temp}")
		
		
		
		if(Sum_Temp-10<Sum_Initial):
			sensor_comm(str(constrain(CENTER+float(left_dist-right_dist)*(float(MAX_ANGLE)/30),CENTER-MAX_ANGLE,CENTER+MAX_ANGLE)))
		elif(Sum_Temp-10>Sum_Initial):
			sensor_comm(str(constrain(CENTER+float(left_dist+right_dist)*(float(MAX_ANGLE)/30),CENTER-MAX_ANGLE,CENTER+MAX_ANGLE)))
		else:
			sensor_comm("70")
			
		
		'''
		
		
		print(left_dist)
		print(right_dist)
		print("")
		
		real_l = left_dist
		if (abs(last_l-left_dist)>10):
			real_l = last_l
		real_r = right_dist
		if (abs(last_r-right_dist)>10):
			real_r = last_r
		
		if abs(left_dist-right_dist < 40):
			sensor_comm(str(constrain(CENTER+float(real_l-real_r)*(float(MAX_ANGLE)/20),CENTER-MAX_ANGLE,CENTER+MAX_ANGLE)))
		else:
			sensor_comm(str(constrain(CENTER+float(real_l-real_r)*(float(50)/20),CENTER-50,CENTER+50)))
			
		# Line counting
		
		if min(r,min(g,b)) == r and r < min(g,b):
			line_count += 1
			#sensor_comm(str(CENTER-REDIR_ANGLE))
			#time.sleep(3)
			#sensor_comm(str(CENTER))
			
		
		
		#if line_count >= 12:
			#time.sleep(3)
			#break
			
		last_l = left_dist
		last_r = right_dist
			
			'''
	bot.stop()
	
	
				
				

except serial.SerialException as e:
	print(f"ERROR al abrir el puerto: {e}")
except KeyboardInterrupt:
	print("\nLectura detenida por el usuario.")
finally:
	if 'ser' in locals() and ser.is_open:
		ser.close()
	picam2.stop()
	cv2.destroyAllWindows()
