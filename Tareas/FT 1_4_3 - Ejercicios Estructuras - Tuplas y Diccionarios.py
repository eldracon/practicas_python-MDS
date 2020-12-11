## Crea un diccionario (currences) que contenga el nombre de los países y su moneda. A
## continuación, mostrar los países que tiene el diccionario y solicitar al usuario escriba
## alguno de esos países para mostrarle la moneda


#paises=["España","Inglaterra","EEUU"]
#currences={paises[0]:"Euro",paises[1]:"Libra",paises[2]:"dolar"}
#print("Estos son los paises que tengo en mi diccionario: ", paises)
#pais=input("¿Que país quieres consultar?: ")
#indice=paises.index(pais)
#print("La mondea de {a} es {b}" .format(a=pais,b=currences[paises[indice]]))

#input("Presiona una tecla para seguir...")
#Crea un diccionario users que contenga la información de los usuarios de una
#aplicación, donde se distingue cada usuario por un nombre de usuario único. Escribe
#hasta 3 usuarios y muestralo por pantalla.

#### PENDIENTE VER COMO ASIGNAR LISTAS A DICCIONARIOS

id_usuario=[]
nombre_usuario=[]
continuar="Si"
contador=0

while continuar=="Si" or contador<3:
    nombre_usuario.append(input("Dime tu nombre: "))
   
    id_usuario.append(input("Dime tu ID: "))

    contador=contador+1
    if(contador>=3):
        continuar=input("Deseas continuar metiendo datos(Si/No): ")


users=dict.fromkeys("Nombre","Identificador")
print(users)
users["Nombre"]="Pepe"
users["Identificador"]=100


print(users,type(users))
