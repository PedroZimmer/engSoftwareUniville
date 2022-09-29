



#COMO CRIAR UM GRÁFICO
x<-1:20
y = x^2
plot(x,y,type = "b", pch=19)


#PADRÃO DOS PONTOS
plot(0:20, #coord. eixo das abscissas
     rep(0,21), #coord. eixo das ordenadas
     pch=0:20, #estilo dos pontos
     cex = 2, # tamanho dos pontos
     main = "Padrão\ndos pontos", #titulo (NOTE O \N)
     xlab = "pch=", #tecto dos eixos das abscissas
     ylab="") #sem texto nas ordenadas
     

#CARACTER COMO PADRAO DE PONTO
plot(x,y,pch="M")


#VARIOS GRAFICOS NA MESMA JANELA
par(mfrow=c(2,2)) #arranjo "2 por 2"
plot(x,y)
plot(rev(x),y)
plot(x,2*y)
plot(x,log(y))


#VARIAS CURVAS EM UM GRAFICO
x <-seq(0,10,0.1)
x1<-0.4*exp(-0.4*x)
x2<-0.3*exp(-0.3*x)
y<-cbind(x1,x2)
matplot(y,type="l")
legend(80,0.3,c("x1","x2"), lty= c(1,2), col=c(1,2))


#PERSONALIZANDO GRAFICOS
x<-1:10
y<-c(2,5,9,6,7,8,4,1,3,10)
x;y

#1o gráfico
plot(x,y)


#2o gráfico
plot(x,y,                     #plota x e y
     xlab = "Eixo x",         #nomeia o eixo x
     ylab = "Eixo y",         #nomeia o eixo y
     main="Personalizando um gráfico", # titulo
     xlim = c(0,10), #limites do eixo x
     ylim = c(0,10), #limites do eixo y
     col = "red",    #cor dos pontos
     pch = 22,       #formato dos pontos
     bg = "blue",    #cor do preenchimento
     tcl = 0.4,      #tamanho dos traços dos eixos
     las = 1,        #orientaçãp dps valores nos eixos
     cex = 1.5,      #tamanho do ponto
     bty='l')        #altera as bordas