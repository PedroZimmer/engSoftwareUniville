diassemana = ["Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sábado"]
diasem = 0
maior = 0
totalkm = 0
cont = 0
contpsg = 0
for dia in range(1,7):
    print(diassemana[diasem])
    diasem2 = (diassemana[diasem])
    diasem += 1
    numtrans = int(input("Insira o número de passageiros transportados...\n"))
    km = int(input("Km's rodados no dia...\n"))
    totalkm += km
    contpsg += numtrans
    if numtrans > 50:
        cont += 1
    if dia == 1:
        menor = numtrans
        omenor = diasem2
    if numtrans < menor:
        menor = numtrans
        omenor = diasem2
    if numtrans > maior:
        maior = numtrans
        omaior = diasem2
    media = totalkm / 6
    faturamento = contpsg * 14
    consumo = (totalkm/11) * 6.9
    if faturamento > consumo:
        lucro = faturamento - consumo        
    else:
        preju = consumo - faturamento        
print("O dia com menos passageiros é:", omenor)
print("O dia com mais passageiros é:", omaior)
print("Média de Km's rodados:", round(media,0))
print("A van transportou mais de 50 passageiros no dia em", cont,"dia(s)")
if lucro > 0:
    print("A empresa teve $", round(lucro,2),"de lucro..")
else:
    print("A empresa teve $", round(preju,2),"de prejuizo.")