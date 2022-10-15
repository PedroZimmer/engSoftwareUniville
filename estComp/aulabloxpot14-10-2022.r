
#Exemplo1
InsectSprays
boxplot(count~spray,
        data=InsectSprays,
        main="Boxplot",
        xlab="Insecticida",
        ylab="Insetos Sobreviventes",
        col=3
)

#grafico em setores

a<-c(1,2,3,4,5,6,7,8,9,10)
names(a) <- c('a','b','c','d','e','f')
pie(a, col=c("red","blue","green","yellow","pink","purple"),
    main="Grafico em setores")




x <- c(0:20)
y = x^2
plot(x,y,pch="M") #plotando x e y 
points(rev(x),y, pch="P") #adicionando pontos
lines(x,400-y)
title("Titulo")


x <- c(0:20)
y = x^2
plot(x,y)
abline(0,10) #reta passando pelo 0 e inclinação 20
abline(h=200, col=4) #reta horinzontal em y=200 azul
abline(v=15, col=2) #reta vertical em x=15 vermelha

#mudando linhas
x <- c(0:20)
y = x^2
plot(x,y, type = 'n')
lines(x,y,lwd=4)
lines(rev(x),y,lty=2)


#definindo manualmente o intervalo dos eixos
plot(x,y,
    ylim= c(0,600)
    )


#adicionando text
plot(x,y,xlab="eixo x", ylab="eixo y")
title("Titulo \n (quebra de linha)")
text(6,200,"Texti qualquer")



#interagindo com a janela grafica+
x<-c(2,3,4,5,6,7)
y<-c(15,46,56,15,81,11)
nomes<-LETTERS[1:6]
cidades<-data.frame(x,y,row.names = nomes)
cidades

plot(cidades, main="Coordenadas das cidades")

#podemos identificar os nomes das cidades
identify(x,y,nomes,n=3)



