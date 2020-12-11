
# JUEGO DE TRONOS
# Si se encuentra un amigo, le da un pócima de fortaleza que le da 30 puntos de vida más al guardían
# Si se encuentra la cabaña derruida (vacía), el guardían se cansa y empieza el combate con 30 ptos de vida menos

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
                    "\nLlegas a un poblado con varias cabañas."\
                    "Debes elegir en qué cabaña entrarás."\
                    
                    
    print(storytelling)




def rellenar_cabanas () :
    """ OBJ: Rellena el poblaco con cabañas vacías, amigos o enemigos"""
    estado_cabana=("enemigo","vacía","amigo")
    
    cabanas_totales=int(input("Selecciona el número de cabañas que tiene el poblado: "))
    
    poblado=[]
    for i in range (cabanas_totales):
        cabana=random.choice(estado_cabana)
        poblado.append(cabana)
    print(poblado)
    return poblado,cabanas_totales

def crear_personajes ():
    armas=("espada","hacha","cuchillo")
    guardian={"vida":50,"arma":armas[0],"estado":"normal"}
    salvaje={"vida":40,"arma":armas[0],"estado":"normal"}
    
    return guardian,salvaje,armas


def golpe_danyo (guardian,salvaje):
    tipos_ataque=("acierto","fallo")
    if guardian["arma"] == "espada" : 
        ataque_guardian=random.choices(tipos_ataque,weights=(50,50),k=1)
        danyo_guardian=random.randint(8,12)
    elif guardian["arma"] == "hacha" : 
        ataque_guardian=random.choices(tipos_ataque,weights=(40,60),k=1)
        danyo_guardian=random.randint(6,15)
    else :    
        ataque_guardian=random.choices(tipos_ataque,weights=(65,35),k=1)
        danyo_guardian=random.randint(5,9)

    if salvaje["arma"] == "espada" : 
        ataque_salvaje=random.choices(tipos_ataque,weights=(50,50),k=1)
        danyo_salvaje=random.randint(8,12)
    elif guardian["arma"] == "hacha" : 
        ataque_salvaje=random.choices(tipos_ataque,weights=(40,60),k=1)
        danyo_salvaje=random.randint(6,15)
    else :    
        ataque_salvaje=random.choices(tipos_ataque,weights=(65,35),k=1)
        danyo_salvaje=random.randint(5,9)
    
    return ataque_guardian,danyo_guardian,ataque_salvaje,danyo_salvaje


def luchar(guardian,salvaje):

        
    salir=1
    
    while guardian["vida"]>0 and salvaje ["vida"]>0 and salir!=0 :
        print("\n--------------------------")
        print("Vida del guardian: ", guardian["vida"]," Vida del salvaje: ",salvaje["vida"])
        
        combatir=input("¿Deseas seguir luchando? (S/N): ").upper()
        if combatir == "S":
            ataque_guardian,danyo_guardian,ataque_salvaje,danyo_salvaje=golpe_danyo(guardian,salvaje)
            
            if ataque_guardian[0] == "acierto" : 
                print("El Guardia de la Noche golpea al Wildling haciendo ",danyo_guardian, "puntos de daño, con su ",guardian["arma"])
                salvaje["vida"]-=danyo_guardian
            elif ataque_salvaje[0] == "acierto" : 
                print("El Wildling golpea al Guardian con su arma, haciendo",danyo_salvaje, "puntos de daño.")
                guardian["vida"]-=danyo_salvaje
            else :print("Ninguno de los combatientes acierta el golpe...")
                        
            
        else: salir=0

    if salir==0 : print("Gano el salvaje porque el guardián huyo")
    elif guardian["vida"] > 0 : print("Gano el guardian")
    
    else: print("Gano el salvaje")








def genera_encuentro (poblado,cabanas_totales) :
    seleccion=0
    guardian,salvaje,armas=crear_personajes()
    while (seleccion<=0) or (seleccion>cabanas_totales):
        try: seleccion=int(input("Elige una cabaña (1-X): "))
        except ValueError:
            seleccion=0
        

        if poblado[seleccion-1] == "amigo" : 
            print("Encuentras un amigo que te ofrece un hacha o un cuchillo a cambio de tu espada")
            print("Estadisticas:")
            print("1.- Espada (Arma Actual). Probabilidad de Impacto 50% , Daño 8-12")
            print("2.- Hacha. Probabilidad de Impacto 40% , Daño 6-15")
            print("3.- Daga. Probabilidad de Impacto 65% , Daño 5-9")
            eleccion=int(input("Elige un arma (1-3): "))
            if eleccion==2 : guardian["arma"]=armas[1]
            
            elif eleccion==3 : 
                guardian["arma"]=armas[2]
                print("Después de haber seleccionado el arma, tu amigo te indica dónde hay un enemigo...")
                luchar(guardian,salvaje)

            
        elif poblado[seleccion-1] == "enemigo" : 
            print("Arma=",guardian["arma"])
            luchar(guardian,salvaje)
        else : print("La cabaña está vacía")

        
    return seleccion






def juego() :
    enunciado()
    seguir="S"
    while seguir == "S":
        poblado,cabanas_totales=rellenar_cabanas()
        genera_encuentro(poblado,cabanas_totales)
        seguir=input("\n¿Quieres seguir jugando (S/N): ").upper()
        



if __name__ == "__main__":
    juego()
    

