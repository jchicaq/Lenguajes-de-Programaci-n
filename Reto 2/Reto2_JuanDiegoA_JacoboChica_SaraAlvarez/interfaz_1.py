import tkinter as tk

# Función para manejar el clic en los botones de los pisos
def seleccionar_piso(piso):
    # Aquí puedes agregar la lógica para controlar el ascensor
    label_piso.config(text=f"{piso}")
    print(f"Seleccionaste el piso {piso}")

# Funciones para manejar los clics en los botones de abrir y cerrar puertas
def abrir_puertas():
    # Aquí puedes agregar la lógica para abrir las puertas
    print("Abriendo las puertas")

def cerrar_puertas():
    # Aquí puedes agregar la lógica para cerrar las puertas
    print("Cerrando las puertas")

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
boton_subir4 = tk.Button(canvas, image=imagen_subir_f, command=lambda: print("Subir a 4"))
boton_bajar3 = tk.Button(canvas, image=imagen_bajar_f, command=lambda: print("Bajar a 3"))
boton_subir3 = tk.Button(canvas, image=imagen_subir_f, command=lambda: print("Subir a 3"))
boton_bajar2 = tk.Button(canvas, image=imagen_bajar_f, command=lambda: print("Bajar a 2"))
boton_subir2 = tk.Button(canvas, image=imagen_subir_f, command=lambda: print("Subir a 2"))
boton_bajar1 = tk.Button(canvas, image=imagen_bajar_f, command=lambda: print("Bajar a 1"))


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
# Iniciar el bucle principal de la aplicación
ventana.mainloop()
