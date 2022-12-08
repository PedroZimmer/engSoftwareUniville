




# 1. Importando os dados

library(readxl)

Seattle_Coffee <- read_excel("C:/#Dev/engSoftwareUniville/estComp/2aAtividade_2oBimestre/Seattle Coffee.xlsx")
View(Seattle_Coffee)

Seattle_Coffee

# 2. Criando fatores

cafes <- factor(Seattle_Coffee$Cafe)

cafesgl <- gl(7,1, 49, labels = c(cafes))
cidadesgl <- gl(7, 7, 49, labels = c("novayork", "sidney", "seattle", "singapore", "tokyo", "paris", "orlando"))
#cidadesgl <- gl(7,7, label=c(paste("Cidade", 1:7, sep="")))
#cafesgl <- rep(paste("Cafe", 1:7, sep=""), 7)
dados <- c(87.467,
68.781,
142.235,
99.845,
84.501,
74.069,
76.587,
55.446,
83.289,
133.545,
105.151,
96.418,
83.740,
62.278,
71.250,
99.526,
99.064,
114.119,
91.382,
57.799,
65.774,
71.895,
111.142,
85.936,
83.922,
83.261,
100.042,
102.104,
79.270,
99.367,
124.137,
137.280,
84.019,
59.356,
69.725,
68.703,
114.340,
79.813,
79.842,
92.233,
47.635,
38.722,
70.860,
114.382,
93.264,
109.462,
85.250,
68.629,
87.541
)


#dados <- gl(49, 1, 49, labels = c(novayork, sidney, seattle, singapore, tokyo, paris, orlando))




#3 Criando um data frame
tabela <- data.frame(Cidadesdata = cidadesgl, cafesdata = factor(cafesgl), dadosdata = dados)

resultado <- aov(dadosdata ~ cafesdata + Cidadesdata, tabela)

anova(resultado)


#teste tuckey 

testetuvkey <- TukeyHSD(resultado, "cafesdata")

plot(testetuvkey, cex=0.0001)