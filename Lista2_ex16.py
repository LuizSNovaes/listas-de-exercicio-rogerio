bilhete = int(input("Digite o tipo de bilhete (unitario - 1, duplo - 2 ou 10 viagens - 3): "))
valor_pago = float(input("Digite o valor pago: "))

if bilhete == 1:
    preco = 1.30

elif bilhete == 2:
    preco = 2.60

elif bilhete == 3:
    preco = 12.00

else:
    print("Tipo de bilhete inválido.")
    preco = 0

if preco > 0:
    quantidade = int(valor_pago / preco)
    troco = valor_pago - (quantidade * preco)

    print("Quantidade de bilhetes:", quantidade)
    print("Troco: R$", troco)