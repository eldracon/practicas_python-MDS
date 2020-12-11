# JUEGO DE TRONOS

print("\n \nEl guardián lleva semanas andando al otro lado del muro, en una expedición  para detectar posibles salvajes.") 
print("Está agotado, pero está llegando a un poblado con 5 cabañas. Deberá elegir una cabaña.")
print("Si está vacía podrá descansar... pero corre el riesgo de encontrarse con un salvaje y morir…")

import random

seguir="S"

while seguir == "S":
    estado_cabana=("enemigo","vacía","amigo")
    lista_cabanas=[]
    for i in range (5):
        cabana=random.choice(estado_cabana)
        lista_cabanas.append(cabana)
#    print (lista_cabanas)

    seleccion=0
    while (seleccion<=0) or (seleccion>5):
        try: seleccion=int(input("Elige una cabaña (1-5): "))
        except ValueError:
            seleccion=0
        
    if lista_cabanas[seleccion-1]=="enemigo": print("Has muerto!!")
    else : print("Vives.")
    seguir=input("¿Quieres seguir jugando (S/N)?: ").upper()
