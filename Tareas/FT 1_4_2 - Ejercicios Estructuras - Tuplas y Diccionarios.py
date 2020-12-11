## EJ1  Crea la tupla dimensions con los valores 100 y 200. Muestra por pantalla la tupla y su tipo
dimensions=(100,200)
print(dimensions,type(dimensions))
print(dimensions[0],type(dimensions[0]))
## EJ3 . Muestra todos los elementos de la tupla. Utiliza un bucle. (Deja este ejercicios paracuando aprendamos bucles)
for a in dimensions:
    print(a)


#EJERCICIOS DICCIONARIOS
# Solicita al usuario su nombre, dirección, edad, teléfono y guárdalo en un diccionario person. 
# A continuación, muestra por pantalla el texto: <nombre> tiene <edad>años, vive en <dirección> y su número de teléfono es <teléfono>

#Inicializamos el diccionario con los atributos
atributos=["nombre","edad","dirección","teléfono"]
#grabamos el valor none en el diccionario
person={clave: None for clave in atributos}
print("Atributo vacío nombre", person["nombre"])

#otra forma de inicializarlo a none es con el método 
person=dict.fromkeys(atributos)
print("Atributo vacío nombre", person["nombre"])

person["nombre"]=input("Dime tu nombre: ")
person["edad"]=input("Dime tu edad: ")
person["dirección"]=input("Dime tu dirección: ")
person["teléfono"]=input("Dime tu tel: ")

print("{a} tiene {b}, vive en {c} y su teléfono es {d}" .format(a=person["nombre"],b=person["edad"],c=person["dirección"],d=person["teléfono"]))


## Crea un diccionario vacio person y rellénalo con la información de una persona. Para ello, será consultando al usuario el dato que quiere guardar y el valor. 
#¿Qué dato quieres introducir? Nombre
#Nombre: Juan López
#{'Nombre': Juan López'}
#¿Quieres añadir más información (Si/No)? Si
#¿Qué dato quieres introducir? Dirección
#Dirección: Barcelona
#{'Nombre': 'Juan López', 'Dirección': 'Barcelona'}
#¿Quieres añadir más información (Si/No)? Si
#¿Qué dato quieres introducir? email
#email: jlopezz@kk.com
#{'Nombre': Juan López', 'Dirección': 'Barcelona', 'email':
#'jlopezz@kk.com'}
#¿Quieres añadir más información (Si/No)? No


atributos=["nombre","dirección","email"]
person=dict.fromkeys(atributos)
continuar="Si"

while continuar == "Si":
    tipo_dato=input("¿Que dato quieres introducir?(Nombre, Dirección, Email)")
    if(tipo_dato=="Nombre"):
        person["nombre"]=input("Dime el nombre: ")
    if(tipo_dato=="Dirección"):
        person["dirección"]=input("Dime la Dirección: ")
    if(tipo_dato=="Email"):
        person["email"]=input("Dime el email: ")
        
    continuar= input("¿Quieres añadir más información (Si/No)?")

print(person)

