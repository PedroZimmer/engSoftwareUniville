

def calctab(num1,num2):
    res = num1 * num2
    return res

print(calctab(2,3))

calctab2 = lambda num1,num2: num1 * num2
print(calctab2(2,3))


def gerartabuada(numero, regra):
    for i in range(11):
        print(regra(numero,i))
        
gerartabuada(10,calctab2)