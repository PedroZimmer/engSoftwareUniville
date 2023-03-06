
lados = ['a','b','c']
dados = []
for i in lados:
    print('Digite o valor do lado',i)
    dados.append(int(input()))

for i in range(0,3):
    if i+1 == len(dados):
        break
    else:
        if dados[i] > dados[i+1]:
            dados[i], dados[i+1] = dados[i+1], dados[i]
        else:
            pass
print(dados)

if dados[0] + dados[1] > dados[2]:
    print('É um triangulo')
    
