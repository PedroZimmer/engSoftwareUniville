

#Um algoritmo que lê um número e imprime a lista dos seus divisores.

numero = int(input("Digite um número: "))
divisores = []

for i in range(1, numero+1):
    if numero % i == 0:
        divisores.append(i)
        
print(divisores)



#Um algoritmo que lê as 4 notas de um aluno e diga se ele passou por média, está em final ou reprovou. 

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print("Aprovado")
elif media >= 4:
    print("Final")
else:
    print("Reprovado")