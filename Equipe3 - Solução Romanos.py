romanos = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
soma = 0

def transformar(romano):

    arrayRomano = []
    arrayRomano[:0] = romano

    if romanos[arrayRomano[-1]] > romanos[arrayRomano[-2]]:
        global soma
        soma = romanos[arrayRomano[-1]] - romanos[arrayRomano[-2]]
        del arrayRomano[-1]
        del arrayRomano[-1]
    for i in arrayRomano:
        soma += romanos[i]
    return soma


num = input("Digite o número romano: ")
arrayTeste = ["I", "V", "X", "L", "C", "D", "M"]

cont = 0
vai = True
for letra in num:
    if letra.upper() in arrayTeste:
        cont += 1

if cont == len(num):
    print(transformar(num.upper()))
else:
    print("Você não digitou um número romano")
