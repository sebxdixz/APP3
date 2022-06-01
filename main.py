#App 3: En esta aplicacion se recibira un input.txt, este mismo representaria un laberinto, el cual esta construido a base de 1 y 0.
#Los 0s representan caminos en el laberinto y los 1s representan paredes.
#Este programa tiene que ser construido en Paradigma Orientado Funcional, por lo que no se pueden usar variables globales.
#Despues entregara un output de las cordenadas, por las cuales paso el laberinto.
#Tiene que haber una entrada a la izquierda, y tambien una salida a la derecha. 

import sys
import numpy as np


def main(n,m,laberinto):
    laberinto = np.zeros((n, m), dtype=int)

    for x in open('input.txt','r').read():
    

  
