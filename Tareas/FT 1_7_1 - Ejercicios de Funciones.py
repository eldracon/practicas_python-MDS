
#ENUNCIADOS

# 1. Programa una función que determine si un número entero es impar.

# 2 . Escribe una función que calcule el impuesto que debe pagar un contribuyente a partir
#de sus ingresos anuales y el número de hijos. El impuesto a pagar es un tercio del
#ingreso imponible, siendo este último igual a los ingresos totales menos una deducción
#personal de 600€, a lo que se ha de añadir otra deducción de 60€ por hijo

# 3 Escribe un programa modularizado que, utilizando funciones, calcule el perímetro y el
# área de un círculo cuyo radio es proporcionado por el usuario.

# 4 Implementa una función “fuerza” que retorne el valor de la fuerza en función de los valores de masa y aceleración recibidos como parámetros. Implementa,
# posteriormente, un programa probador que, leyendo de teclado los valores necesarios, invoque a la función “fuerza” y muestre por pantalla el valor de la 
# fuerza a partir de una masa y aceleración dadas.


#5 Implementa un programa modularizado que, leyendo de teclado los valores necesarios calcule el área de distintas figuras geométrica. Para ello, se le
# presentará un menú en el que pueda elegir la figura, se le pidan los datos para cada caso y se muestre el resultado 
# 1. Circulo    # 2. Cuadrado   # 3. Triángulo  Pulsa de 1 a 4 la figura:
# Nota: importa el módulo math para poder usar PI
# import math
# math.PI

#6 Implementa un programa modularizado que, leyendo la nota obtenida por tres
# alumnos en una asignatura, muestre por pantalla la media de las notas.

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



## MODULOS ***************************************************************************************************
def esPAR (a):
    """int --> bool
    OBJ: Determinar si el número pasado cómo argumento es par y devolver true or false
    PRE: Nada """

    if (a%2==0) : par=True
    else: par=False
    return par

def impuesto (ingresos,hijos):
    """int,inte ---> float
    OBJ: Calcular los impuestos en función de ingresos e hijos
    PRE: Ingresos e Hijos >=0"""
    tasas=(ingresos- 600 -60*hijos)/3
    return tasas

def area_circulo (radio):
    import math
    pi=math.pi
    area=pi * radio**2
    return area

def perimetro_circulo (radio):
    perimetro=3.1416 * radio*2
    return perimetro


def fuerza (masa,aceleracion):
    """ float,float --> float
    OBJ: Calcula la fuerza cómo el producto de la masa por la aceleración
    PRE: masa,aceleracion >=0"""
    fuerza = masa*aceleracion
    return fuerza

def area__cuadrado (lado):
    """ float --> float
    OBJ: Devuelve el área de un cuadrado a partir de su lado"""
    area=lado*lado
    return area

def area__triangulo (base,altura):
    """ float,float --> float
    OBJ: Devuelve el área de un triangulo a partir de su base y altura"""
    area=base*altura/2
    return area



def menu_area (seleccion):
    """ int --> float
    OBJ: Menú para seleccionar que área queremos calcular en función de la opción que seleccione el usuario
    PRE: seleccion = 1,2 o 3"""
    
    if (seleccion==1):
        radio=float(input("Introduzca el radio del círculo: "))
        area=area_circulo(radio)
    elif (seleccion==2):
        lado=float(input("Introduzca el lado del cuadrado: "))
        area=area__cuadrado(lado)
    elif (seleccion==3):
        base=float(input("Introduzca la base del traingulo: "))
        altura=float(input("Introduzca la altura del triangulo: "))
        area=area__triangulo(base,altura)
    return area


def nota_media (nota_alumno1,nota_alumno2,nota_alumno3):
    media =(nota_alumno1+nota_alumno2+nota_alumno3)/3
    return media


## PROGRAMA PRINCIPAL **********************************************************************
## PROGRAMA PRINCIPAL **********************************************************************

#1
numero=int(input("Dame un numero: "))
if esPAR(numero): print("Es par")
else: print("Es impar")

#2
sueldo=int(input("¿Cuanto ganas? "))
hijos=int(input("¿Cuantos hijos tienes? "))
print("Debes a hacienda",impuesto(sueldo,hijos))


#3 Area = PI*r^2 Perimetro= 2*PI*r
radio=float(input("Dame un radio: "))
print("El área es", area_circulo(radio), " y el perímetro es ",perimetro_circulo(radio))

#4 Fuerza = m*a
masa=float(input("Masa?: "))
aceleracion=float(input("Aceleracion?: "))
print("La fuerza es: ", fuerza(masa,aceleracion))


#5 Implementa un programa modularizado que, leyendo de teclado los valores necesarios calcule el área de distintas figuras geométrica.

seleccion=int(input("1. Circulo     2. Cuadrado   3. Triángulo (1/2/3): "))
print("El area de la figura es: ", menu_area(seleccion))


# Nota media de 3 alumnos
nota1=float(input("Introduce la nota del alumno 1: "))
nota2=float(input("Introduce la nota del alumno 2: "))
nota3=float(input("Introduce la nota del alumno 3: "))
print("La nota media es: ",nota_media(nota1,nota2,nota3))
