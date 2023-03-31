myArray = (1,2,2,5,4,6,7,8,8,8)

n = len(myArray)
number = myArray[0]
cont= 0
longitud = 0


for i in range(n):
    cont = 0
    for j in range(n):
        if myArray[i] == myArray[j]:
            cont+=1
            if cont > longitud:
                number = myArray[i]
                longitud = cont

print('numero')
print(number)
print('longitud')
print(longitud)