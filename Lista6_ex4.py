lista = []

for i in range(8):
    numero = int(input("Digite um número: "))
    lista.append(numero)

maior = lista[0]

for i in range(8):
    if lista[i] > maior:
        maior = lista[i]

print("Maior valor da lista:", maior)