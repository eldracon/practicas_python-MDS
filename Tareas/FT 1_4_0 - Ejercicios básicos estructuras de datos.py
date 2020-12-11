######## LISTAS
##1
bicycles=["trek", "cannondale","redline","specialized"]
print(bicycles,type(bicycles))
##2
print(bicycles[1])
##3
print(bicycles[1].title())
##4
print(bicycles[-1])
##5
print("My first bicycle was a {p_a}." .format(p_a=bicycles[0].title()))
##6
motorcycles =["honda", "yamaha", "suzuki"]
print(motorcycles)
##7
motorcycles[0]="ducati"
##8
motorcycles[-1]="honda"
print(motorcycles)
##9
motorcycles.remove("ducati")
print(motorcycles)
##10
motorcycles.insert(0,"ducati")
print(motorcycles)
#11
motorcycles_popped=motorcycles.pop()
print(type(motorcycles_popped))
#12
motorcycles.remove("yamaha")
print(motorcycles)
#13
motorcycles=[]
motorcycles.append("yamaha")
motorcycles.append("ducati")
motorcycles.append("suzuki")
motorcycles.append("ducati")
motorcycles.append("ducati")
## motorcycles.remove("ducati")*3  --> No funciona. No hay manera de hacerlo que no sea con un for ??
motorcycles.remove("ducati"),motorcycles.remove("ducati"),motorcycles.remove("ducati")
print(motorcycles)
#14
motorcycles=["yamaha", "suzuki", "honda", "ducati"]
motorcycles.sort()
print(motorcycles)
#15
motorcycles=["yamaha", "suzuki", "honda", "ducati"]
moto_sorted=motorcycles.copy()
moto_sorted.sort()
print(motorcycles,moto_sorted)
#16
print(len(motorcycles))
#17
print(motorcycles)
moto_reves=motorcycles.copy()
moto_reves.reverse()
print(moto_reves)
#18
## print(motorcycles[4]) -->Esto muestra un error porque no hay elemento en esa posición
#19
print(moto_reves[-1])
#20
print(moto_reves[1:3])
#21
print(moto_reves[1:])
#22
my_foods=["pizza", "cakes", "meat"]
family_foods=my_foods.copy()
print("My favourite foods are " ,my_foods) 
print("My family's are " ,family_foods) 
#23
my_foods.append("ice cream")
print(my_foods)
print(family_foods)




