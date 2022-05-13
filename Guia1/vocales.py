print("ingrese una frase")
frase=input()

def vocales():
    vocales=0
    for i in range(len(frase)):
        if(frase[i]=="a" or frase[i]=="e" or frase[i]=="i" or frase[i]=="o" or frase[i]=="u"):
            vocales+=1
    print("la frase tiene " + str(vocales) + " vocales")

vocales()