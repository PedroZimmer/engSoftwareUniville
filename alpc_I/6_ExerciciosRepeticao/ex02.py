maior = 0
totalprop = 0
totalmusic = 0
hrsmes = 744
for semana in range(1,5):
    print("Semana", semana)
    musica = int(input("Tempo de música...\n"))
    propaganda = int(input("Tempo de propaganda...\n"))
    if propaganda > maior:
        maior = propaganda
        omaior = semana
    if semana == 1:
        menor = musica
        omenor = semana
    if semana < menor:
        menor = semana
        omenor = semana
    totalprop += propaganda
    totalmusic += musica
    perc = (totalprop / hrsmes) * 100
print("Semana com mais propaganda:", omaior)
print("Semana com menos música:", omenor)
print("Total de musica:", totalmusic)
print("Total de propaganda:", totalprop)
print("Porcentagem de propaganda:", round(perc,1),"%")