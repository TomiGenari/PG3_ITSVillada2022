numeros = [21, 3, 67, 45]
print(numeros)
print("ingrese el numero que desea saber su posicion")


def search():  
    numeroIngresado=int(input())
    index = numeros.index(numeroIngresado)
    print(index)

search()