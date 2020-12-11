
# JUEGO DE TRONOS

import random
import time
import textwrap


def enunciado ():
    """ OBJ: Presentar el enunciado del juego"""
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
    print(storytelling)




def rellenar_cabanas () :
    """ OBJ: Rellena el poblaco con cabañas vacías, amigos o enemigos"""
    estado_cabana=("enemigo","vacía","amigo")
    cabanas_totales=5
    poblado=[]
    for i in range (cabanas_totales):
        cabana=random.choice(estado_cabana)
        poblado.append(cabana)
    print(poblado)
    return poblado




def selecciona_cabana () :
    seleccion=0
    while (seleccion<=0) or (seleccion>5):
        try: seleccion=int(input("Elige una cabaña (1-5): "))
        except ValueError:
            seleccion=0
    return seleccion




def atacar():
    tipos_ataque=("acierto","fallo")
    golpe_guardian=golpe_salvaje=0
    valor_golpe=random.randint(10,15)
    print("Valor golpe: ",valor_golpe)
    ataque_guardian=random.choices(tipos_ataque,weights=(60,40),k=1)
    ataque_salvaje=random.choices(tipos_ataque,weights=(40,60),k=1)
    print("El guardian tiene un ",ataque_guardian," en su ataque")
    print("El salvaje tiene un ",ataque_salvaje," en su ataque")
    
    if ataque_guardian[0] == "acierto" : 
        print("Ataque del guardian: ",valor_golpe)
        golpe_guardian=valor_golpe
    
    if ataque_salvaje [0]=="acierto" : 
        golpe_salvaje=valor_golpe
        print("Ataque del salvaje: ",valor_golpe)
        
    input("Pulsa tecla para iniciar una nueva ronda... ")
    
    return (golpe_guardian,golpe_salvaje)
    


def luchar():
    vida_personajes = {"guardian":50,"salvaje":40}
    salir=1
    while vida_personajes["guardian"]>0 and vida_personajes ["salvaje"]>0 and salir!=0 :
        print("\n--------------------------")
        input()
        print("Vida guardian", vida_personajes["guardian"])
        print("Vida salvaje", vida_personajes["salvaje"])
        combatir=input("¿Deseas seguir luchando? (S/N): ").upper()
        if combatir == "S":
            golpe_guardian,golpe_salvaje=atacar()
            vida_personajes["guardian"]-=golpe_salvaje
            vida_personajes["salvaje"]-=golpe_guardian
        else: salir=0

    if salir==0 : print("Gano el salvaje porque el guardián huyo")
    elif vida_personajes["guardian"] > 0 : print("Gano el guardian")
    
    else: print("Gano el salvaje")



def genera_encuentro () :
    lista_cabanas=rellenar_cabanas()
    seleccion=selecciona_cabana()
    
    if lista_cabanas[seleccion-1]=="enemigo": 
        combatir=input("\nTe encuentras un enemigo. ¿Quieres luchar? (S/N): ").upper()
        if combatir=="S": luchar()
        else : print ("Has perdido por cobarde ¡¡")
   
    else : print("\n Vives.")
    




def juego() :
    enunciado()
    seguir="S"
    while seguir == "S":
        genera_encuentro()
        seguir=input("¿Quieres seguir jugando (S/N): ").upper()
        


if __name__ == "__main__":
    juego()
    

