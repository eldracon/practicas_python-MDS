
# JUEGO DE TRONOS

import random
import time
import textwrap


def enunciado ():
    ancho=110
    print("\n")
    linea="-"*ancho
    print(linea)
    storytelling =  "Perteneces a la Guardia de la Noche."\
                    "Llevas semanas andando al otro lado del muro,"\
                    "en una expedición para detectar posibles salvajes."\
                    "Llegas a un poblado con 5 cabañas."\
                    "Debes elegir en qué cabaña entrarás."\
                    "Si está vacía podrás descansar... pero"\
                    "corres el riesgo de encontrarte con un salvaje y morir…"



def rellenar_cabanas () :
    estado_cabana=("enemigo","vacía","amigo")
    cabanas_totales=5
    poblado=[]
    for i in range (cabanas_totales):
        cabana=random.choice(estado_cabana)
        poblado.append(cabana)
    return poblado


def selecciona_cabana () :
    seleccion=0
    while (seleccion<=0) or (seleccion>5):
        try: seleccion=int(input("Elige una cabaña (1-5): "))
        except ValueError:
            seleccion=0
    return seleccion


def resultado () :
    seleccion=selecciona_cabana()
    lista_cabanas=rellenar_cabanas()
    
    if lista_cabanas[seleccion-1]=="enemigo": print("\nHas muerto!!")
    else : print("\nVives.")
    


def juego() :
    enunciado()
    seguir="S"
    while seguir == "S":
        resultado()
        seguir=input("¿Quieres seguir jugando (S/N): ").upper()
        


if __name__ == "__main__":
    juego()
    

