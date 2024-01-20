"""
Reto #2: Control de un ascensor 

Septiembre 25 del 2023

Realizado por:
- Jacobo Chica Quintero
- Sara Alvarez Bello
- Jua Diego Agudelo Balvin

"""

# Librerias
import tkinter

# Creación de la interfaz grafica
window=tkinter.Tk()
window.geometry("300x400")

# Titulos
titulo = tkinter.Label(window, text = "CONTROL MOTOR DC",font = ('Courier', 30, "bold"))
titulo.pack()
subtitulo = tkinter.Label(window, text = "Interfaz grafica en Python",font = ('Courier', 16, "bold"))
subtitulo.pack()
window.mainloop()