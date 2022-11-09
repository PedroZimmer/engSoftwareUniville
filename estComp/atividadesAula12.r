# 1. Apresente os espaços amostrais dos seguintes experimentos aleatórios:
# a) Lançamento de uma moeda honesta e observação da face voltada para cima.
a <- c("cara", "coroa")
# b) Contagem do número de clientes numa fila única do banco, que chegaram durante uma hora.
b <- 0:10
# c) Medição da velocidade do vento, em km/h, na pista de um aeroporto.
c <- seq(0, 100, 1)
# d) Medição da temperatura, em graus Celsius, numa estação meteorológica da cidade de Joinville.
d <- seq(-10, 40, 1)



# 2. Considere que você vai cronometrar o tempo, em segundos, para carregar uma página na web. Represente, em forma de conjuntos, os seguintes eventos:
#   a) A = mais do que 5 e, no máximo, 10 segundos
a <- seq(5, 10, 1)
#   b) B = Mais do que 10 segundos
b <- seq(10, 100, 1)
#   c) C = Mais do que 8 segundos
c <- seq(8, 100, 1)
#   d) D = A U B
d <- c(a, b)
#   e) E = A intersecção B
e <- intersect(a, b)
#   f) F = A intersecção C
f <- intersect(a, c)
#   g) G = A’
g <- setdiff(1:100, a)



#3. No lançamento de um dado, qual a probabilidade de se obter um número não-inferior a 5?
x <- c(5,6)
dado <- dpois(x, 6)
dado*100


# 4. Retira-se, ao acaso, uma carta de um baralho de 52 cartas. Calcule a probabilidade de:
# a) A carta não ser de ouros;
a
# b) Ser um rei;
# c) Ser uma carta de ouros ou uma figura.