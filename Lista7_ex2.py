movimentacoes = []

while True:
    valor = float(input("Digite uma movimentação (0 para encerrar): "))

    if valor == 0:
        break

    movimentacoes.append(valor)

receitas = 0
despesas = 0

for valor in movimentacoes:

    if valor > 0:
        receitas += valor
    else:
        despesas += valor

saldo = receitas + despesas

print("RELATÓRIO")
print("Total arrecadado:", receitas)
print("Total gasto:", despesas)
print("Saldo final:", saldo)

if saldo > 0:
    print("Lucro")
elif saldo < 0:
    print("Prejuízo")
else:
    print("Empate")