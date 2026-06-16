nomes = []
medias = []

soma = 0

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))

    nomes.append(nome)
    medias.append(media)

    soma += media

media_geral = soma / 5

acima_media = 0

print("Alunos cadastrados:")

for i in range(5):
    print(nomes[i], "-", medias[i])

    if medias[i] > media_geral:
        acima_media += 1

print("Média geral da turma: ", media_geral)
print("Alunos acima da média: ", acima_media)