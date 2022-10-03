'''
2.	Faça uma função que receba, por parâmetro, a altura e o sexo de uma pessoa e retorne o seu peso ideal.
Para homens calcular o peso ideal usando a fórmula a seguir: 
pesoideal = 72.7 * alt – 58 e para mulheres: pesoideal = 62.1 * alt – 44.7
'''

altura = float(input('Digite a altura: '))
sexo = input('Digite o sexo: ')
def funcao(altura, sexo):
    if sexo == 'm':
        pesoideal = 72.7 * altura - 58
    else:
        pesoideal = 62.1 * altura - 44.7
    return pesoideal
print(funcao(altura, sexo))

