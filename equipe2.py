senha = input("Digite sua senha: ")
if len(senha) > 4 and len(senha) < 8 and senha.isnumeric():
    print("Senha válida")
else:
    print("Senha inválida")