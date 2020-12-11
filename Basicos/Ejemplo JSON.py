import json

datos = {
    "nombre":"Zoltan",
    "email":"zs@ese.com",
    "edad":40
}

#Con el método dumps pasamos una variable a formato json
formato_json=json.dumps(datos)
print(formato_json)

#Escritura en un archivo

with open("datos.json","w") as f: json.dump(datos,f)


#Lectura de un archivo JSON
with open("datos.json","r") as f: lectura_json=json.load(f)

print(lectura_json)

  
