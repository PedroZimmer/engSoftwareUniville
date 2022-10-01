# Um dado foi lançado 50 vezes e foram registrados os seguintes resultados:
# 5 4 6 1 2 5 3 1 3 3
# 4 4 1 5 5 6 1 2 5 1
# 3 4 5 1 1 6 6 2 1 1
# 4 4 4 3 4 3 2 2 2 3
# 6 6 3 2 4 2 6 6 2 1
# Construa o histograma dos resultados, com intervalo fechado à esquerda. Escolha um título para o
# gráfico e para os eixos x e y e a cor das barras faça de verde.

# Dados
x <- c(5, 4, 6, 1, 2, 5, 3, 1, 3, 3, 4, 4, 1, 5, 5, 6, 1, 2, 5, 1, 3, 4, 5, 1, 1, 6, 6, 2, 1, 1, 4, 4, 4, 3, 4, 3, 2, 2, 2, 3, 6, 6, 3, 2, 4, 2, 6, 6, 2, 1)

# Histograma
hist(x, breaks = 6, col = "green", main = "Histograma", xlab = "Valores", ylab = "Frequência")