codigo = 0
parar = 0
total = 0
cachorro = 0
simples = 0
comovo = 0
hamburguer = 0
queijoburguer = 0
refri = 0
print("Bem-Vindo(a) a lanchonete do Pedrão")
print("Para finalizar digite '66'")
while True:
  if codigo == 66:
    print("\nObrigado pela preferência")
    print("O pedido ficou num total de:", total)
    break
  else:
      print("\nCódigo do produto ou Encerrar('66'):")
      codigo = int(input())
      if codigo >=100 and codigo <=105:
        if codigo == 100:
          print("\nCachorro Quente...")
        if codigo == 101:
          print("\nBauru Simples...")
        if codigo == 102:
          print("\nBauru com ovo...")
        if codigo == 103:
          print("\nHamburguer...")
        if codigo == 104:
          print("\nCheeseburguer...")
        if codigo == 105:
          print("\nRefri...")        
        print("Insira a quantidade")
        qtd = int(input())
        if codigo == 100:
          cachorro = 1.2 * qtd
          total += cachorro
        else:
          if codigo == 101:
            simples = 1.3 * qtd
            total += simples
          else:
            if codigo == 102:
              comovo = 1.5 * qtd
              total += comovo
            else:
              if codigo == 103:
                hamburguer = 1.2 * qtd
                total += hamburguer  
              else:
                if codigo == 104:
                  queijoburguer = 1.3 * qtd
                  total += queijoburguer
                else:
                  if codigo == 105:
                    refri = 1 * qtd
                    total += refri
        #total += cachorro + simples + comovo + hamburguer + queijoburguer + refri        
      else:
          print("<Insira um código válido!>")