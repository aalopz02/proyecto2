#Andres Artavia Lopez
#Carnet: 2017075875
#Grupo: 04
from tkinter import *
import winsound
import os
import time

tk=Tk()
funciones=("hello=dice hola\nbuilt=fecha de creacion\npower=dar energia al robot\nstatus=muestra la energiarestante\ngoahead=se mueve hacia delante\ngoback=se mueve hacia atras\nright=gira hacia la derecha\nleft=gira ala izquierda\ndance=el robotbaila\nsmile=el robot se rie\ncry=el robot llora\nown1=se hacen reset de los datos\nown2=el robot salta\n")
#Se define la tupla que contiene los comandos de ayuda
animaciones=['../img/robot.gif','../img/robotatras.gif',
             '../img/robotderecha.gif','../img/robotizquierda.gif',
             '../img/robotcamina1.gif','../img/robotcamina2.gif',
             '../img/robotbaila1.gif','../img/robotbaila2.gif','../img/robotsonrie.gif',
             '../img/robotllora.gif','../img/robotsalta.gif','../img/robotcaminaatras.gif']
#Se define la lista con los directorios de las animaciones para mayor facilidad de manipulacion 
#Funcion que abre el archivo al inicio y asigna los diferentes valores guardados a las diferentes variables, recibe el indice al que va a asignar la lectura
i=0
def leer_archivo(n):
     with open("robot.txt") as txt:
          x=txt.readlines()
          for i in range(0,len(x)-1):
               x[i].strip('\n')
          return int(x[n])
energia_aux=leer_archivo(3)
animacion=leer_archivo(4)
tamano1=leer_archivo(5)
tamano2=leer_archivo(6)
#Funcion que recibe un valor a sobreescribir y cual nombre tiene, para guardarlo en el .txt
def escribir_archivo(cambio,valor):
     guardar=open("robot.txt","r+")
     x=guardar.readlines()
     x_aux=''
     guardar.seek(0)
     valor=str(valor)
     if cambio=='energia':
          x[3]=valor+'\n'
     elif cambio=='posicion':
          x[4]=valor+'\n'
     elif cambio=='t1':
          x[5]=valor+'\n'
     elif cambio=='t2':
          x[6]=valor+'\n'
     else: error('error al escribir archivo')
     for i in range(0,7):
          x_aux=x_aux+x[i]
     guardar.write(x_aux)
     guardar.close()
def Aceptar():
     act=e1.get()
     hacer_accion(act)
     e1.delete(0,END)
#Funcion que abre un .txt que contiene una descripcion mas detallada de los comandos
def mas_opciones():
     os.startfile('ayuda.txt')
#Funcion que crea la ventana de ayuda la cual contien los comandos que puede digitar el usuario
def Ayuda():
     ventana2=Tk()
     ventana2.title("HELP")
     ayuda=Label(ventana2,text=funciones,fg="black")
     salir=Button(ventana2,text="SALIR",command=ventana2.destroy,fg="red",bg="white")
     mas=Button(ventana2,text="MAS...",command=mas_opciones,fg="blue",bg="white")
     ayuda.grid(row=0,column=0,columnspan=2,rowspan=1)
     salir.grid(row=1,column=1,sticky=E)
     mas.grid(row=1,column=0,sticky=W)
#Funcion que crea una ventana para hacer la recarga
def power():
     #Funcion que verifica que el texto de la entrada sea valido y llama a la funcion que modifica la energia
     def recargar():
          n=power.get()
          if n=='':
               power.delete(0,END)
               return error('valor invalido')
          if ('.' in n) or (','in n):
               power.delete(0,END)
               return error('el valor de recarga no es entero')
          n=int(power.get())
          if n<0:
               power.delete(0,END)
               return error('el valor de recarga es menor a 0')
          power.delete(0,END)
          global energia_aux
          if n+energia_aux>100:
               return error('el valor de la recarga supera 100')
          else:
               reducir_energia(-n)
     recarga=Tk()
     recarga.title("RECARGAR")
     txt=Label(recarga,text="Digite el total a recargar ",fg="black")
     power=Entry(recarga,fg="black",bg="white")
     ok=Button(recarga,text="OK",command=recargar,fg="black")
     salir=Button(recarga,text="SALIR",command=recarga.destroy,fg="red")
     salir.grid(row=1,column=0)
     txt.grid(row=0,column=0)
     power.grid(row=0,column=1)
     ok.grid(row=1,column=1)
#Funcion que cambia la etiqueta que contiene el dato de la energia, recibe el texto de energia y el color, que depende de la cantidad de energia
def energia_robot(tk,cfe,energia):
     energy=Label(tk,text="  "+energia+"  ",fg="black",bg=cfe)
     energy.grid(row=0,column=0,sticky=N)
#Funcion que modifica la variable de la energia y envia datos a la funcion que cambia la etiqueta para ver si se cambia el color de la etiqueta. Recibe el valor a recargar o reducir
def reducir_energia(n):
     global energia_aux
     energia_aux=energia_aux-n
     if energia_aux<=20:
          x="red"
     else:
          x="green"
     escribir_archivo('energia',energia_aux)
     energia_robot(tk,x,str(energia_aux))
#Funcion que revisa la cantidad de energia y envia un mensaje si esta baja o agotada
def revisar_energia():
     if energia_aux<10 and energia_aux>1:
            error('Energia baja')
     elif energia_aux==0:
            error('Energia agotada')
#Funcion para el comando 'status' que cambia de ccolor la energia para llamar la atencion del usuario
def status():
     revisar_energia()
     energia_robot(tk,"yellow",str(energia_aux))
     tk.after(500, lambda: reducir_energia(0))
#Funcion que se ejecuta despues del comando 'own1' que resetea completamente el robot
def hacer_reset():
     global tamano1
     global tamano2
     tamano1=24
     tamano2=24
     reducir_energia(-(100-energia_aux))
     cambiar_posicion(0,'+')
     cambiar_posicion(0,'-')
#Funcion que recibe dos valores para cambiar la imagen, el numero por la cual se cambia en la lista de animaciones y otro para ver si se hace mas pequeña o mas grande
def cambiar_imagen2(event):
     global animaciones                   
     global img
     global imagen
     global i
     img=PhotoImage(file=animaciones[i])
     tk.columnconfigure(1, weight=1)
     tk.rowconfigure(0,weight=1)
     imagen=Label(image=img,bg='white')
     imagen.grid(row=0,column=1,columnspan=2,rowspan=2)
     i+=1
     if i>11:
          i=0

def cambiar_posicion(x,tamano):
     global animaciones
     global i
     global img
     global imagen
     global tamano1
     global tamano2
     img=PhotoImage(file=animaciones[x])
     if tamano=='+':
          img=img.zoom(tamano1)
          img=img.subsample(tamano2)
          tamano1+=1
          #escribir_archivo('t1',tamano1)
     elif tamano=='-':
          img=img.zoom(tamano1)
          img=img.subsample(tamano2)
          tamano2+=1
          #escribir_archivo('t2',tamano2)
     else:
          img=img.zoom(tamano1)
          img=img.subsample(tamano1)
     tk.columnconfigure(1, weight=1)
     tk.rowconfigure(0,weight=1)
     imagen=Label(image=img,bg="white")
     imagen.grid(row=0,column=1,columnspan=2,rowspan=2)
     #escribir_archivo('posicion',x)
     if i==0:
          i=4
     else: i=0
#Fucion que contiene el menu con los diferentes comandos y la funcion que debe de ejecutar cada uno, recibe el valor de la entrada de texto
def hacer_accion(act):
     global animaciones                   
     global img
     global imagen
     if act=="hello":
          winsound.PlaySound('../audio/hola.wav',winsound.SND_FILENAME)
     if act=='built':
          winsound.PlaySound('../audio/built.wav',winsound.SND_FILENAME)
     if act=='power':
          power()
     if act=='status':
          status()
     if act=='goahead':
          if energia_aux>0:
               cambiar_posicion(5,'+')
               tk.after(50, lambda: cambiar_posicion(0,'+'))
               reducir_energia(1)
               revisar_energia()
          else:error("No hay suficiente energia")
     if act=='goback':
          if energia_aux>0:
               cambiar_posicion(11,'-')
               tk.after(50, lambda: cambiar_posicion(1,'-'))
               reducir_energia(1)
               revisar_energia()
          else:error("No hay suficiente energia")
     if act=='right':
           if energia_aux>0:
               cambiar_posicion(2,'+')
               reducir_energia(1)
               revisar_energia()
           else:error("No hay suficiente energia")
     if act=='left':
           if energia_aux>0:
               cambiar_posicion(3,'+')
               reducir_energia(1)
               revisar_energia()
           else:error("No hay suficiente energia")
     if act=='dance':
          if energia_aux<2:
               error("No hay suficiente energia")
          else:
               cambiar_posicion(6,'+')
               tk.after(50, lambda: cambiar_posicion(7,'-'))
               reducir_energia(2)
               revisar_energia()
     if act=='smile':
          for i in range(0,2):
               tk.after(1000,lambda: cambio_imagen2(i))
          #cambiar_posicion(8,'-')
          #tk.after(50, lambda: cambiar_posicion(0,'-'))
     if act=='cry':
          if energia_aux>0:
               cambiar_posicion(9,'-')
               tk.after(50, lambda: cambiar_posicion(0,'-'))
               reducir_energia(1)
               revisar_energia()
          else:error("No hay suficiente energia")
     if act=='own2':
          if energia_aux>0:
               cambiar_posicion(10,'+')
               tk.after(50, lambda: cambiar_posicion(0,'-'))
               reducir_energia(1)
               revisar_energia()
          else:error("No hay suficiente energia")
     if act=='own1':
          hacer_reset()
#Funcion que recibe un texto y crea una ventana de error con ese valor
def error(txt):
     ventana=Tk()
     ventana_error=Label(ventana,text=txt,fg="black")
     ventana_error.pack()
     ventana.title("ERROR")
     ventana.minsize(200,10)

#Creacion de la ventana principal y la modificacion de los respectivos valores
img=PhotoImage(file=animaciones[0])
imagen=Label(image=img)
cambiar_posicion(animacion,'=')
tk.title("ROBOT")
tk.configure(background='white')
tk.maxsize(335,340)
tk.minsize(335,340)
energia_robot(tk,"green",str(energia_aux))
reducir_energia(0)
e1=Entry(tk,fg="black",bg="white")
e1.insert(20,"instruccion")
e1.grid(row=3,column=1,sticky=E)
aceptar=Button(tk,text="ACEPTAR",command=Aceptar,bg="green")
aceptar.grid(row=3,column=2,sticky=W)
ayuda=Button(tk,text="  ?  ",command=Ayuda,fg="black",bg="blue")
ayuda.grid(row=0,column=3,sticky=N)
tk.bind("<Up>",cambiar_imagen2)

tk.mainloop()
