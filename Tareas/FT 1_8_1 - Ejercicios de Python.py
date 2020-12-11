
# Realizar un programa que determina el mayor de 3 números.

numeros=[]
numero=1
while numero!=0 :
    numero=int(input("Dame un num: (0 para salir) "))
    numeros.append(numero)
mayor=max(numeros)
print(mayor)


# Realizar un programa que solicite al usuario el número de horas y el 
# precio por hora y calcule el salario bruto, teniendo en cuenta que las 
# horas que sobrepasen 40 se considerarán extra y pagadas a 1,5 veces el precio de la hora regular.

horas=int(input("Horas trabajadas?: "))
tarifa=int(input("Precio por hora?: "))
if horas>40:
    salario=(40*tarifa) + ((horas-40)*tarifa*1.5)
else: salario=horas*tarifa

print(salario)


# Realizar un programa que solicite números al usuario hasta que 
# introduzca el -9999 y mostrar entonces la media de los números introducidos.

numero=contador=total=0

while numero != -9999:
        numero=int(input("Dame un num (-9999 para salir): "))
        if numero != -9999:
            total=total+numero
            contador+=1
print("La media es: ", total/contador)
