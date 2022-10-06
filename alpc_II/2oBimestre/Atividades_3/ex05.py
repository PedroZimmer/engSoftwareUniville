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
