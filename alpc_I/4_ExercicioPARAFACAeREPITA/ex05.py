maiorprop = 0
totalmusica = 0
totalprop = 0
totalhrs = 744
idmusic = 0
idprop = 0
for semana in range(1,5):
  print("Semana", semana)
  print("Insira o número de horas de músicas tocadas na semana...")
  horassem = int(input())
  print("Insira o número de horas de propagandas vinculadas...")
  propsem = int(input())
  if semana == 1:
    menormusic = horassem
  if horassem < menormusic:
    menormusic = horassem
    idmusic = semana 
  if propsem > maiorprop:
    maiorprop = propsem
    idprop = semana
  #total de horas de música 
  totalmusica += horassem
  #total de horas de propaganda
  totalprop += propsem
  percprop = (totalprop / totalhrs) * 100
print("A semana", idprop,"é a semana com o mais propaganda.")
print("A semana", idmusic,"é a semana com menos música.")
print("Total de música:", totalmusica)
print("Total propaganda:", totalprop)
print("Percentual de propagandas:", percprop,"%")

