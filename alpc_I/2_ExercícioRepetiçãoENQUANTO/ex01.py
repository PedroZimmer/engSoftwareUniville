# Faça um algoritmo que calcule a multiplicação de dois números inteiros sem utilizar o operador “*”. Em vez disso, utilize apenas o operador de adição “+”. 
# Para implementar esse algoritmo, devemos lembrar que qualquer multiplicação pode ser expressa por meio de somas. 
# Por exemplo, o resultado da expressão 6 * 3 é o mesmo que 6 + 6 + 6 ou 3 + 3 + 3 + 3 + 3 + 3. Ou seja, soma-se um elemento com ele próprio o número de vezes do segundo elemento.
print("Digite o primeiro numero")
num = int(input())
print("Digite o segundo numero")
num2 = int(input())
res = 0
contador = 0
for i in range(num):
    res += num2
print("Resultado:", res)
res = 0
while contador < num2:
    print(num, end="+")
    res += num
    contador += 1
print("\n Resultado:", res)