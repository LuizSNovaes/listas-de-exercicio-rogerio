lista_a = []
lista_b = []

print("Lista A")

for i in range(6):
    valor = float(input("Digite um valor: "))
    lista_a.append(valor)

print("Lista B")

for i in range(6):
    valor = float(input("Digite um valor: "))
    lista_b.append(valor)

for i in range(6):
    lista_a[i] = lista_a[i] + lista_b[i]

print("Nova lista A:")

for valor in lista_a:
    print(valor)