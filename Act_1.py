myArray = (1,3,4,2,7,0)

n = len(myArray)

for i in range(n):
    for j in range(n):
        if (myArray[i] + myArray[j]) == 10:
            print(f'{myArray[i]}  {myArray[j]}')

