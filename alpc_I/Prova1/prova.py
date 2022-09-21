omaior = 0
linhamaior = 0
totalturno1 = 0
totalturno2 = 0
for lin in range(1, 4):
    print("Linha", lin)
    totalprod = 0
    for turno in range(1, 3):
        print("\tTurno", turno)
        print("\t\tDigite o código do produto...")
        code = int(input())
        print("\t\tDigite a quantidade produzida...")
        qtdproduzida = int(input())
        print("\t\tDigite a quantidade refugada...")
        qtdrefugada = int(input())
        if turno == 1:
          totalturno1 = qtdrefugada
        else:
          totalturno2 = qtdrefugada
        totalprod += qtdproduzida
        if code == 2:
            if qtdrefugada <= 100:
                print("\t<Produção Normal>")
            else:
                print("\t<Produção Irregular>")
        else:
            if qtdrefugada >= 50:
                print("\t<Produção Normal")
            else:
                print("\t<Produção Irregular>")
    if totalprod > omaior:
        omaior = totalprod
        linhamaior = lin
print("A linha de maior producão é a:", linhamaior, ", produziu:", omaior,
      "produtos.")
print("O total descartado no turno 1 é de...", totalturno1)
print("O total descartado no turno 2 é de...", totalturno2)