#A
listax = [1,2,3,4,5,6,7,8,9,10]
listay = [6,7,8,9,10,11,12,13,14,15]
print("Lista X:", listax)
print("Lista Y:", listay)
lista1 = []
for i in range(10):
    lista1.append(listax[i])
cont = 0
for j in range(10):
    for i in range(10):
        if listay[cont] != lista1[i]:
            pass
        else:
            lista1.append(listay[i])           
    cont += 1
print("A. União ->", lista1)
#B
lista2 = []
for i in range(10):
    lista2.append(listax[i])
for j in range(10):
    for i in range(10):
        if len(lista2) > j:
            if lista2[j] == listay[i]:
                lista2.remove(lista2[j])
            else:
                pass
        else:
            break    
print("B. Diferença ->", lista2)
#C
lista3 = []
for i in range(10):
    lista3.append(listax[i] + listay[i])
print("C. Soma ->", lista3)
#D
lista4 = []
for i in range(10):
    lista4.append(listax[i] * listay[i])
print("D. Produto ->", lista4)
#E
lista5 = []
for j in range(10):
    for i in range(10):
        if len(lista5) < j:
            if listax[j] == listay[i]:
                lista5.append(listax[j])
            else:
                pass
        else:
            break    
print("E. Intersecção ->", lista5)