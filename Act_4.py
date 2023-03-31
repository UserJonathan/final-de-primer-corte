genero = {'f': 8284,
            'm': 9321}

departamento = {'huila': 251.921625,
                'casanare': 252.430580,
                'meta': 253.170546,
                'nariño': 254.874578,
                'quindio': 254.983682,
                'risaralda': 255.983682,
                'cundinamarca': 257.643275,
                'boyaca': 262.909390,
                'santander': 265.857387,
                'bogota': 267.886987,
}

for clave, valor in genero.items():
    print(f'{clave}: {valor}')
print()
print('Departamento:')
print()

for clave, valor in sorted(departamento.items()):
    print(f'{clave}: {valor}')







# for i in sorted(departamento):
