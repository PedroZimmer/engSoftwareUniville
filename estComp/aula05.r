

nomes <- c('Pedro', 'Leandro', 'Marcelo', 'Rodrigo')
idade <- c(18,32,22,34)
mão <-factor( c('d', 'c', 'd', 'c'))

tabela <- data.frame(nomes,idade,mão)
tabela
tabela[2,]
tabela[,2]

tabela[,3] <- as.character(tabela[,3])
tabela[,3]

#procurar
tabela$mão
tabela$nomes[2]
tabela$nomes[1:3]

#adicionar coluna
tabela <- cbind(tabela, altura=c(120,130,140,150))
tabela

#Adiciona linha
tabela <- rbind(tabela, 'linha 7'= c('Luan', 20, 'c', 150))
tabela

#excluir coluna
tabela <- tabela[,-2]
tabela


#armazenar
i <- tabela[1:3,]
i

#escolher uma classe 
h <- tabela[tabela$nomes=='Pedro',]

#ordenar
tabela[order(tabela$nomes),] #OU REV
tabela

tabela[order(tabela$mão, tabela$altura),]
tabela




