
listas = []

while True:
    lista = input("ingrese el producto:")


    if lista == "n":
        break

    else:
        listas.append(lista)


for index, value in enumerate (listas, 1):
    print(f"{index} -> {value}")


