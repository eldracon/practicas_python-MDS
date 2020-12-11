sssoo=("Mac","Win","Lin")
print(sssoo[0])
vocal_lista=["a","e","i","o","u"]
vocal_tupla=("a","e","i","o","u")
print(vocal_lista,type(vocal_lista))
print(vocal_tupla,type(vocal_tupla))

## Para crear una tupla con un elemento tenemos que terminar en ,
no_tupla=("Python")
tupla=("Python",)
print(no_tupla,type(no_tupla))
print(tupla,type(tupla))

tupla_simple = ("Pepe","Juan",10,1.55)
print(tupla_simple)
tupla_anidada = tupla_simple,("Vino","Cerveza",1534)
print(tupla_anidada)

## Puedo volcar los valores de las tuplas en variables
posi1,posi2,posi3,posi4=tupla_simple
print(posi1)
