maior = 0
menor = 0 
omaior = 0
omenor = 0
for aluno in range(1,4):
    print("Aluno", aluno)
    num = int(input("Insira o número do aluno...\n"))
    altura = int(input("Insira a altura...\n"))
    if aluno == 1:
        menor = altura
        omenor = num
    if altura < menor:
        menor = altura 
        omenor = num
    if altura > maior:
        maior = altura
        omaior = num
print("\nO maior aluno:\n Número:", omaior,"\nTem", maior, "cm de altura.")
print("O menor aluno:\n Número:", omenor,"\nTem", menor, "cm de altura.")