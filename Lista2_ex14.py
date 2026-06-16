nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("Média:", media)

if media >= 8:
    conceito = "A"
elif media >= 7:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 5:
    conceito = "D"
else:
    conceito = "E"

print("Conceito:", conceito)