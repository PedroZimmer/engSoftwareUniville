#1)
#a)
media <- scan()
mean(media)
#b)
moda <- media
table(moda)
#c)
mediana <- media
median(mediana)
#d)
variancia <- media
var(variancia)
#e)
desvioPadrao <- media
sd(desvioPadrao)

#2)
#moda
x <- c(rep(3,5), rep(5,7), rep(7,10), rep(9,3), rep(11,5))
table(x)
#mediana
median(x)
#media
mean(x)

#3)
#coeficiente de variação
y <-(1.47/18.3)*100 #desvio padrao dividido pela media vezes 100
y

#4)
#Na de matematica pois o desvio padrao é maior

#5
#grupo 1
g1 <- (5.97/160.6)*100
g1
#grupo 2
g2 <- (6.01/161.9)*100
g2
#grupo 2 é mais homogeneo

#6)
z <- ((163.8*3.3)/100) #media vezes desvio padrao dividido por 100
z
