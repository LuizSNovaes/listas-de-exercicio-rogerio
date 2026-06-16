soma_positivos = 0
qtd_positivos = 0

soma_negativos = 0
qtd_negativos = 0

for i in range(100):

    numero = int(input("Digite um número: "))

    if numero >= 0:
        soma_positivos += numero
        qtd_positivos += 1

    else:
        soma_negativos += numero
        qtd_negativos += 1

print("Soma dos positivos: ", soma_positivos)
print("Quantidade de negativos: ", qtd_negativos)

if qtd_positivos > 0:
    media_positivos = soma_positivos / qtd_positivos
else:
    media_positivos = 0

if qtd_negativos > 0:
    media_negativos = soma_negativos / qtd_negativos
else:
    media_negativos = 0

print("Média dos positivos: ", media_positivos)
print("Média dos negativos: ", media_negativos)

diferenca = qtd_positivos - qtd_negativos

print("Diferença entre positivos e negativos: ", diferenca)