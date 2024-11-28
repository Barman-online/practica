def guardar_nombres():
    nombres = []
     
    while True:
        nombre = input("introduce un nombre o pulsa n para terminar:")

        if nombre.lower() == "n":
            break

        nombres.append(nombre)

        nombres.sort(key=len)

        print("nombres ordenados por tamaño:")

        for index, value in enumerate (nombres, 1):
            print(f"{index} -> {value}")


guardar_nombres()



