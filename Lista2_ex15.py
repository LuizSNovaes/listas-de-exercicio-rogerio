nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("Média:", media)

if media >= 7:
    print("Aprovado")

elif media >= 3:
    print("Exame")

    nota_exame = 12 - media

    print("Nota mínima no exame para aprovação:", nota_exame)

else:
    print("Reprovado")