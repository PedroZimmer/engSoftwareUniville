#varargs 

def muitacoisa(*args):
    for umitem in args:
        print(umitem)
    print("Fim da lista")

muitacoisa(1,2)
muitacoisa(9,10,11,12,13)
muitacoisa()


#lista

def teste(lista,outro):
    for i in lista:
        print(i)
    print("Outro:",outro)
        
lista = [1,2,3,4,5,6,7,8,9,10]
outro = 1
teste(lista,outro)