# Um artigo do periódico Materials Engineering descreve os resultados de teste de tensão
# quanto à adesão em 22 corpos de prova de liga U-700. A carga no ponto de falha do corpo
# de prova é dada pelo arquivo “carga no ponto de falha.txt”. Verifique se os dados sugerem
# que a carga média na falha excede 10 MPa. Considere o nível de significância de 5%.
# Interprete o resultado.


cargaNoPontodeFalha <- c(read.table("C:\\#Dev\\engSoftwareUniville\\estComp\\atividadeAv2oBIM\\Aula14-Carga_no_ponto_de_falha.txt", header = TRUE))

t.test(cargaNoPontodeFalha,
        mu = 10,
        alternative = "greater",
        conf.level = 0.95)







# Dois catalisadores estão sendo analisados para determinar como eles afetam o rendimento
# médio de um processo químico. Especificamente, o catalisador 1 está corretamente em
# uso, mas o catalisador 2 é aceitável. Uma vez que o catalisador 2 é mais barato, ele deve
# ser adotado, desde que ele não mude o rendimento do processo. Um teste é feito em uma
# planta piloto, resultando nos dados do arquivo “catalisadores”. Há alguma diferença entre
# os rendimentos médios? Use α = 0,05 e considere variâncias iguais. Formule antes as
# hipóteses.




catalisador <- read.table("C:\\Users\\pedro\\Downloads\\catalisador.txt", header = TRUE)


t.test(catalisador[1],
        catalisador[2],
        conf.level = 0.95)



# Uma companhia fabrica propulsores para uso em motores de turbinas de avião. Uma das
# operações envolve esmerilhar o acabamento de uma superfície particular para um
# componente de liga de titânio. Dois processos diferentes para esmerilhar podem ser
# usados, podendo produzir peças com iguais rugosidades médias na superfície. Uma
# amostra aleatória de n1 = 11 peças, proveniente do primeiro processo, resulta em um
# desvio-padrão de s1 = 5,1 micropolegadas. Uma amostra aleatória de n2 = 16 peças,
# proveniente do segundo processo, resulta em um desvio-padrão de s2 = 4,7
# micropolegadas. Verifique se a razão entre as duas variâncias é diferente de 1 com um
# nível de confiança de 90%. Considere que os dois processos sejam diferentes e a
# rugosidade na superfície seja normalmente distribuída


amostra1 = rnorm(11, 0, 5.1)
amostra2 = rnorm(16, 0, 4.7)
desvioPadrao1 = 5.1
desvioPadrao2 = 4.7
confianca = 0.9

var.test(amostra1, amostra2, conf.level = confianca)

qqnorm(amostra1)
qqline(amostra1)
qqnorm(amostra2)
qqline(amostra2)




#4
cargaNoPontodeFalha <- c(19.8,15.4,11.4,19.5,
10.1,
18.5,
14.1,
8.8,
14.9,
7.9,
17.6,
13.6,
7.5,
12.7,
16.7,
11.9,
15.4,
11.9,
15.8,
11.4,
15.4,
11.4)

shapiro.test(cargaNoPontodeFalha)




catalisador <- c()

shapiro.test(catalisador)

