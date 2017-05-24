from tkinter import *
import winsound
import os
import time

tk=Tk()
delante=['../img/robot.gif','../img/robotcamina1.gif','../img/robotcamina2.gif','../img/robot.gif']
atras=['../img/robotatras.gif','../img/robotcaminaatras.gif','../img/robotcaminaatras2.gif','../img/robotatras.gif']
#,'../img/robotderecha.gif',
  #           '../img/robotizquierda.gif','../img/robotbaila1.gif','../img/robotbaila2.gif',
    #         '../img/robotsonrie.gif','../img/robotllora.gif','../img/robotsalta.gif']

i=0
j=0
tamano1=27
tamano2=27

def cambio_imagen_delante(event):
     tk.after(1500)
     global animaciones
     global img
     global i
     global imagen
     global tamano1
     global tamano2
     print(delante[i])
     img=PhotoImage(file=delante[i])
     img=img.zoom(tamano1)
     img=img.subsample(tamano2)
     tk.columnconfigure(1, weight=1)
     tk.rowconfigure(0,weight=1)
     imagen=Label(image=img,bg='white')
     imagen.grid(row=0,column=1)
     tamano1+=1
     i+=1
     if i==3:
          i=0
          
def cambio_imagen_atras(event):
     tk.after(1500)
     global j
     global animaciones
     global img
     global imagen
     global tamano1
     global tamano2
     print(atras[j])
     img=PhotoImage(file=atras[j])
     img=img.zoom(tamano1)
     img=img.subsample(tamano2)
     tk.columnconfigure(1, weight=1)
     tk.rowconfigure(0,weight=1)
     imagen=Label(image=img,bg='white')
     imagen.grid(row=0,column=1)
     j+=1
     tamano2+=1
     if j==3:
          j=0

tk.maxsize(335,340)
tk.minsize(335,340)
tk.configure(background='white')
img=PhotoImage(file=delante[0])
imagen=Label(image=img)
imagen.grid(row=0,column=1)
tk.bind("<Up>",cambio_imagen_delante)
tk.bind("<Down>",cambio_imagen_atras)

tk.mainloop()
