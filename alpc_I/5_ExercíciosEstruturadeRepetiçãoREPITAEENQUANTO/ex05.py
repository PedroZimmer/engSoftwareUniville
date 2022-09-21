
cidades = 2
maior = 0
menor = 0
omenor = 0
omaior = 0
totalcarros = 0
somaacidentes = 0
soma2 = 0
for city in range(1,cidades+1):
    print("Cidade", city)
    code = int(input("Insira o código da cidade...\n"))
    carros = int(input("Insira a quantidade de carros...\n"))
    acidentes = int(input("Insira o número de acidentes...\n"))
    if city == 1:
        menor = acidentes
        omenor = city
    if acidentes < menor:
        menor = acidentes
        omenor = city
    if acidentes > maior:
        maior = acidentes
        omaior = city
    if carros < 2000:
        somaacidentes += acidentes
        soma2 += 1
totalcarros += carros
media = totalcarros / cidades
media2 = somaacidentes / soma2
print("Cidade com mais acidentes:", omaior,"com ", maior,"acidentes")
print("Cidade com menor acidentes:", omenor,"com ", menor,"acidentes")
print("Média de carros é de:", media)
print("Média de acidentes com menos de 2000 carros:", media2)
