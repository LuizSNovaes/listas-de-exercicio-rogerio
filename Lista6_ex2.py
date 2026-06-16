lista = []

for i in range(8):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("Múltiplos de 2: ")

for numero in lista:
    if numero % 2 == 0:
        print(numero)

print("Múltiplos de 3:")

for numero in lista:
    if numero % 3 == 0:
        print(numero)
        