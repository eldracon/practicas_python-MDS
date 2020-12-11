factura = ["huevos", "pan",10,50, "pan" ] #creación de una lista con valores
print(factura)
factura.append("leche")
personas = ["Maria", "Pedro", "Juan"]
factura.append(personas)
print (factura)
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
sublista=numeros[5:]
sublistas2=numeros[1::2]
print(sublista)
print(sublistas2)
fact_texto = str(factura)
print (fact_texto)
print("Tu lista contiene", factura)
print("El primer elemento de tu lista es {p_a} y el quint es {p_b} y la sublista 2º es {p_c}" .format(p_a=factura[0],p_b=factura[5],p_c=factura[6][1]))
## Sacamos el penultimo por el final
print(factura[-2])
##Machacamos valor
factura[0]="Pepito"
print(factura[0])
cola=factura.pop()
print(cola)

