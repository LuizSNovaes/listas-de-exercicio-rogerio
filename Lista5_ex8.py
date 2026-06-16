soma_2_filhos = 0
qtd_2_filhos = 0

soma_0_filhos = 0
qtd_0_filhos = 0

soma_1_filho = 0
qtd_1_filho = 0

soma_geral = 0

for i in range(100):

    nome = input("Nome: ")
    salario = float(input("Salário: "))
    filhos = int(input("Número de filhos: "))

    soma_geral += salario

    if filhos == 2:
        soma_2_filhos += salario
        qtd_2_filhos += 1

    elif filhos == 1:
        soma_1_filho += salario
        qtd_1_filho += 1

    elif filhos == 0:
        soma_0_filhos += salario
        qtd_0_filhos += 1

if qtd_2_filhos > 0:
    media_2 = soma_2_filhos / qtd_2_filhos
else:
    media_2 = 0

if qtd_0_filhos > 0:
    media_0 = soma_0_filhos / qtd_0_filhos
else:
    media_0 = 0

if qtd_1_filho > 0:
    media_1 = soma_1_filho / qtd_1_filho
else:
    media_1 = 0

media_geral = soma_geral / 100

print("Média de quem possui 2 filhos:", media_2)
print("Média de quem não possui filhos:", media_0)

if media_1 > media_2:
    print("Maior média: pessoas com 1 filho")
elif media_2 > media_1:
    print("Maior média: pessoas com 2 filhos")
else:
    print("As médias são iguais")

print("Média salarial geral:", media_geral)