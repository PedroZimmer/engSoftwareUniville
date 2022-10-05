#1) Qual é a diferença entre população e amostra?
a <- "População é o conjunto de todos os elementos de uma determinada pesquisa.
Amostra é uma parte da população, que são objetos selecionados para serem estudados."

#2) Para cada uma das variáveis a seguir, determine se a variável é categórica ou numérica. Se a variável for numérica, determine se é discreta ou contínua:
# a.	Valor gasto com vestuário por mês
# b.	Loja de departamento preferida
# c.	Período mais provável em que ocorre a compra de peças de vestuário (dia útil durante o dia, dia útil durante a noite ou final de semana)
# d.	Número de sapatos que a pessoa possui.

"a.	Numérica contínua
 b.	Categórica
 c.	Categórica
 d.	Numérica discreta"

#3) Faça os arredondamentos requeridos usando as funções adequadas, transcreva a sequência os comandos utilizados até chegar ao resultado.
# 8,7578 para 3 algarismos significativos
# 434,4348 para 2 casas decimais
# 56,894 para o maior valor
# 89,335 para o menor valor

c <- round(8.7578, 3)
c2 <- round(434.4348, 2)
c3 <- ceiling(56.894)
c4<- floor(89.335)
c
c2
c3
c4

#4) Siga a sequência abaixo: 
# a) Crie o vetor “A” com a sequência de números de 0 a 100 com incremento 5. 
# b) Utilize os dados do vetor “A” para criar uma matriz 3x7, disposta através das colunas. 
# c) Localize o 3° elemento da 2ª coluna da matriz. 
# d) Usando o comando summary( ), encontre as medidas descritivas da matriz. 
# e) Acrescente uma linha à matriz M contendo elementos sequenciais de 1 a 7, chame a nova matriz de N.

a <- seq(0, 100, 5)
b <- matrix(a, nrow = 3, ncol = 7, byrow = 0)
c <- b[2, 3]
d <- summary(b)
e <- rbind(b, c(1:7))
a
b
c
d
e


#5) Considere as informações contidas abaixo acerca das alturas de 20 alunos. Faça uma distribuição de frequências e o gráfico histograma correspondente, com intervalo fechado a esquerda (escolha a formatação do seu histograma).
# 1.52, 1.56, 1.61, 1.67, 1.68, 1.71, 1.72, 1.72, 1.75, 1.75, 1.76, 1.78, 1.79, 1.80, 1.81, 1.87, 1.88, 1.90, 1.91, 2.01

a <- c(1.52, 1.56, 1.61, 1.67, 1.68, 1.71, 1.72, 1.72, 1.75, 1.75, 1.76, 1.78, 1.79, 1.80, 1.81, 1.87, 1.88, 1.90, 1.91, 2.01)
hist(a)
table(a)
hist(a, breaks = 5, col = "blue", main = "Histograma", xlab = "Altura", ylab = "Frequência")



#6 Prevenir a propagação de trinca de fadiga em estruturas de aviões é um importante elemento de segurança em aeronaves. Um estudo de engenharia para investigar a trinca de fadiga em n = 9 asas carregadas ciclicamente reportou os seguintes comprimentos (em mm) de trinca:
#2,13	2,96	3,02	1,82	1,15	1,37	2,04	2,47	2,60
#Crie um vetor com os valores e calcule a média e o desvio-padrão da amostra.

a <- c(2.13, 2.96, 3.02, 1.82, 1.15, 1.37, 2.04, 2.47, 2.60)
mean(a)
sd(a)
