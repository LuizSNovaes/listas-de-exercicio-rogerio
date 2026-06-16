soma_salarios = 0
quantidade = 0

continuar = "s"

while continuar == "s":

    nome = input("Nome: ")
    salario = float(input("Salário: "))
    filhos = int(input("Número de filhos: "))

    soma_salarios += salario
    quantidade += 1

    continuar = input("Deseja cadastrar outra pessoa? (s/n): ")

media = soma_salarios / quantidade

print("Média salarial geral:", media)