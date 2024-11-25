edad = int(input("ingresa tu edad:"))
cedula = str(input("tienes tu cedula:"))
pasaporte = str(input("tiene pasaporte:"))
trabajo = str(input("tiene usted trabajo:"))
sueldo = int(input("ingre su sueldo:"))

if edad > 18:
    print("usted tiene visa")
elif cedula == "si" and pasaporte == "si" and trabajo == "si":
    print("usted tiene visa")
elif sueldo > 5000000:
    print("usted tiene visa")
else:
    print("usted no tiene visa")
