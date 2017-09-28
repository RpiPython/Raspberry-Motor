# Importar librerias necesarias
import RPi.GPIO as GPIO
import time

#Configuracion de los puertos
GPIO.setmode(GPIO.BCM)

	# Puertos de salida
GPIO.setup(17, GPIO.OUT) # Este va ser el PWM
GPIO.setup(27, GPIO.OUT) # Puerto de direccion del motor
GPIO.setup(22,GPIO.OUT) # Puerto de direcion del motor
	# Puertos de entrada
GPIO.setup(18,GPIO.IN) # Puerto de parada
GPIO.setup(23,GPIO.IN) # Aumentar velocidad
GPIO.setup(24,GPIO.IN) # Reducir velocidad

	# Redefinir Variables
P1 = 27
P2 = 22
Paro = 18
Up = 23
Down = 24

	# Variables necesarias para el proceso
	
x = 10 # Variable de incrementar o decrementar
y = 100 # Velocidad acutal

	# Inicializar el motor a maxima potencia

PWM = GPIO.PWM(17,100) # Se inicializa el PWM con 100  pulsos por seg
PWM.start(y) # Arrancamos el motor a maxima potencia

	# Inicializar el loop infinito

while (GPIO.input(Paro) == GPIO.LOW): # El programa no finaliza hasta que se pulse el boton
		
		if (GPIO.input(Up)==GPIO.LOW): # Incrementar la velocidad
			y = y + x
			if (y > 100):
				y = 100

			PWM.ChangeDutyCycle(y)

		if (GPIO.input(Down)==GPIO.LOW): # Decrementa la velocidad
			y = y - x
			if (y < 0):
				y = 0

			PWM.ChangeDutyCycle(y)
	 	time.sleep(0.5) # Frecuencia con la que se comprueba los botones	

# Salida del cilco infinito


GPIO.cleanup()

# Fin del programa		
