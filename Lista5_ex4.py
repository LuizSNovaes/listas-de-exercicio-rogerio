def par_impar(numero):

    if numero % 2 == 0:
        return 1
    else:
        return 0

n = int(input("Digite um número: "))
print(par_impar(n))