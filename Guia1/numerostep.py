
print("ingrese un numero")
num=int(input())

def isStep():
     if num/float(2)!=num/2:
        return False
     for i in range(0,len(num),2):
        if not (int(num[i:i+2][0])+1==int(num[i:i+2][1]) or int(num[i:i+2][0])-1==int(num[i:i+2][1])):
            return False

     return True
 
isStep()

   
