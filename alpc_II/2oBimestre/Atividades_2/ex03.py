'''
3.	A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e número de filhos.
Faça uma função que leia esses dados para um número não determinado de pessoas e retorne a média de salário da população,
a média do número de filhos, o maior salário e o percentual de pessoas com salário até R$ 350,00.
'''


def main():
    salario = []
    filhos = []
    menu = True
    while menu:
        print('1 - Cadastrar')
        print('Digite o salario: ')
        salario.append(int(input()))
        filhos.append(int(input('Digite o número de filhos: ')))
        menu = input('Deseja continuar? [S/N] ').upper()
        if menu == 'S':
            menu = True
        else:
            menu = False
    print('Média de salário: ', sum(salario) / len(salario))
    print('Média de filhos: ', sum(filhos) / len(filhos))
    print('Maior salário: ', max(salario))
    print('Percentual de pessoas com salário até R$ 350,00: ', (salario.count(350) / len(salario)) * 100)
    return 0
main()