lista = []

for i in range(6):
    numero = int(input("Digite um número: "))
    lista.append(numero)

pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Quantidade de pares:", len(pares))
print("Números pares:", pares)

print("Quantidade de ímpares:", len(impares))
print("Números ímpares:", impares)