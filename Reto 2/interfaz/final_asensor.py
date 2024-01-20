#Library declaration
import RPi.GPIO as GPIO
import time
import tkinter as tk
import threading


# Función para manejar el clic en los botones de los pisos
def seleccionar_piso(piso):
    # Aquí puedes agregar la lógica para controlar el ascensor
    label_piso.config(text=f"{piso}")
    print(f"Seleccionaste el piso {piso}")

    if piso == 1:
        piso1()
    elif piso == 2:
        piso2()
    elif piso == 3:
        piso3()
    else:
        piso4()

# Funciones para manejar los clics en los botones de abrir y cerrar puertas
def abrir_puertas():
    # Aquí puedes agregar la lógica para abrir las puertas
    print("Abriendo las puertas")

def cerrar_puertas():
    # Aquí puedes agregar la lógica para cerrar las puertas
    print("Cerrando las puertas")

def detect_ps1():
    global state
    if GPIO.input(ps1) == 1:
        GPIO.output(rs1, 1)
        ms1 = 1
        state = 1

def detect_ps2():
    global state
    if GPIO.input(ps2) == 1:
        GPIO.output(rs2, 1)
        ms2 = 1
        state = 2

def detect_pb2():
    global state
    if GPIO.input(pb2) == 1:
        GPIO.output(rb2, 1)
        mb2 = 1
        state = 2

def detect_ps3():
    global state
    if GPIO.input(ps3) == 1:
        GPIO.output(rs3, 1)
        ms3 = 1
        state = 3

def detect_pb3():
    global state
    if GPIO.input(pb3) == 1:
        GPIO.output(rb3, 1)
        mb3 = 1
        state = 3

def detect_pb4():
    global state
    if GPIO.input(pb4) == 1:
        GPIO.output(rb4, 1)
        mb4 = 1
        state = 4
        print(state)


state=0

#sensores pisos
sp1=3
sp2=4
sp3=17
sp4=27

#botones
ps1=6
pb2=13
ps2=19
pb3=26
ps3=5
pb4=24

#motores
subir=14
bajar=15
abrir=18
cerrar=23
# retorno de los botones
rs1=7
rb2=12
rs2=16
rb3=20
rs3=21
rb4=25

GPIO.setmode(GPIO.BCM)
GPIO.setup(sp1,GPIO.IN)
GPIO.setup(sp2,GPIO.IN)
GPIO.setup(sp3,GPIO.IN)
GPIO.setup(sp4,GPIO.IN)

GPIO.setup(ps1,GPIO.IN)
GPIO.setup(pb2,GPIO.IN)
GPIO.setup(ps2,GPIO.IN)
GPIO.setup(pb3,GPIO.IN)
GPIO.setup(ps3,GPIO.IN)
GPIO.setup(pb4,GPIO.IN)

ms1=0
mb2=0
ms2=0
mb3=0
ms3=0
mb4=0

GPIO.setup(subir,GPIO.OUT)
GPIO.setup(bajar,GPIO.OUT)
GPIO.setup(abrir,GPIO.OUT)
GPIO.setup(cerrar,GPIO.OUT)
GPIO.setup(rs1,GPIO.OUT)
GPIO.setup(rb2,GPIO.OUT)
GPIO.setup(rs2,GPIO.OUT)
GPIO.setup(rb3,GPIO.OUT)
GPIO.setup(rs3,GPIO.OUT)
GPIO.setup(rb4,GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(bajar, 0)
GPIO.output(subir, 0)
GPIO.output(abrir, 0)
GPIO.output(cerrar, 0)

GPIO.output(rs1, 0)
GPIO.output(rs2, 0)
GPIO.output(rb2, 0)
GPIO.output(rs3, 0)
GPIO.output(rb3, 0)
GPIO.output(rb4, 0)



def detect():
    global state
    
    if GPIO.input(ps1) == 1 :
        GPIO.output(rs1, 1)
        ms1=1
        state=1
    elif GPIO.input(ps2) == 1 :
        GPIO.output(rs2, 1)
        ms2=1
        state=2
    elif GPIO.input(pb2) == 1 :
        GPIO.output(rb2, 1)
        mb2=1
        state=2
    elif GPIO.input(ps3) == 1 :
        GPIO.output(rs3, 1)
        ms3=1
        state=3
    elif GPIO.input(pb3) == 1 :
        GPIO.output(rb3, 1)
        mb3=1
        state=3
    elif GPIO.input(pb4) == 1 :
        GPIO.output(rb4, 1)
        mb4=1
        state=4
        print(state)
        
def piso1():
    global state
    if GPIO.input(sp2)==1 or GPIO.input(sp3)==1 or GPIO.input(sp4)==1:
        GPIO.output(bajar, 1)
    state=5
    print(state)
    
def piso2():
    global state
    if GPIO.input(sp3)==1 or GPIO.input(sp4)==1:
        GPIO.output(bajar, 1)
    elif GPIO.input(sp1)==1:
        GPIO.output(subir, 1)
    state=6
    print(state)
    
def piso3():
    global state
    if GPIO.input(sp2)==1 or GPIO.input(sp1)==1:
        GPIO.output(subir, 1)
    elif GPIO.input(sp4)==1:
        GPIO.output(bajar, 1)
    state=7
    print(state)

def piso4():
    global state
    if GPIO.input(sp1)==1 or GPIO.input(sp2)==1 or GPIO.input(sp3)==1:
        GPIO.output(subir, 1)
    state=8
    print(state)

def pare1():
    global state
    if GPIO.input(sp1)==1:
        GPIO.output(bajar, 0)
        GPIO.output(subir, 0)
        GPIO.output(rs1, 0)
        state=0
    print(state)
        
def pare2():
    global state
    if GPIO.input(sp2)==1:
        GPIO.output(bajar, 0)
        GPIO.output(subir, 0)
        GPIO.output(rs2, 0)
        GPIO.output(rb2, 0)
        state=0
    print(state)

def pare3():
    global state
    if GPIO.input(sp3)==1:
        GPIO.output(bajar, 0)
        GPIO.output(subir, 0)
        GPIO.output(rs3, 0)
        GPIO.output(rb3, 0)
        state=0
    print(state)

def pare4():
    global state
    if GPIO.input(sp4)==1:
        GPIO.output(bajar, 0)
        GPIO.output(subir, 0)
        GPIO.output(rb4, 0)
        state=0
    print(state)



FSM = {0: detect,
       1: piso1,
       2: piso2,
       3: piso3,
       4: piso4,
       5: pare1,
       6: pare2,
       7: pare3,
       8: pare4,
       
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
botones_pisos_12 = [tk.Button(canvas, image=imagen, command=lambda i=i: seleccionar_piso(i+1)) for i, imagen in enumerate(imagenes_pisos[:2])]
botones_pisos_34 = [tk.Button(canvas, image=imagen, command=lambda i=i: seleccionar_piso(i+3)) for i, imagen in enumerate(imagenes_pisos[2:])]

# Crear botones de abrir y cerrar puertas
boton_abrir = tk.Button(canvas, image=abrir_f, command=abrir_puertas)
boton_cerrar = tk.Button(canvas, image=cerrar_f, command=cerrar_puertas)

botones_pisos_12 = [tk.Button(canvas, image=imagen, command=lambda i=i: seleccionar_piso(i+1)) for i, imagen in enumerate(imagenes_pisos[:2])]
botones_pisos_34 = [tk.Button(canvas, image=imagen, command=lambda i=i: seleccionar_piso(i+3)) for i, imagen in enumerate(imagenes_pisos[2:])]


# Crear botones de "Subir" y "Bajar" para cada grupo de pisos
boton_subir4 = tk.Button(canvas, image=imagen_subir_f, command=detect_ps3)
boton_bajar3 = tk.Button(canvas, image=imagen_bajar_f, command=detect_pb4)
boton_subir3 = tk.Button(canvas, image=imagen_subir_f, command=detect_ps2)
boton_bajar2 = tk.Button(canvas, image=imagen_bajar_f, command=detect_pb3)
boton_subir2 = tk.Button(canvas, image=imagen_subir_f, command=detect_ps1)
boton_bajar1 = tk.Button(canvas, image=imagen_bajar_f, command=detect_pb2)


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


# Función que representa el bucle en segundo plano
def bucle_en_paralelo():
    while True:
        tact = time.time() #Acquire actual time
        FSM[state]()   



# Crear y comenzar el hilo para el bucle en paralelo
hilo_bucle = threading.Thread(target=bucle_en_paralelo)
hilo_bucle.daemon = True  # Hacer que el hilo sea un demonio para que termine cuando se cierre la aplicación
hilo_bucle.start()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

