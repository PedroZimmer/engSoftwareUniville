matriz = [[0]*2 for i in range(2)]
print(matriz)
print(len(matriz[0]))


matriz = [[] for i in range(2)]
matriz[0].append(1)
print(matriz)

matriz.append([])
print(matriz)
