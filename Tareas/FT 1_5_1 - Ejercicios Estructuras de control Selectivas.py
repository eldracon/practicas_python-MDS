# EJ 1 Pedir la edad al usuario e indicar si es mayor de edad o no. Establecer como constante el valor de mayor de edad
mayor_edad = 18
edad = int(input("¿Cuantos años tienes?: "))
if edad > mayor_edad:
    print("Eres mayor de Edad")
else:
    print("Eres menor")

# EJ 2 Crea una lista favorite_movies con los valores ‘Iron Man’, ‘Captain America’, ‘Avengers’. 
# Pide al usuario el nombre de una película. Deberás comprobar si su película coincide con alguna de la lista. 
# Si es así se mostrará el mensaje “A los dos nos gusta la misma película: nombre peli”. Sino coincide se mostrará el mensaje “No nos gustan las mismas películas.

# EJ 3 ¿Qué sucede si la película que escribe el usuario está en minúsculas o mayúculas? Depura el programa para que coincida con los textos escritos en la lista

favourite_movies = ["Iron Man", "Captain America", "Avengers"]
peli=input("¿Dime una película?: ")
pelicula=peli.title()
encontrado=False
indice=0
for i in favourite_movies:
    if pelicula == favourite_movies[indice]: 
        print("A los dos nos gusta: ",favourite_movies[indice])
        encontrado=True
    indice=indice+1
if not encontrado: print("No nos gustan las mismas pelis.")

#EJ 4 La entrada a un museo dependerá de la edad del visitante. Si es menor de 4 años el acceso será gratuito, hasta 12 años pagará 4,5€, a partir de 12 años será como un
# adulto y la entrada será 8€. Realiza un programa en Python que solicite la edad al visitante y le calcule el precio de la entrada.
edad = int(input("¿Cuantos años tienes?: "))
if edad < 4 : precio=0
elif edad <12 : precio=4.5
else : precio=8
print("Por tener {a} años tienes que pagar {b} euros" .format(a=edad,b=precio))

# EJ 5 Solicitar la edad al usuario y en función de esta le mostraremos un mensaje:
#a. Menores de 2 años: “¡Eres un bebe!”
#b. Menores de 4 años: “¡Eres un crí@!”
#c. Menores de 13 años: “¡Eres un niñ@!”
#d. Menores de 20 años:”¡Eres un adolescente”!
#e. Menores de 65: “¡Eres adulto!”
#f. Resto: “Eres un ancian@”

edad = int(input("¿Cuantos años tienes?: "))
if edad <2 : print("Bebe")
elif edad<4 : print("Crio")
elif edad <13 : print("Niño")
elif edad < 20 : print ("Adolescente")
elif edad < 65: print ("Adulto")
else: print ("Anciano")

#EJ 6 Escribe del 1 al 9 la siguiente salida, utilizando un bucle for y if-elif-else
# 1st 2nd 3rd 4th 5th 6th 7th 8th 9th
for i in range(1,9):
    if i==1: print("%ist"%i)
    elif i==2: print("%ind"%i)
    elif i==3: print("%ird"%i)
    else: print("%ith"%i)