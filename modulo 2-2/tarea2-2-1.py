sueldo_anual = int(input("ingrese su sueldo anual:"))

if sueldo_anual > 10_000_000:
    print("usted es millonario")
elif sueldo_anual > 3_000_000:
    print("usted es clase alta")
elif sueldo_anual > 1_000_000:
    print("clase baja")
else:
    print("usted es pobre")
    