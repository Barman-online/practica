contraseña = "cesarpython"

intentos = 0

while intentos <3:
    contraseña = input("ingrese su contraseña:")

    if contraseña.lower == contraseña:
        print ("contraseña correcta!!")
        break

    else:
        intentos += 1
        print (f"incorrecto. te quedan {3-intentos} intento(s)")

    
if intentos == 3:
    print("has alcanzado el numero de intentos, el programa se cerrara....")