# REPPARA1) Calcule e apresente a PROGRESSÃO GEOMÉTRICA dos 200 próximos números de 1 considerando o quociente 4.
x = 1
for i in range(1, 201):
    print(x)
    x = 1 * 4**(i-1)
