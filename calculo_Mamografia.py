# Calculo de Blindaje de Mamografía y dosis posterior al blindaje 
# 13-01-2023 EJRT
import numpy as np
import matplotlib.pyplot as plt
import math

## Factores proporcionales de Cálculo en Rayos x barreras secundarias
#alfa_rx_1= []
#beta_rx_1=
#gamma_rx1=


## Factores de proporcionales de cálculo Mamografía barrera secundaria
aPb= 2.99E+01 # mm-1
bPb= 1.84E+02 # mm-1
gPb= 3.55E-01

k= 3.60E-02 # mGy/pac
n_paciente= float(input('Ingresa el numero de pacientes en un día:  ',))
dias_semanales= float(input('Ingresa los días hábiles:  ',   ))
print ("Estos son los días hábiles"," ", dias_semanales)

#horas_diarias= 8

betaalfa= bPb/aPb
betaalfa_1= betaalfa+1
alfagamma= aPb*gPb
n= n_paciente*dias_semanales


of= float(input('Ingresa el factor de ocupación de la barrera:  ',))
distance= float(input('Ingresa la distancia de la barrera o PIR en [m]:  ',))
x=float(input('Ingresa el espesor en [mm] de Pb:  ',))

#print ("La ocupación es= ", of, "Mientras que la distancia de la barrera o del PIR es= ",distance)

dosis_despues_de_la_barrera= (n*of*k)/((distance**2)*(((np.exp(x*alfagamma)*betaalfa_1)-betaalfa)**(1/gPb)))
#dosis_despues_de_la_barrera= (of*k)/((distance**2)*(((np.exp(x*alfagamma)*betaalfa_1)-betaalfa)**(1/gPb))) #No funciona

barrera_comprobacion= (1/alfagamma)*(math.log(((n*of*k/((distance**2)*dosis_despues_de_la_barrera))**gPb+betaalfa)/betaalfa_1))

Limite_de_dosis_semanal= float(input('Ingrese acá el límite de dosis semanal en [mSv]  ',  ))

#barrera_calculada= (1/alfagamma)*(np.log(((N*of*k/((distance**2)*Limite_de_dosis_semanal))**gPb+betaalfa)/betaalfa_1))

barrera_calculada=(1/alfagamma)*(math.log((((n*of*k/((distance**2)*Limite_de_dosis_semanal))**gPb)+betaalfa)/betaalfa_1))

print ("Total de pacientes semanales", ' ',n)
#barrera_comprobacion= round(barrera_comprobacion, 1)
print('El espesor de comprobación de la barrera es ',barrera_comprobacion, '[mm] de Plomo')
print('EL valor entre el espesor impuesto y el calculado tiene un', float(((x-barrera_comprobacion)/barrera_comprobacion)*100),"% de diferencia")
dosis_despues_de_la_barrera= np.format_float_scientific(dosis_despues_de_la_barrera, precision=2, exp_digits=2)
print('La Dosis despues de la barrera es ', dosis_despues_de_la_barrera, '[mSv]')
barrera_calculada= round(barrera_calculada, 1)
print('La barrera calculada por el NCRP 147 es ', barrera_calculada, '[mm] de Plomo')

## Haciendo un nuevo ciclo para radiodiagnostivo
