def fibonancci(limite):
    a = 1
    b = 0
    for i in range (0, limite ):
        b = b+a
        a = b-a
        print(a, end=", ")


         
if __name__ == "__main__":
    fibonancci(10)