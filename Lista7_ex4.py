precos = []

while True:

    preco = float(input("Digite o preço do produto: "))

    if preco < 0:
        break

    precos.append(preco)

valor_bruto = 0

for preco in precos:
    valor_bruto += preco

quantidade = len(precos)

if quantidade > 10:
    desconto = valor_bruto * 0.05
else:
    desconto = 0

valor_final = valor_bruto - desconto

print("Quantidade de produtos:", quantidade)
print("Valor bruto:", valor_bruto)
print("Desconto:", desconto)
print("Valor final:", valor_final)