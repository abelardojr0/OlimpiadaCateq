num = input("Digite um número até 7 dígitos: ")

milhar = 0
centena = 0
dezena = 0
unidade = 0
dezenaMilhar = 0
centenaMilhar = 0
milhao = 0

repetir = True

while repetir:
    if num.isnumeric() and len(num) <=7:
        repetir = False
    else:
        print("ERRO!")
        num = input("Digite um número até 7 dígitos: ")

        
resposta = int(num)

while resposta != 0: 
        if resposta >= 1000000:
            resposta = resposta - 1000000
            milhao +=1
        elif resposta >= 100000:
            resposta = resposta - 100000
            centenaMilhar +=1
        elif resposta >= 10000:
            resposta = resposta - 10000
            dezenaMilhar +=1
        elif resposta >= 1000:
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
    
print(f"Milhões = {milhao}\nCentenza de Milhar = {centenaMilhar}\nDezena de Milhar = {dezenaMilhar}\nMilhar: = {milhar}\nCentena = {centena}\nDezena = {dezena}\nUnidade = {unidade} ")