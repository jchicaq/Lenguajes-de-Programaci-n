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


# Estados
stop = 0
up = 1
down = 2
start = 3

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
        
    if IO.input(piso_4) == 1:
        piso_act = 4
        print("Piso actual: ", piso_act)
        state = 0
    
    else:
        print("Buscando el piso mas cercano")
        while IO.input(piso_1) == 0 and IO.input(piso_2) == 0 and IO.input(piso_3) == 0 and IO.input(piso_4) == 0:
            IO.output(motor_down, 0)
            IO.output(motor_up, 1)
            
            
            

def stop():
    # Variables globales
    global time_i
    global state
    global piso_act
    
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
                print("Estado: Puertas abriendo")
                time.sleep(3)
                IO.output(retorno_1up, 0)
                print("Estado: Puertas cerrando")
                
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
                print("Estado: Puertas abriendo")
                time.sleep(3)
                IO.output(retorno_2down, 0)
                print("Estado: Puertas cerrando")
                
            elif IO.input(retorno_2up) == 1:
                print("Estado: Puertas abriendo")
                time.sleep(3)
                IO.output(retorno_2up, 0)
                print("Estado: Puertas cerrando")
                
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
                print("Estado: Puertas abriendo")
                time.sleep(3)
                IO.output(retorno_3down, 0)
                print("Estado: Puertas cerrando")
                
            elif IO.input(retorno_3up) == 1:
                print("Estado: Puertas abrienddo")
                time.sleep(3)
                IO.output(retorno_3up, 0)
                print("Estado: Puertas cerrando")
                
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
                print("Estado: Puertas abriendo")
                time.sleep(3)
                IO.output(retorno_4down, 0)
                print("Estado: Puertas cerrando")
                
def up():
    global state
    global piso_act
    print("Estado: Subiendo")
    
        
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
            print("Estado: Puertas abriendo")
            time.sleep(3)
            IO.output(retorno_2up, 0)
            print("Estado: Puertas cerrando")
            
            
            
            
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
                print("Estado: Puertas abriendo")
                time.sleep(3)
                IO.output(retorno_3up, 0)
                print("Estado: Puertas cerrando")
                
            
            
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
                print("Estado: Puertas abriendo")
                time.sleep(3)
                IO.output(retorno_4down, 0)
                print("Estado: Puertas cerrando") 
            
        if j == 1:
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
            print("Estado: Puertas abriendo")
            time.sleep(3)
            IO.output(retorno_3up, 0)
            print("Estado: Puertas cerrando")
            
        
                
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
                print("Estado: Puertas abriendo")
                time.sleep(3)
                IO.output(retorno_4down, 0)
                print("Estado: Puertas cerrando")
                
                
        if j == 1:
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
            print("Estado: Puertas abiendo")
            time.sleep(3)
            IO.output(retorno_4down, 0)
            print("Estado: Puertas cerrando")
            
    
        if j == 1:
            state = 0
        
def down():
    global state
    global piso_act
    print("Estado: Bajando")
    
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
            print("Estado: Puertas abiendo")
            time.sleep(3)
            IO.output(retorno_3down, 0)
            print("Estado: Puertas cerrando")
            
            
            
                    
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
                print("Estado: Puertas abiendo")
                time.sleep(3)
                IO.output(retorno_2down, 0)
                print("Estado: Puertas cerrando")
            
            
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
                print("Estado: Puertas abriendo")
                time.sleep(3)
                IO.output(retorno_1up, 0)
                print("Estado: Puertas cerrando")
                
                    
        if j == 1:
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
            print("Estado: Puertas abriendo")
            time.sleep(3)
            IO.output(retorno_2down, 0)
            print("Estado: Puertas cerrando")
                
            
                                       
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
                print("Estado: Puertas abiendo")
                time.sleep(3)
                IO.output(retorno_1up, 0)
                print("Estado: Puertas cerrando")
                    
                    
        if j == 1:
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
            print("Estado: Puertas abriendo")
            time.sleep(3)
            IO.output(retorno_1up, 0)
            print("Estado: Puertas cerrando")
            
    
        if j == 1:
            state = 0


# Diccionario
mef = {
    0: stop,
    1: up,
    2: down,
    3: start
    }


# Void Loop
while True:
    mef[state]()
    