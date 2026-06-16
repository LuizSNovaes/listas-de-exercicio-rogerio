def perfeito(numero):
    soma = 0
    
    for i in range(1, numero):

        if numero % i == 0:
            soma += i

    if soma == numero:
        return 1
    else:
        return 0

valor = int(input("Digite um número: "))

print(perfeito(valor))