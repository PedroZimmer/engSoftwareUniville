






hist(x,         #histograma de x
     right = T,  #intervalos fechados a direita
     include.lowest = F, #não soma extremos do vetor
     breaks = 1:6 #intervalos de classes
)

x= c(2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,6)
hist(x)
table(x)

hist(x,
     right = T,include.lowest = F,breaks = 1:6)



x= c(27,22,20,21,25,26,38,31,35,3,23,14,24,34,44,51,15,6)
hist(x)
table(x)
hist(x,
     nc=6,
     right=F,
     main="Histograma",
     xlab="tempo em minutos",
     ylab="frequencia",
     col="green",
     density= 25
)

