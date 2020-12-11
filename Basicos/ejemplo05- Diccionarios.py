datos_basicos = {
 "nombres":"Leonardo Jose",
 "apellidos":"Caballero Garcia",
 "clave":"26938401",
 "fecha_nacimiento":"03/12/1980",
 "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
 "nacionalidad":"Venezolana",
 "estado_civil":"Soltero"
}
print (datos_basicos, type(datos_basicos))
print ("\nDetalle del diccionario")
print ("=======================")
print ("\nClaves de diccionario:", datos_basicos.keys())
print ("\nValores de diccionario:", datos_basicos.values())
print ("\nDatos de participante")
print ("---------------------")
print ("Clave de identidad: ", datos_basicos['clave'])
print ("Nombre completo: " + datos_basicos['nombres'] + " ")
dni=datos_basicos.get("clave")
print(dni)
