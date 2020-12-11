print ("Hola desde VS sin depurar")
# Esto es un comentario
print ("Cadena1"); print("Cadena2")
# puedo dividir lineas largas con \
print("Este es un mensaje de cadena larga que \
    dividimos en dos lineas")
nombre = input("Cual es tu nombre?")
#Con el operado + estamos concatenando cadenas
print("Te llamas "+nombre)
print(nombre)
#Puedo indicar la variable cadena con %s
print("Hola %s" %nombre)
numero = 19 #ejemplo de integer
# La función STR convierte INT en STR
print("El numero es " + str(numero))
print("El numero tb es %i" %numero)
print ("Tambien el numero es ",numero)
altura=1.38
print("Altura es %f" %altura)
print("Altura",altura)
#Con %.1f --> indico el numero de decimales
print("%s tiene %.1f altura" %(nombre,altura))

#modificamos la variable
nombre="Pepito"
#otra forma de escribir variables es con .format (nombre variables)
print("Mi nombre es {} tengo {} años y mido {}".format(nombre,numero,altura))
print("Numero",numero)
print("Nombre",nombre)