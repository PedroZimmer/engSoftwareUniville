num = int(input("Insira um número...\n"))
for i in range(1,num+1):
    if num % i == 0:    
        print(i)