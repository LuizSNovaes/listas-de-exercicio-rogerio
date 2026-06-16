def positivo_negativo(numero):

    if numero >= 0:
        return 1
    else:
        return 0

n = int(input("Digite um número: "))
print(positivo_negativo(n))