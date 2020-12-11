# Range(inicio,fin,saltos)
for i in range(0,10,2): print("%i es par"%i)

words=["perro","gato","periquito"]
for w in words: 
    print(w, end = " / ")
print("\n")

colegas=["Isma","Fran","Ivan"]
for amigo in colegas:
    invitado=amigo + " te espero en mi fiesta"
    print(invitado)

# Mostrar los resultados de multiplicar tablas pares

for i in range(2,11,2):
    for j in range(1,11):
        multiplicacion= i * j
        print (i, " * ", j ,"es = " ,multiplicacion)

# Pedir numeros hasta que escriba par

par = False
while par == False :
    numero=int(input("Dame num: "))
    if (numero%2 == 0) : par=True

# Guardar en una lista las vocales encontradas
vocales = ["a","e","i","o","u"]
palabra=input("Dame una palabra: ")
vocales_encontradas=[]

for letra in palabra:
    for vocal in vocales:
       if (letra in vocal) : 
           vocales_encontradas.append(letra)
           print(letra," es una vocal")
for vocal in vocales_encontradas:
    print(vocal, " es una vocal almacenada.")