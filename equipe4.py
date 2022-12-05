num = input("Digite um número: ")
milhar = 0
centena = 0
dezena = 0
unidade = 0
resposta = int(num)
while resposta != 0: 
    if len(num) >= 4:
        if resposta >= 1000:
            resposta = resposta - 1000
            milhar +=1
        elif resposta >= 100:
            resposta = resposta - 100
            centena += 1
        elif resposta >= 10:
            resposta = resposta - 10
            dezena +=1
        elif resposta >= 1:
            resposta = resposta - 1
            unidade += 1
    else:
        print("Inválido")
    
print(f"Milhar: {milhar},Centena: {centena}, Dezena: {dezena}, Unidade: {unidade} ")