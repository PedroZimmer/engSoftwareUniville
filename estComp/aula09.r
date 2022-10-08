
#EXEMPLO 1
barplot (c(1,2,3,4,5,6,7,8,9,10), main = "Gráfico de Barras", 
xlab = "Eixo X", 
ylab = "Eixo Y",
bty = "l", 
col = "blue", 
border = "red",)

#EXEMPLO 2
barplot (table(c(1,2,3,4,5,6,7,8,9,10)), main = "Gráfico de Barras",
xlab = 'cores',
ylab = 'frequencia',
bty = 'l',
col = c('red','green','blue','yellow','black','purple','orange','pink','brown','gray'),
horiz = TRUE)

#EXEMPLO 2 com letras

barplot (table(c('a','a','a','a','a','b','b','b','c','c','v','v')),
         main = "Gráfico de Barras",
          xlab = 'cores',
ylab = 'frequencia',
bty = 'l',
col = c('red','green','blue','yellow','black','purple','orange','pink','brown','gray'),
horiz = TRUE)

#EXEMPLO 3

prof <- c(1751,1186,947,29)
escola <- c('privada','estadual','municipal','federal')
barplot (prof, names.arg = escola,
main = "Quantidade de professor",
xlab = "instiuição",
ylim = c(0,2000),
col = 'blue')

#EXEMPLO 4
prof <- c(1751,1186,947,29)
names(prof) <- c('privada','estadual','municipal','federal')
prof
barplot (prof, names.arg = escola,
main = "Quantidade de professor",
cex.names = 1.2,
cex.axis = 0.5,
xlab = "instiuição",
ylim = c(0,2000),
col = 'blue',
density = 80)

#EXEMPLO 5
prof <- c(1751,1186,947,29)
names(prof) <- c('privada','estadual','municipal','federal')
prof
barplot (prof,
main = "Quantidade de professor",
cex.names = 1.2,
cex.axis = 1.2,
ylab = "Instituição",
ylim = c(0,2000),
col = c('blue','green','yellow','red')
)

#EXEMPLO 6 duas variaveis em um grafico
alunosprof <- matrix(c(1751,1186,947,29,25280,21328,18432,280), nrow = 4, ncol = 2)
alunosprof

dimnames (alunosprof) <- list(c('privada','estadual','municipal','federal'),c('professores','alunos'))

barplot (alunosprof,
beside = TRUE,
main = "distribuição de matricula de alunos e professores",
ylab = 'numero de matriculas',
xlab = 'matriculas',
legend.text = rownames(alunosprof))