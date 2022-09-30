'''
1)	Faça uma função que receba as três notas de um aluno como parâmetro e uma letra.
Se a letra for A o procedimento calcula a média aritmética das notas do aluno, 
se for P o procedimento calcula a média ponderada com os pesos 5,3 e 2.
A média calculada deve ser devolvida ao programa principal para, então, ser mostrada.

'''

def funcao(a:int,b:int,c:int,letra:str):
    #MEDIA ARITIMETICA
    if letra == "a" or letra == "A":
        resposta = (a+b+c)/3
    #MEDIA PONDERADA
    if letra == "p" or letra == "P":
        resposta = (a*5,b*3,c*2)/10
    return(resposta)
notas = []
for i in range(3):
    print("Insira a nota", i+1)
    notas.append(int(input()))
letra = str(input("Insira o tipo de média"))
resposta = funcao(notas[0],notas[1],notas[2],letra)
print("Resposta:", resposta)