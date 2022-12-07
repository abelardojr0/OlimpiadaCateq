alfabeto = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
especiais = ("!","#",".","'","@","$","%","&","*","(",")","-","_","=","+","^","~",";",":","?","/", "|", '"',"£","¢","¬","§","ª","º","°","<",">","`",)
alfaMaiusculo = [letra.upper() for letra in alfabeto]

contNum = 0
contAlfa = 0
contEspec = 0
contMaiusc = 0
repetir = True


while(repetir):
    
    senha = input("Digite sua senha: ")
    
    if len(senha) > 4 and len(senha) < 8:
        for digito in senha:
            if digito in alfabeto:
                contAlfa += 1
            elif digito in especiais:
                contEspec +=1
            elif digito.isnumeric():
                contNum +=1
            elif digito in alfaMaiusculo:
                contMaiusc +=1
        if contNum > 0 and contAlfa > 0 and contEspec > 0 and contMaiusc >0:
            print("Senha válida")
            repetir = False
        else:
            print("Senha inválida, sua senha precisa ter pelo menos 1 número, 1 letra maiúscula, 1 letra minúscula, 1 caracter especial")
            print(f"Números: {contNum>0}")
            print(f"Letra Maiúscula: {contMaiusc>0}")
            print(f"Letra Minúscula: {contAlfa>0}")
            print(f"Caracter Especial: {contEspec>0}")
            
    elif(len(senha) <= 4 or len(senha) >=8):
            print("Senha inválida, sua senha precisa ter no mínimo 5 dígitos e no máximo 8")
        