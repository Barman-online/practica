
def convertir(f):
    c = (f-32) * 5/9
    return c 


f = float(input("ingrese los grados fahrenheit:"))
print(f"la cenvercion de grados celsius es:{convertir(f)}")
