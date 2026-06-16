soma = 0
quantidade = 0

continuar = "s"

while continuar == "s":

    numero = float(input("Digite um número: "))

    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    continuar = input("Deseja continuar? (s/n): ")

media = soma / quantidade

print("Média:", media)
print("Maior número:", maior)
print("Menor número:", menor)