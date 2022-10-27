'''
1)	Faça uma função que receba as três notas de um aluno como parâmetro e uma letra.
Se a letra for A o procedimento calcula a média aritmética das notas do aluno, 
se for P o procedimento calcula a média ponderada com os pesos 5,3 e 2.
A média calculada deve ser devolvida ao programa principal para, então, ser mostrada.

'''

def funcao(notas, letra):
    if letra == "a" : #MEDIA ARITIMETICA
        return media_aritimetica(notas)
    if letra == "p": #MEDIA PONDERADA
        return media_ponderada(notas)

def media_aritimetica(notas):
    a,b,c = colocar_nas_variaveis(notas)
    return (a+b+c)/3

def media_ponderada(notas):
    a,b,c = colocar_nas_variaveis(notas)
    resultado = (a*5+b*3+c*2)/10
    return resultado

def ler_notas():
    notas = []
    for i in range(3):
        print("Insira a nota", i+1)
        notas.append(int(input()))
    return notas

def colocar_nas_variaveis(notas):
    a,b,c = notas
    return a,b,c      

notas = ler_notas()
letra = str(input("Insira o tipo de média"))

resposta = funcao(notas, letra)
print("Resposta:", resposta)