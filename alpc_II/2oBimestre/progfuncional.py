

def calctab(num1,num2):
    res = num1 * num2
    return res

print(calctab(2,3))

calctab2 = lambda num1,num2: num1 * num2
print(calctab2(2,3))


calctab3 = lambda calctab2: calctab2(2,3) * 2
print(calctab3(calctab2))