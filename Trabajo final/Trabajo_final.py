# Trabajo Final Lenguajes de programación 2023
# Control de una red API con XBee
# Jacobo Chica Quintero
# Sara Alvarez
# Juan Diego Agudelo

#Librerias
from digi.xbee.devices import XBeeDevice
from digi.xbee.io import IOLine, IOMode
import time



# Variables
port = "COM8"
vel = 9600

id_sensor ="sensor"
id_motor ="motor"
id_ledsw ="ledsw"

sensor = IOLine.DIO0_AD0

motor_der = IOLine.DIO2_AD2
motor_izq = IOLine.DIO1_AD1
motor_pwm = IOLine.DIO11_PWM1

led = IOLine.DIO2_AD2
sw = IOLine.DIO0_AD0

estado = 0

print(" +------------------------------------------------+")
print(" | Control de los actuadores con XBee en modo API |")
print(" +------------------------------------------------+\n")

time.sleep(1)

while True:

    if estado == 0: # Estado 0
        aux = 0
        print(" Estado inicial \n")
        time.sleep(1)
        print(" Indique que acción desea realizar \n")
        time.sleep(1)
        print("     1: Lectura del sensor")
        print("     2: Girar motor derecha")
        print("     3: Girar motor izquierda")
        print("     4: Detener motor")
        print("     5: Encender led")
        print("     6: Apagar led")
        print("     7: Posición swiche \n")

        aux = input("Elija una de las opciones \n")
        sig_estado = int(aux)

        if sig_estado >= 1 and sig_estado <= 7:
            estado = sig_estado
        else:
            print("Seleccione un numero del 1 al 7 \n")
            time.sleep(3)
            
        
    
    if estado == 1: # Estado 1

        print("Estado: lectura del sensor \n")
        time.sleep(1)

        xb_local = XBeeDevice(port, vel)
        xb_local.open()
        xb_net = xb_local.get_network()
        xb_rem_sen = xb_net.discover_device(id_sensor)

        if xb_rem_sen is None:
            print("No se encuentra la XBee del sensor \n")
            estado = 0
            xb_local.close()

        else:
           xb_rem_sen.set_io_configuration(sensor, IOMode.ADC)
           valor_sen = xb_rem_sen.get_adc_value(sensor)
           print("Temperatura: ", valor_sen, "\n")
           time.sleep(3)
           xb_local.close()
           estado = 0

    if estado == 2: # Estado 2
        print("Estado: Girar motor derecha \n")
        time.sleep(1)
        xb_local = XBeeDevice(port, vel)
        xb_local.open()
        xb_net = xb_local.get_network()
        xb_rem_mot = xb_net.discover_device(id_motor)
        if xb_rem_mot is None:
            print("No se encuentra la XBee del motor \n")
            xb_local.close()
            estado = 0
        else:
           xb_rem_mot.set_io_configuration(motor_der, IOMode.DIGITAL_OUT_HIGH)
           xb_rem_mot.set_io_configuration(motor_izq, IOMode.DIGITAL_OUT_LOW)
           pwm_aux = input("Escoja el porcentaje del PWM (1 al 100)")
           pwm = int(pwm_aux)
           if pwm >= 1 and pwm <= 100:
               xb_rem_mot.set_pwm_duty_cycle(motor_pwm, pwm)
               time.sleep(2)
               xb_local.close()
               estado = 0
           else:
               print("Seleccione un numero entero del 1 al 100")
               
               

    
    if estado == 3: # Estado 3
        print("Estado: Girar motor izquierda \n")
        time.sleep(1)
        xb_local = XBeeDevice(port, vel)
        xb_local.open()
        xb_net = xb_local.get_network()
        xb_rem_mot = xb_net.discover_device(id_motor)
        if xb_rem_mot is None:
            print("No se encuentra la XBee del motor \n")
            xb_local.close()
            estado = 0
        else:
           xb_rem_mot.set_io_configuration(motor_der, IOMode.DIGITAL_OUT_LOW)
           xb_rem_mot.set_io_configuration(motor_izq, IOMode.DIGITAL_OUT_HIGH)
           pwm_aux = input("Escoja el porcentaje del PWM (1 al 100)")
           pwm = int(pwm_aux)
           if pwm >= 1 and pwm <= 100:
               xb_rem_mot.set_pwm_duty_cycle(motor_pwm, pwm)
               time.sleep(2)
               xb_local.close()
               estado = 0
           else:
               print("Seleccione un numero entero del 1 al 100")
               

    if estado == 4: # Estado 4

        print("Estado: Detener motor \n")
        time.sleep(1)

        xb_local = XBeeDevice(port, vel)
        xb_local.open()
        xb_net = xb_local.get_network()
        xb_rem_mot = xb_net.discover_device(id_motor)

        if xb_rem_mot is None:
            print("No se encuentra la XBee del motor \n")
            xb_local.close()
            estado = 0
        else:
           xb_rem_mot.set_io_configuration(motor_der, IOMode.DIGITAL_OUT_LOW)
           xb_rem_mot.set_io_configuration(motor_izq, IOMode.DIGITAL_OUT_LOW)

           time.sleep(2)
           xb_local.close()
           estado = 0
           

    
    if estado == 5: # Estado 5

        print("Estado: Encender led \n")
        time.sleep(1)

        xb_local = XBeeDevice(port, vel)
        xb_local.open()
        xb_net = xb_local.get_network()
        xb_rem_led = xb_net.discover_device(id_ledsw)

        if xb_rem_led is None:
            print("No se encuentra la XBee del led \n")
            xb_local.close()
            estado = 0
        
        else:
            xb_rem_led.set_io_configuration(led, IOMode.DIGITAL_OUT_HIGH)
            xb_local.close()
            estado = 0


    if estado == 6: # Estado 6

        print("Estado: Apagar led \n")
        time.sleep(1)

        xb_local = XBeeDevice(port, vel)
        xb_local.open()
        xb_net = xb_local.get_network()
        xb_rem_led = xb_net.discover_device(id_ledsw)

        if xb_rem_led is None:
            print("No se encuentra la XBee del led \n")
            xb_local.close()
            estado = 0
        
        else:
            xb_rem_led.set_io_configuration(led, IOMode.DIGITAL_OUT_LOW)
            xb_local.close()
            estado = 0

    
    if estado == 7: # Estado 7

        print("Estado: Posicion swiche \n")
        time.sleep(1)

        xb_local = XBeeDevice(port, vel)
        xb_local.open()
        xb_net = xb_local.get_network()
        xb_rem_led = xb_net.discover_device(id_ledsw)

        if xb_rem_led is None:
            print("No se encuentra la XBee del swiche \n")
            xb_local.close()
            estado = 0

        else:
            xb_rem_led.set_io_configuration(sw, IOMode.DIGITAL_IN)
            sw_estado = xb_rem_led.get_dio_value(sw)
            print("La posicion del swiche es: ", sw_estado, "\n")
            time.sleep(1)
            xb_local.close()
            estado = 0



            









