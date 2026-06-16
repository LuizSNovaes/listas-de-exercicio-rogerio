contador = 0

for i in range(5):
    numero = float(input("Digite um número: "))

    if numero > 100:
        contador += 1

print("Quantidade de números maiores que 100:", contador)