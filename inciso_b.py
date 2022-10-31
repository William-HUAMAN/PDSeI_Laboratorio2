# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:05:15 2022

@author: lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

signal, samplerate = sf.read('audio.wav')
n = len(signal)
#_________________ RUIDO ____________________%
cantidadRuido = 0.0005
puntosRuido = np.random.permutation(n)
puntosRuido = puntosRuido[0:int(n*cantidadRuido)]
signal[puntosRuido] = 50+np.random.rand(len(puntosRuido))*100
plt.style.use('dark_background')
#___________________________________________#


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

########### METODO LENTO (en tiempo real)

fsignal = np.zeros_like(signal)
for i in range(1,len(signal)-1):
    fsignal[i] = signal[i]**2 - signal[i-1]*signal[i+1]

########### METODO RÁPIDO 

fsignal2 = np.zeros_like(signal)
fsignal2[1:-1] = signal[1:-1]**2 - signal[0:-2]*signal[2:]

plt.figure(figsize = (20,6))
plt.plot(signal/np.max(signal),'b',label='Señal')
plt.plot(fsignal2/np.max(fsignal2),'r',label='Señal Normalizada')
plt.title("Señal original y filtrada normalizada")
plt.xlabel("Tiempo (ms)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

plt.show()



input()