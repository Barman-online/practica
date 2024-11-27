def contar_palabras(text:str, charsplit= " ") -> int:
    return len(text.split(charsplit)) 

texto = "hola soy cesar programador en python"

print(contar_palabras(text=texto, charsplit="a"))