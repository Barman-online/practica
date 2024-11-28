def guardar_nombres():
    nombres = set()
    
    while True:
        nombre = input("introduce un nombre o pulsa (salir) para terminar:")

        if nombre.lower() =="salir":
            break

        elif nombre in nombres:
            print("ese nombre ya ha sido guardado ingrese otro.")

        else:
            nombres.add(nombre)

        print("nombres guardados:")

    for nombre in nombres:
        print (nombre) 


            
guardar_nombres()