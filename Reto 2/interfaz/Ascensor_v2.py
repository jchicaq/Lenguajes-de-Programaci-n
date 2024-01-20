"""
Reto #2 Control de llamado del ascensor en 4 pisos

Realizado por:
- Jacobo Chica Quintero
- Sara Alvarez Bello
- Juan Diego Agudelo
"""

# Librerias
import RPi.GPIO as IO
import time
import tkinter as tk
import threading

### Funciones interfaz ###
# Funciones para manejar los clics en los botones de abrir y cerrar puertas
def abrir_puertas():
    # Aquí puedes agregar la lógica para abrir las puertas
    print("Abriendo las puertas")

def cerrar_puertas():
    # Aquí puedes agregar la lógica para cerrar las puertas
    print("Cerrando las puertas")

# Estados
stop = 0
up = 1
down = 2
hold_up = 3
hold_down = 4
start = 5

# Entradas y salidas
piso_1 = 3
piso_2 = 4
piso_3 = 17
piso_4 = 27

boton_1up = 6
boton_2down = 13
boton_2up = 19
boton_3down = 26
boton_3up = 2
boton_4down = 22

motor_down = 15
motor_up = 14

retorno_1up = 24
retorno_2down = 25
retorno_2up = 8
retorno_3down = 7
retorno_3up = 12
retorno_4down = 16

# Variables
time_i = 0.0 # Tirmpo inicial
time_a = 0.0 # Tiempo actual
time_r = 0.0 # Tiempo relativo

piso_act = 0; # Piso actual dle ascensor

# Definicion estado incial
state = start

IO.setwarnings(False)

# Pin setup
IO.setmode(IO.BCM)

IO.setup(motor_down, IO.OUT)
IO.setup(motor_up, IO.OUT)
IO.setup(retorno_1up, IO.OUT)
IO.setup(retorno_2down, IO.OUT)
IO.setup(retorno_2up, IO.OUT)
IO.setup(retorno_3down, IO.OUT)
IO.setup(retorno_3up, IO.OUT)
IO.setup(retorno_4down, IO.OUT)
IO.setup(21, IO.OUT)

IO.setup(piso_1, IO.IN)
IO.setup(piso_2, IO.IN)
IO.setup(piso_3, IO.IN)
IO.setup(piso_4, IO.IN)
IO.setup(boton_1up, IO.IN)
IO.setup(boton_2down, IO.IN)
IO.setup(boton_2up, IO.IN)
IO.setup(boton_3down, IO.IN)
IO.setup(boton_3up, IO.IN)
IO.setup(boton_4down, IO.IN)

# Reset salidas
IO.output(motor_down, 0)
IO.output(motor_up, 0)

IO.output(retorno_1up, 0)
IO.output(retorno_2down, 0)
IO.output(retorno_2up, 0)
IO.output(retorno_3down, 0)
IO.output(retorno_3up, 0)
IO.output(retorno_4down, 0)



# Funciones

def start():
    # Variables globales
    global time_i
    global state
    global piso_act

    # Acciones
    IO.output(motor_down, 0)
    IO.output(motor_up, 0)
    
    if IO.input(piso_1) == 1:
        piso_act = 1
        jj = 0
        print("Piso actual: ", piso_act)
        state = 0
        
    elif IO.input(piso_2) == 1:
        piso_act = 2
        print("Piso actual: ", piso_act)
        state = 0
    
    elif IO.input(piso_3) == 1:
        piso_act = 3
        print("Piso actual: ", piso_act)
        state = 0
        
    if IO.input(piso_3) == 1:
        piso_act = 3
        print("Piso actual: ", piso_act)
        state = 0
    
    else:
        print("Buscando el piso mas cercano")
        while IO.input(piso_3) == 0 and IO.input(piso_2) == 0 and IO.input(piso_3) == 0 and IO.input(piso_4) == 0:
            IO.output(motor_down, 1)
            IO.output(motor_up, 0)
            
            
            

def stop():
    # Variables globales
    global time_i
    global state
    global piso_act
    estado = "stop"
    
    if piso_act == 1:
        i = 0
        while i == 0:
            
            if IO.input(boton_1up) == 1:
                IO.output(retorno_1up, 1)
                
            elif IO.input(boton_2down) == 1:
                IO.output(retorno_2down, 1)
                
            elif IO.input(boton_2up) == 1:
                IO.output(retorno_2up, 1)
                
            elif IO.input(boton_3down) == 1:
                IO.output(retorno_3down, 1)
                
            elif IO.input(boton_3up) == 1:
                IO.output(retorno_3up, 1)
                
            elif IO.input(boton_4down) == 1:
                IO.output(retorno_4down, 1)
                
            elif IO.input(retorno_1up) == 1:
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_1up, 0)
                print("Puertas cerradas")
                
            elif IO.input(retorno_2down) == 1:
                state = 1
                i = 1
                
            elif IO.input(retorno_2up) == 1:
                state = 1
                i = 1
                
                
            elif IO.input(retorno_3down) == 1:
                state = 1
                i = 1
                
            elif IO.input(retorno_3up) == 1:
                state = 1
                i = 1
                
            elif IO.input(retorno_4down) == 1:
                state = 1
                i = 1
            
    if piso_act == 2:
        i = 0
        while i == 0:
            
            if IO.input(boton_1up) == 1:
                IO.output(retorno_1up, 1)
                
            elif IO.input(boton_2down) == 1:
                IO.output(retorno_2down, 1)
                
            elif IO.input(boton_2up) == 1:
                IO.output(retorno_2up, 1)
                
            elif IO.input(boton_3down) == 1:
                IO.output(retorno_3down, 1)
                
            elif IO.input(boton_3up) == 1:
                IO.output(retorno_3up, 1)
                
            elif IO.input(boton_4down) == 1:
                IO.output(retorno_4down, 1)
                
            elif IO.input(retorno_1up) == 1:
                state = 2
                i = 1
                
            elif IO.input(retorno_2down) == 1:
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_2down, 0)
                print("Puertas cerradas")
                
            elif IO.input(retorno_2up) == 1:
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_2up, 0)
                print("Puertas cerradas")
                
            elif IO.input(retorno_3down) == 1:
                state = 1
                i = 1
                
            elif IO.input(retorno_3up) == 1:
                state = 1
                i = 1
                
            elif IO.input(retorno_4down) == 1:
                state = 1
                i = 1
                
    if piso_act == 3:
        i = 0
        while i == 0:
            
            if IO.input(boton_1up) == 1:
                IO.output(retorno_1up, 1)
                
            elif IO.input(boton_2down) == 1:
                IO.output(retorno_2down, 1)
                
            elif IO.input(boton_2up) == 1:
                IO.output(retorno_2up, 1)
                
            elif IO.input(boton_3down) == 1:
                IO.output(retorno_3down, 1)
                
            elif IO.input(boton_3up) == 1:
                IO.output(retorno_3up, 1)
                
            elif IO.input(boton_4down) == 1:
                IO.output(retorno_4down, 1)
                
            elif IO.input(retorno_1up) == 1:
                state = 2
                i = 1
                
            elif IO.input(retorno_2down) == 1:
                state = 2
                i = 1
                
            elif IO.input(retorno_2up) == 1:
                state = 2
                i = 1
                
            elif IO.input(retorno_3down) == 1:
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_3down, 0)
                print("Puertas cerradas")
                
            elif IO.input(retorno_3up) == 1:
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_3up, 0)
                print("Puertas cerradas")
                
            elif IO.input(retorno_4down) == 1:
                state = 1
                i = 1
                
    if piso_act == 4:
        i = 0
        while i == 0:
            
            if IO.input(boton_1up) == 1:
                IO.output(retorno_1up, 1)
                
            elif IO.input(boton_2down) == 1:
                IO.output(retorno_2down, 1)
                
            elif IO.input(boton_2up) == 1:
                IO.output(retorno_2up, 1)
                
            elif IO.input(boton_3down) == 1:
                IO.output(retorno_3down, 1)
                
            elif IO.input(boton_3up) == 1:
                IO.output(retorno_3up, 1)
                
            elif IO.input(boton_4down) == 1:
                IO.output(retorno_4down, 1)
                
            elif IO.input(retorno_1up) == 1:
                state = 2
                i = 1
                
            elif IO.input(retorno_2down) == 1:
                state = 2
                i = 1
                
            elif IO.input(retorno_2up) == 1:
                state = 2
                i = 1
                
            elif IO.input(retorno_3down) == 1:
                state = 2
                i = 1
                
            elif IO.input(retorno_3up) == 1:
                state = 2
                i = 1
                
            elif IO.input(retorno_4down) == 1:
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_4down, 0)
                print("Puertas cerradas")
                
def up():
    global state
    global piso_act
    print("Subiendo")
    
        
    if piso_act == 1:
        
        if IO.input(retorno_2up) == 1:
            IO.output(motor_down, 0)
            IO.output(motor_up, 1)
            j= 0
       
            while j == 0:
                
                if IO.input(piso_2) == 1:
                    j = 1
                
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
                    
            
            IO.output(motor_down, 0)
            IO.output(motor_up, 0)
            piso_act = 2
            print("Piso actual: ", piso_act)
            print("Puertas abiertas")
            time.sleep(3)
            IO.output(retorno_2up, 0)
            print("Puertas cerradas")
            
            
            
            
        if IO.input(retorno_3up) == 1:
            IO.output(motor_down, 0)
            IO.output(motor_up, 1)
            j = 0
            
            while j == 0:
                
                if IO.input(piso_3) == 1:
                    j = 1
                
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                    j = 2
                    
                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                    
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
            
            if j == 1:
                IO.output(motor_down, 0)
                IO.output(motor_up, 0)
                piso_act = 3
                print("Piso actual: ", piso_act)
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_3up, 0)
                print("Puertas cerradas")
                
            
            
        if IO.input(retorno_4down) == 1:
            IO.output(motor_down, 0)
            IO.output(motor_up, 1)
            j = 0
            
            while j == 0:
                
                if IO.input(piso_4) == 1:
                    j = 1
                
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                    j = 2
                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                    
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    j = 2
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
            
            if j == 1:
                IO.output(motor_down, 0)
                IO.output(motor_up, 0)
                piso_act = 4
                print("Piso actual: ", piso_act)
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_4down, 0)
                print("Puertas cerradas") 
            
        if j == 1:
            print("cambio")
            state = 0
        
                
    if piso_act == 2:        
        
        if IO.input(retorno_3up) == 1:
            IO.output(motor_down, 0)
            IO.output(motor_up, 1)
            j = 0
            
            while j == 0:
            
                if IO.input(piso_3) == 1:
                    j = 1
            
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
            
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)          
            
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
        
            IO.output(motor_down, 0)
            IO.output(motor_up, 0)
            piso_act = 3
            print("Piso actual: ", piso_act)
            print("Puertas abiertas")
            time.sleep(3)
            IO.output(retorno_3up, 0)
            print("Puertas cerradas")
            
        
                
        if IO.input(retorno_4down) == 1:
            IO.output(motor_down, 0)
            IO.output(motor_up, 1)
            j = 0
    
            while j == 0:
        
                if IO.input(piso_4) == 1:
                    j = 1
        
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                    
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    j = 2
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
    
            if j == 1:
                IO.output(motor_down, 0)
                IO.output(motor_up, 0)
                piso_act = 4
                print("Piso actual: ", piso_act)
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_4down, 0)
                print("Puertas cerradas")
                
                
        if j == 1:
            print("cambio")
            state = 0
            
    if piso_act == 3:
        
        if IO.input(retorno_4down) == 1:
            IO.output(motor_down, 0)
            IO.output(motor_up, 1)
            j = 0
    
            while j == 0:
        
                if IO.input(piso_4) == 1:
                    j = 1
        
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                    
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
    
            
            IO.output(motor_down, 0)
            IO.output(motor_up, 0)
            piso_act = 4
            print("Piso actual: ", piso_act)
            print("Puertas abiertas")
            time.sleep(3)
            IO.output(retorno_4down, 0)
            print("Puertas cerradas")
            
    
        if j == 1:
            print("cambio")
            state = 0
        
def down():
    global state
    global piso_act
    print("Bajando")
    
    if piso_act == 4:
                            
        if IO.input(retorno_3down) == 1:
            IO.output(motor_down, 1)
            IO.output(motor_up, 0)
            j= 0
       
            while j == 0:
                
                if IO.input(piso_3) == 1:
                    j = 1
                
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
                    
            
            IO.output(motor_down, 0)
            IO.output(motor_up, 0)
            piso_act = 3
            print("Piso actual: ", piso_act)
            print("Puertas abiertas")
            time.sleep(3)
            IO.output(retorno_3down, 0)
            print("Puertas cerradas")
            
            
            
                    
        if IO.input(retorno_2down) == 1:
            IO.output(motor_down, 1)
            IO.output(motor_up, 0)
            j = 0
            
            while j == 0:
                
                if IO.input(piso_2) == 1:
                    j = 1
                
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                    j = 2
                    
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
            
            if j == 1:
                IO.output(motor_down, 0)
                IO.output(motor_up, 0)
                piso_act = 2
                print("Piso actual: ", piso_act)
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_2down, 0)
                print("Puertas cerradas")
            
            
        if IO.input(retorno_1up) == 1:
            IO.output(motor_down, 1)
            IO.output(motor_up, 0)
            j = 0
            
            while j == 0:
                
                if IO.input(piso_1) == 1:
                    j = 1
                
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                    j = 2
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                    j = 2
                    
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
            
            if j == 1:
                IO.output(motor_down, 0)
                IO.output(motor_up, 0)
                piso_act = 1
                print("Piso actual: ", piso_act)
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_1up, 0)
                print("Puertas cerradas")
                
                    
        if j == 1:
            print("cambio")
            state = 0

    if piso_act == 3:        
                            
        if IO.input(retorno_2down) == 1:
            IO.output(motor_down, 1)
            IO.output(motor_up, 0)
            j = 0
                
            while j == 0:
                
                if IO.input(piso_2) == 1:
                    j = 1
            
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                    
            
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)          
            
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                    j = 2
                    
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
            
            IO.output(motor_down, 0)
            IO.output(motor_up, 0)
            piso_act = 2
            print("Piso actual: ", piso_act)
            print("Puertas abiertas")
            time.sleep(3)
            IO.output(retorno_2down, 0)
            print("Puertas cerradas")
                
            
                                       
        if IO.input(retorno_1up) == 1:
            IO.output(motor_down, 1)
            IO.output(motor_up, 0)
            j = 0
    
            while j == 0:
        
                if IO.input(piso_1) == 1:
                    j = 1
        
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                    j = 2
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                    j = 2
                    
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)
        
            if j == 1:
                IO.output(motor_down, 0)
                IO.output(motor_up, 0)
                piso_act = 1
                print("Piso actual: ", piso_act)
                print("Puertas abiertas")
                time.sleep(3)
                IO.output(retorno_1up, 0)
                print("Puertas cerradas")
                    
                    
        if j == 1:
            print("cambio")
            state = 0
   
          
    if piso_act == 2:
        
        if IO.input(retorno_1up) == 1:
            IO.output(motor_down, 1)
            IO.output(motor_up, 0)
            j = 0

            while j == 0:
        
                if IO.input(piso_1) == 1:
                    j = 1
        
                if IO.input(boton_1up) == 1:
                    IO.output(retorno_1up, 1)
                    
                elif IO.input(boton_2down) == 1:
                    IO.output(retorno_2down, 1)
                    j = 2
                
                elif IO.input(boton_2up) == 1:
                    IO.output(retorno_2up, 1)
                
                elif IO.input(boton_3down) == 1:
                    IO.output(retorno_3down, 1)
                    j = 2
                    
                elif IO.input(boton_3up) == 1:
                    IO.output(retorno_3up, 1)
                    
                elif IO.input(boton_4down) == 1:
                    IO.output(retorno_4down, 1)

            
            IO.output(motor_down, 0)
            IO.output(motor_up, 0)
            piso_act = 1
            print("Piso actual: ", piso_act)
            print("Puertas abiertas")
            time.sleep(3)
            IO.output(retorno_1up, 0)
            print("Puertas cerradas")
            
    
        if j == 1:
            print("cambio")
            state = 0







# Diccionario
mef = {
    0: stop,
    1: up,
    2: down,
    3: hold_up,
    4: hold_down,
    5: start
    }


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de Ascensor")

# Establecer el tamaño de la ventana (ancho x alto)
ventana.geometry("235x490")  # Cambia estas dimensiones según tus necesidades

# Crear un Canvas como fondo
canvas = tk.Canvas(ventana)
canvas.pack(fill=tk.BOTH, expand=True)  # Para que el Canvas se ajuste al tamaño de la ventana

# Cargar la imagen de fondo y obtener sus dimensiones
fondo = tk.PhotoImage(file="fondo.png")  # Reemplaza "fondo.png" con tu propia imagen de fondo
ancho_fondo = fondo.width()
alto_fondo = fondo.height()

# Configurar el Canvas para que se ajuste al tamaño de la imagen de fondo
canvas.config(width=ancho_fondo, height=alto_fondo)

# Mostrar la imagen de fondo en el Canvas
canvas.create_image(0, 0, anchor=tk.NW, image=fondo)


# Crear botones de imagen para los pisos
imagenes_pisos = [tk.PhotoImage(file=f"btn_{i}.png") for i in range(1, 5)]
cerrar  = tk.PhotoImage(file="cerrar.png")
abrir= tk.PhotoImage(file="abrir.png")
imagen_subir = tk.PhotoImage(file="arriba.png") 
imagen_bajar = tk.PhotoImage(file="abajo.png")  
imagen_subir_f = imagen_subir.subsample(2, 2)
imagen_bajar_f = imagen_bajar.subsample(2, 2)  
abrir_f = abrir.subsample(2, 2)
cerrar_f = cerrar.subsample(2, 2) 

# Crear botones de abrir y cerrar puertas
boton_abrir = tk.Button(canvas, image=abrir_f, command=abrir_puertas)
boton_cerrar = tk.Button(canvas, image=cerrar_f, command=cerrar_puertas)


# Crear botones de "Subir" y "Bajar" para cada grupo de pisos
boton_4down = tk.Button(canvas, image=imagen_subir_f, command=retorno_4down)
boton_3down = tk.Button(canvas, image=imagen_bajar_f, command=retorno_3down)
boton_3up = tk.Button(canvas, image=imagen_subir_f, command=retorno_3up)
boton_2down = tk.Button(canvas, image=imagen_bajar_f, command=retorno_2down)
boton_2up = tk.Button(canvas, image=imagen_subir_f, command=retorno_2up)
boton_1up = tk.Button(canvas, image=imagen_bajar_f, command= retorno_1up)


label_piso = tk.Label(canvas, text="", bg="black", fg="red", font=("Helvetica", 36))
label_piso.place(x=40, y=40)  # Ajusta las coordenadas (x, y) según tu preferencia

for i, boton in enumerate(botones_pisos_12):
    boton.place(x=90 + i *40, y=30)  # Ajusta las coordenadas (x, y) según tu preferencia
for i, boton in enumerate(botones_pisos_34):
    boton.place(x=90 + i*40, y=70)  # Ajusta las coordenadas (x, y) según tu preferencia
boton_abrir.place(x=178, y=38)  # Ajusta las coordenadas (x, y) según tu preferencia
boton_cerrar.place(x=178, y=78)  # Ajusta las coordenadas (x, y) según tu preferencia
boton_subir4.place(x=178,y=235)
boton_bajar3.place(x=178,y=160)#20
boton_subir3.place(x=178,y=330)
boton_bajar2.place(x=178,y=270)
boton_subir2.place(x=178,y=435)
boton_bajar1.place(x=178,y=365)

# Void Loop
while True:
    mef[state]()
    
# Iniciar el bucle principal de la aplicación
ventana.mainloop()