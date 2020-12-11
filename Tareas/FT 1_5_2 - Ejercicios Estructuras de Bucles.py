

#Ejercicios con Range
#1. Utiliza un bucle for para mostrar por pantalla los números del 1 al 20
#2. Mostrar por pantalla los números del 3 al 30 de 3 en 3.
#3. Crea una lista de números del 3 al 30 de 3 en 3 y muestra por pantalla
#4. Mostrar por pantalla el cubo de los números del 1 al 10. Guardar en una lista cubes el cubo de cada número. 
# Mostrar la lista

for i in range(1,21): print(i)
for i in range(3,31,3): print(i)

lista=[]
for i in range(3,31,3): lista.append(i)
print(lista)

cubes=[]
for i in range(1,11):
    cubo=i**3
    cubes.append(cubo)
print(cubes)


input("PULSA TECLA PARA CONTINUAR ***********")

#Pide un número al usuario y muestra su tabla de multiplicar. 
numero=int(input("Dame nº: "))
for i in range (1,11): print(numero, " * ", i, " es ",numero*i)

#Pregunta al usuario su nombre y cuántas veces desea que le saludes. A continuación,
#muestra el mensaje “Hola nombre_usuario” tantas veces como haya indicado.
nombre= input ("nombre? ")
repeticion = int(input("Veces saludo? "))
i=0
for i in range (repeticion) :
    print ("Hola ",nombre)


#3. Suma los 100 primeros números y muestra el resultado por pantalla.
i=total=0
for i in range(1,101): total+=i
print(total)


#4. Pide números al usuario hasta que escriba un número negativo. Mostrar al final
#cuántos números positivos escribió
negativo=False
num_pos=[]
while negativo==False:
    numero=int(input("dame numero: "))
    if numero < 0 : negativo=True
    else : num_pos.append(numero)
print(num_pos)

#5. Para acceder a una aplicación se deberá escribir el nombre de usuario admin y la
#contraseña 1234&. Hasta que el usuario no escriba la contraseña correcta o haya
#agotado 3 intentos se le solicitará el user y password.
intentos=1
contraseña="1234&"
acierto=False
while (acierto==False) and (intentos<=3):
    clave=input("Dime la pass:")
    if clave == contraseña : 
        acierto=True
        print("Acertaste ¡¡")
    intentos+=1
if(acierto==False): print("Fallaste los 3 intentos")

# 6 . Crea la lista magicians con los valores ‘alice’, ‘carolina’, ‘anne’. Muestralo por pantalla de una forma iterativa
magicians=["alice","carolina","anne"]
for a in magicians: print (a)

# Crea una lista favorite_ingredients con los valores ‘pepperoni’, ‘hawaiian’, ‘veggie’ correspondientes a los ingredientes favoritos de una pizza.
#  Usa un bucle for para mostrar los elementos.
# a. Modifica el for para que muestre el mensaje ‘I love xx in pizza’ 
# b. Al final mostrar ‘I love all pizzas’

favorite_ingredients=["pepperoni","hawaiian","veggie"]
for a in favorite_ingredients: print("I love",a)
print("I love ell pizzas")

#Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre
#1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra
#un mensaje de error. El programa termina cuando el usuario introduce un cero


meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
entrada=13
maximo=len(meses)
while (entrada !=0):
    entrada=int(input("Escribe un n del 1 al 12: "))
    if (entrada>0) and (entrada<=maximo): print(meses[entrada-1])
    else : print("mes erroneo")
