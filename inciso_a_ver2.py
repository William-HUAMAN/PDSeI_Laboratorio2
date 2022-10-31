# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:05:15 2022

@author: lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

signal, samplerate = sf.read('audio2.wav')
n = len(signal)
#_________________ RUIDO ____________________%
cantidadRuido = 0.0005
puntosRuido = np.random.permutation(n)
puntosRuido = puntosRuido[0:int(n*cantidadRuido)]
signal[puntosRuido] = 50+np.random.rand(len(puntosRuido))*100

#___________________________________________#
plt.figure(figsize = (20,6))
plt.plot(signal,'r')
plt.title("Señal Ruidosa Genearada")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

sd.play(signal,samplerate)

input("_______________ PRESIONA ENTER __________________")

#___________________________________________#

###Determinar umbral
umbral = 0.25

supUmbral = np.where(signal>umbral)[0]

fsignal = np.copy(signal)

k = 61 #ORDEN

for t in range(len(supUmbral)):
    limiteInf = np.max((0,supUmbral[t]-k))
    limiteSup = np.min((supUmbral[t]+k,n+1))

    fsignal[supUmbral[t]] = np.median(signal[limiteInf:limiteSup])

plt.figure(figsize = (20,6))
plt.plot(range(0,n),signal,'r',label="Original")
plt.plot(range(0,n),fsignal,'b',label="Filtro Mediana")
plt.title("Señal Ruidosa Genearada")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()
plt.show()

sd.play(fsignal,samplerate)

input()

