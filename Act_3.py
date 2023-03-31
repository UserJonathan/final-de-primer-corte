myArray =(1,2,1,3,3,1,2,1,5,1)

mapa_array = {}

for array in myArray:
    if array in mapa_array:
        mapa_array[array] += 1
    else:
        mapa_array[array] = 1
for valor in sorted(mapa_array):
    print(f'{valor}: {"*" * mapa_array[valor]}')

