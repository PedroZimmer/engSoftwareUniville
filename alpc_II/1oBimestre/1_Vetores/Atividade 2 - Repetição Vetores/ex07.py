poltronajanela = [1]*24 #[0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0]
poltronacorredor = [0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0]
corredordisp = []
janeladisp = []
cont1 = 0
cont2 = 0
for i in range(24):
    if poltronajanela[i] == 1:
        cont1 += 1
    if poltronacorredor[i] == 1:
        cont2 += 1
print("Bem-Vindo")
if cont1 + cont2 >= 48:
    print("Todos as poltronas ocupadas!!!")
else:
    onde = int(input("Qual a preferência de poltrona? 1- Corredor | 2- Janela\n"))
    corredorwhile = True
    while corredorwhile:   
        if onde == 1:
            contocupados1 = [0]
            for i in range(1,25):
                if poltronacorredor[i-1] == 0:
                    corredordisp.append(i)
                else:
                    contocupados1[0] += 1
            if contocupados1[0] < 24:
                print("Esses são as poltronas no corredor disponiveis:\n", corredordisp)
                corredorwhile = False
            else:
                print("Todas as poltronas no corredor estão ocupadas!\nVerificar janelas?")
                verificar = int(input("1- Sim | 2 - Não"))
                if verificar == 1:
                    onde = 2
                else:
                    print("Até uma próxima!!!")
                    break
        else:
            if onde == 2:
                contocupados2 = [0]
                for i in range(1,25):
                    if poltronajanela[i-1] == 0:
                        janeladisp.append(i)
                    else:
                        contocupados2[0] += 1
                if contocupados2[0] < 24:
                    print("Esses são as poltronas na janela disponiveis:\n", janeladisp)    
                    corredorwhile = False
                    print("Até uma próxima!!!")
                else:
                    print("Todas as poltronas na janela estão ocupadas!\nVerificar corredor?")
                    verificar = int(input("1- Sim | 2 - Não"))
                    if verificar == 1:
                        onde = 1
                        corredorwhile = True
                    else:
                        corredorwhile = False
                        print("Até uma próxima!!!")
                        break                      