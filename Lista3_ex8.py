numeros = int(input("Quantos números serão digitados? "))

soma_pares = 0
soma_impares = 0

qtd_pares = 0
qtd_impares = 0

for i in range(numeros):
    n = int(input("Digite um número: "))

    if n % 2 == 0:
        soma_pares += n
        qtd_pares += 1
    else:
        soma_impares += n
        qtd_impares += 1

print("Soma dos pares:", soma_pares)
print("Quantidade de pares:", qtd_pares)

print("Soma dos ímpares:", soma_impares)
print("Quantidade de ímpares:", qtd_impares)