
#Somatorio
y <- c(65,75,85,65,95,80)
#primeiro tipo
sum(y^2)-y[1]^2-y[5]^2
#segundo tipo
sum(y[-c(1,5)]^2)

#Produtorio
z<- c(1,2,3,4)
prod(z)
prod(z[-c(3,4)])

#medidas de posição amostral

#media
w<-1:5
w[2]<-NA
mean(w)
mean(w,na.rm = T)

#mediana
a<-c(1,2,3,4,5,6,7,8,9,10)
median(a)

#moda
b <- c(2,3,3,6,6,5,5,2,2,2,3,3,6,6,4,4,4)
table(b) #cria uma tabela de frequencia
#install.packages("modeest")
library(modeest)
mfv(b)
#terceiro tipo
subset(table(b),table(b)==max(table(b)))


