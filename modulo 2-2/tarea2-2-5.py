usuario = str(input("ingrese su usuario:"))
contraseña = int(input("ingrese su contraseña:"))

if usuario == "cesar":
    print ("usuario correcto")
elif contraseña == 123456:
    print("contraseña correcta")
else:
    print("vuelva a intentarlo")