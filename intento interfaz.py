from tkinter import *
from PIL import Image, ImageTk
import time
import pygame
from pygame import mixer
import random
#Musica para la pantalla principal
mixer.init()
cancion = mixer.Sound("X2Download.app - Tokyo Drift (Fast & Furious) (64 kbps).mp3")
mixer.Sound.set_volume(cancion, 0.1)


#Ventana Principal
ventana = Tk()
ventana.title("Carrito")
ventana.geometry("987x629")
ventana.resizable(False, False)
cancion.play()

#Canvas
canvas1 = Canvas(ventana, width=989, height=629, bg="#D5D2FF")
canvas1.place(x=-1, y=0)

#Imagen fondo
imgfondo = Image.open("carro1.jpg")
resizedfondo = imgfondo.resize((987, 629), Image.ANTIALIAS)
nvofondo = ImageTk.PhotoImage(resizedfondo)
fndbg = canvas1.create_image(0, 0, image=nvofondo, anchor=NW)

#Titulo
imgtitulo = Image.open("titulo RC.png")
resizedtitulo = imgtitulo.resize((495, 200), Image.ANTIALIAS)
nvotitulo = ImageTk.PhotoImage(resizedtitulo)
titulo = canvas1.create_image(290, 0, image=nvotitulo, anchor=NW)

def ventanajuego():
    ventana2 = Toplevel()
    ventana.withdraw()
    ventana2.title("PLAY")
    ventana2.geometry("730x487")
    ventana2.resizable(False, False)


    #CANVAS DE LA VENTANA 2
    canvas2 = Canvas(ventana2, height=487, width=730)
    canvas2.pack(side="top", anchor="center")
    #IMAGEN FONDO
    imgfondo2 = ImageTk.PhotoImage(Image.open("carro2.jpg"))
    canvas2.create_image(728,2, anchor=NE, image=imgfondo2)

    """IMAGEN FLECHA ARRIBA"""
    img_up = PhotoImage(file="flecha.jpg")

    imgU_label = Label(image=img_up)
    imgU_label.pack(pady=10)

    buttonUp = Button(canvas2, image=img_up, bg="black")
    buttonUp.place(x=100, y=100)
    def back():
        ventana.deiconify()
        ventana2.destroy()

    # BOTÓN QUE REGRESA A LA PANTALLA PRINCIPAL
    regreso = Button(ventana2, text="Back", fg="#ECB301", font=("Broche Cut", 10), background="black", activebackground="#FD8201", activeforeground="black",
                     borderwidth=1, command=back)
    regreso.place(x=645, y=475, anchor=SW)

    ventana2.mainloop()


btnjugar = Button(ventana, text="PLAY", width=8, height=2,fg="#ECB301", bg= "black",font=("Broche Cut", 16), activebackground="#FD8201", activeforeground="black",
                  borderwidth=0, command= ventanajuego).place(relx=0.44, rely=0.85)
btnfuera = Button(ventana, text="EXIT",fg="#ECB301", bg= "black",font=("Broche Cut", 16), activebackground="#FD8201", activeforeground="black",
                  borderwidth=0.5, width=6, height=2, command=lambda: [ventana.destroy()]).place(relx=0.03, rely=0.05)

ventana.mainloop()


