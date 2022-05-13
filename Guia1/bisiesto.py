print("ingrese el año")
año = int(input())

def bisiesto():
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print("es bisiesto")
            else:
                print("no es bisiesto")
        else:
            print("es bisiesto")
    else:
        print("no es bisiesto")
bisiesto()