from matplotlib import pyplot
from tkinter import *
import serial, time


'''Variables Globales'''
colorFondo = "forest green" #chartreuse4, DarkOliveGreen
colorLetra = "White"


humedo = 800 #arduino.readline()
seco = humedo - 1023
estados = ('Seco', 'Humedo')
slices = (seco , humedo)
color = ('red' , 'blue')

'''Visualisado'''
raiz = Tk() #Se habre una ventana
raiz.title('Growing Hacks') #se define el titulo
raiz.iconbitmap("icono.ico") #Se define el logo
#raiz.geometry("650x650")
#raiz.config(background=colorFondo)


'''Procentaje'''

#arduino = serial.Serial('/dev/rfcomm0', 9600) #añadimos una varible
#time.sleep(2)
humedad = 800 #arduino.readline()
porcentaje = humedad * 10.23/100


'''Boton Motores'''
def motores():
    arduino = serial.Serial("COM3", 9600)
    time.sleep(2)
    arduino.write(True) #Se coloca el valor deseado True encendido False apagado
    arduino.close()


'''Contador de tiempo''' # ¿Como se asigna una operacion a una funcion?
def cronomiter():
    while 0==0:
        for d in range(0,9999):
            for h in range(0,24):
                for m in range(0,60):
                    for s in range(0,60):
                        time.sleep(1)
                        print ('Hora:{} Minutos:{} Segundos:{}'.format(h,m,s))

boton1 = Button(raiz, text='Activar mini-pupms', command=motores).grid(row=1,column=1)
boton2 = Button(raiz, text='Macador de siembra', command=cronomiter).grid(row=2,column=1)

etiqueta = Label(raiz,text="Tu humedad es % {}".format(porcentaje)).grid(row=1,column=0)

pyplot.pie(slices, colors=color, labels=estados)
pyplot.axis('equal')
pyplot.title('Grafica de Humedad')
pyplot.legend(labels=estados)
pyplot.show()

raiz.mainloop() #Se evita que alguien realice modificacion desde el simbolo de sistema y se que se cierre la app
