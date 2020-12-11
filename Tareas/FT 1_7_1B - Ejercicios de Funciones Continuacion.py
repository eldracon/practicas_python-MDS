#7 Define una función que convierta radianes en grados (recuerda que 360 grados son 2П radianes.)

#8 Escribe un programa modularizado que solicite al usuario una hora en formato [hora, minutos y segundos] y utilizando una función que calcule el número 
# total de segundos transcurridos desde la última medianoche, lo muestre posteriormente por pantalla.


#9 Escribe un programa que lea una longitud en kilómetros y muestre su equivalencia en Hm, Dm y m utilizando una función para cada cálculo.

#10 Escribe una función que determine si un punto de coordenadas en 2D está o no sobre la circunferencia x2+y2=1000.

#11 El antiguo sistema anglosajón de unidades sigue en vigor en muchos lugares y su uso es frecuente en algunos contextos. Programa una función que 
# determine el número de pintas que contiene una cierta cantidad de líquido expresada en mililitros, sabiendo que 1 pinta (pt) = 473,176473 ml.

#12 Escribe un programa que muestre por pantalla la tabla de multiplicar de un número dado invocando para ello una función a la que le pasará dicho número.
# Utilice el siguiente formato (ejemplo para la tabla del 1):
# 1 x 1 = 1
# 1 x 2 = 2


#13 Escribe una función que a partir de las coordenadas 3D de dos puntos en el espacio en formato (x, y, z) calcule la distancia que hay entre dichos puntos. 
# Prueba su función y el resultado por pantalla. NOTA: ¿qué sucede su A(4,4,4) y B(2,2,2)? Captura la excepción de realizar la raíz cuadrada de un nº negativo

#14 Un año es bisiesto si es divisible por 400 o si lo es por 4 pero no por 100. Programa una función que reciba un año y decida si es o no bisiesto. 



## MODULOS **********************************************
## MODULOS **********************************************

def radianes_en_grados(radianes):
    """ float --> float
    OBJ: Define una función que convierta radianes en grados"""
    import math
    pi=math.pi
    grados =180*radianes/pi
    return grados

def segundos_medianoche (h,m,s):
    segundos=(h*60*60)+(m*60)+s
    return segundos

def hectometros (kilometros):
    hm=kilometros*10
    return hm

def decimetros (kilometros):
    dm=kilometros*100
    return dm

def distancia_3d (x,y,z,u,v,w):
    import math

    valor_raiz=(u-x)+(v-y)+(w-z)
    try:
        distancia = math.sqrt(valor_raiz)
    except ValueError : 
        print("Las coordenadas del pto B tienen que ser mayores que del pto A")
        distancia=0
    return distancia


## PROGRAMA PRINCIPAL **********************************************
## PROGRAMA PRINCIPAL **********************************************


#7
radianes=float(input("Introduce los radianes: "))
print("Los grados correspondientes son: ",radianes_en_grados(radianes))

#8
a,b,c=input("Introduce las HH:MM:SS ").split(":")
horas=int(a)
minutos=int(b)
segundos=int(c)
print("Han pasado: ",segundos_medianoche(horas,minutos,segundos)," segundos.")

#9
kilometros=int(input("Dame Km: "))
print("Tus KM en Hectómetros son: ",hectometros(kilometros), "y en Decímetros son: ", decimetros(kilometros))

#10 Coordenadas. PENDIENTE

#11 Pintas. PENDIENTE

#12 Tabla multiplicar. PENDIENTE

#13 
x,y,z=input("Introduce el punto A  x,y,z ").split(",")
x=int(x)
y=int(y)
z=int(z)
u,v,w=input("Introduce el punto B  x,y,z ").split(",")
u=int(u)
v=int(v)
w=int(w)
if(distancia_3d(x,y,z,u,v,w) !=0): print("La distancia entre ambos puntos es: ", distancia_3d(x,y,z,u,v,w))
#Pendiente gestion excepciones

#14
año=int(input("Dime un año: "))
if año%400 == 0 : print("El año es bisiesto.")
elif  (año%4 == 0) and (año%100 !=0) : print("El año es bisiesto.")
else: print("No es Bisiesto")