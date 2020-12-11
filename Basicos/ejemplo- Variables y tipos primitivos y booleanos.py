numero = 10
print(numero)
print("Tu numero es %i" %numero)
print("Tu numero es",numero)
num1, num2, mensaje = 5,89, "hola"
salida = continuar = True
print (num1)
print (num2)
print (mensaje)
print (salida,continuar)
print("Tipo a mostrar")
print(type(num1))
print(type(mensaje))

flotante_1, flotante_2 = 0.543, 1.5e2
real= 0.56e-3
print(real,type(real))
complejo=3.14j
print(complejo,complejo.imag,complejo.real)
print(complex(real))
print(bool(0))
print(False == False)
aT=True
aF=False
# Salto de pagina \n
print("Comprobacion de boleanos: La variable aT es", aT, "\n", type(aT))
# Las cadenas de texto se pueden referenciar con " "  o ' '
# \t es un tabulador
# Codigo en varias lineas = """"
cadena_larga = """Linea 1
Linea 2
Linea N"""
print(cadena_larga)
#Repeticion de texto
multiple_cad_larg= cadena_larga *3
print(multiple_cad_larg)
# la Funcion LEN nos devuelve el numer de caracteres
texto_a_segmentar = "Esto es un Texto que se segmentará"
texto_segmentado = texto_a_segmentar[1:len(texto_a_segmentar):2]
print("El numero complejo es {param_a} y la cadena segmentada es \n {param_b}" .format(param_a=complejo,param_b=texto_segmentado))
