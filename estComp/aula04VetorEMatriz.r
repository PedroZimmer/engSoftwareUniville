
#VETOR
x <- c(1,2,3,4,5)
y <- c(x,6,7,8,9)


x <- seq(1,10,1) #Começo | Fim | Passo

v <- seq(10,1,-1) #FIM | Começo | Passo(-)
a <- 1:10 #1 até 10

#REPETICAO
rep(1,10) 
rep(c(1,2),5) 
c(rep(0,10),rep(1,5))


x <- 1:10

x[3]
x[2:4]
x[c(2,4)]
x[x<4]
x[-2] #todos menos o elemento '2', no caso.


#MATRIZ
matriz <- matrix(1:10,2,5,1)

matriz2 <- matrix(1:10,ncol=2)


summary(matriz2)


x <- 1:12
dim(x) <- c(2,3,2) #Linha| Coluna | Matriz
x

y <- array(1:12,c(2,3,2))
y

dim(x)
dim(y)

dimnames(x) <- list(
  lat<-c("A","B"),
  long<-c("a","b","c"),
  alt<-c("primeira","segunda"))



x
#PROCURANDO
x[1,2,1] #Linha Coluna Matriz

x[1,2,] #Linha Coluna Tudo

x[1,,1] #Linha Tudo Matriz

x[,2,1] #Tudo Coluna Matriz


