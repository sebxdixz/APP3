#App 3: En esta aplicacion se recibira un input.txt, este mismo representaria un laberinto, el cual esta construido a base de 1 y 0.
#Los 0s representan caminos en el laberinto y los 1s representan paredes.
#Este programa tiene que ser construido en Paradigma Orientado Funcional, por lo que no se pueden usar variables globales.
#Despues entregara un output de las cordenadas, por las cuales paso el laberinto.
#Tiene que haber una entrada a la izquierda, y tambien una salida a la derecha. 

import sys
import numpy as np

#((1+len(open('input.txt','r').read()))/2)**(0.5)

def main(laberinto):
    laberinto = np.zeros(int(((1+len(open('input.txt','r').read()))/2)**(0.5), int((1+len(open('input.txt','r').read()))/2)**(0.5)), dtype=int)
    for x in open('input.txt','r').read():
        n,m=0,0
        if x == "1":
            laberinto[n,m] = 1
            n =+1
        if x == "0":
            laberinto[n,m] = 0
            n =+1
        if x == "\n":
            m =+1
            n = 0
    print(laberinto)
x=0
main(x)
