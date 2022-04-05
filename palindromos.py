
print("ingrese una palabra")
palabra=input()

def palindromo():
    if(palabra==palabra[::-1]):
        print("es palindromo")
    else:print("no es palindromo")

palindromo()   
