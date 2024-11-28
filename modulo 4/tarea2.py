def contar_palabras_y_consonantes(palabra):
    letras = len(palabra)
    consonates = sum(1 for letra in palabra if letra.lower() in "bcdfghjklmnpqrstvwxyz")
    return letras, consonates 

def main():
    palabras = []
    while True:
        palabra = input("introduce una palabra o escribe salir para finalizar:")
        if palabra.lower() == "salir":
            break
        palabras.append(palabra)

    
    for palabra in palabras:
        letras,consonantes = contar_palabras_y_consonantes(palabra)
        print(f"la palabra {palabra} tiene {letras} letras y {consonantes} consonantes")


if __name__== "__main__":
    main()