def fibonacci(n):
  
    serie = []
    
   
    a, b = 0, 1
    
    for _ in range(n):
        serie.append(a)  
        a, b = b, a + b 
    
    return serie


num_terminos = int(input("¿Cuántos términos de la serie de Fibonacci deseas generar? "))


resultado = fibonacci(num_terminos)
print("Serie de Fibonacci:", resultado)
