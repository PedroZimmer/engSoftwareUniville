perc = 1.5
salario = 1000
for ano in range(1995,2023):
    print(ano)
    print(salario)
    salario = (salario * perc / 100) + salario
    perc *= 2
    