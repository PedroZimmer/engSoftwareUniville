'''
5.	Crie uma função que receba como parâmetro a hora de início e a hora de término de um jogo,
ambas subdivididas em dois valores distintos: horas e minutos.
A função deverá retornar a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas...
e que ele pode começar em um dia e terminar no outro.
'''

def funcao(hr_ini, min_ini, hr_fim, min_fim):

    if hr_fim < hr_ini:
        diferença = (24 - hr_ini) + hr_fim
    else:
        diferença = hr_fim - hr_ini
        
        
    if min_fim < min_ini:
        diferençamin = (60 - min_ini) + min_fim
        diferença -= 1
    else:
        diferençamin = min_fim - min_ini
        
    resultado = (diferença*60) + diferençamin
    if resultado >= 1440:
        resultado = "O jogo chegou em 24hrs... Insira os dados novamente!"
        return resultado
    else:
        return resultado


hr_ini = int(input("Digite a hora de inicio do jogo: "))
min_ini = int(input("Digite os minutos de inicio do jogo: "))
hr_fim = int(input("Digite a hora de fim do jogo: "))
min_fim = int(input("Digite os minutos de fim do jogo: "))


resposta = (funcao(hr_ini, min_ini, hr_fim, min_fim))
print("Serão necessários {} minutos para o jogo terminar!".format(resposta))

