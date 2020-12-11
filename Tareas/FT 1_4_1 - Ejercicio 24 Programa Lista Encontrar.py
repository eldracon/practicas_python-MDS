## Crea un programa en Python que tenga dos listas vowels con las vocales y found con
## las vocales que se encuentren en una palabra que se solicite al usuario. Mostrar el
## contenido de found
palabra=input("Escribe tu palabra:")
vowels=["a","e","i","o","u"]
palabra_lista= list(palabra)
## print(palabra_lista, type(palabra_lista))
vowels_set=set(vowels)
found = vowels_set.intersection(palabra_lista)
print(found)
