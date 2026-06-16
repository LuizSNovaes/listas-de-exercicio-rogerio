def depositar(saldo, valor):

    if valor < 0:
        print("Valor inválido.")
        return saldo

    return saldo + valor

def sacar(saldo, valor):

    if valor < 0:
        print("Valor inválido.")
        return saldo

    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo

    return saldo - valor

saldo = 0

while True:
    print("1 - Ver Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Saldo: R$", saldo)

    elif opcao == 2:
        valor = float(input("Valor para depósito: "))
        saldo = depositar(saldo, valor)

    elif opcao == 3:
        valor = float(input("Valor para saque: "))
        saldo = sacar(saldo, valor)

    elif opcao == 4:
        break

    else:
        print("Opção inválida.")