def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def metros_para_centimetros(m):
    return m * 100

while True:
    print("1 - Celsius para Fahrenheit")
    print("2 - Metros para Centímetros")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        c = float(input("Digite a temperatura em Celsius: "))
        print("Fahrenheit:", celsius_para_fahrenheit(c))

    elif opcao == 2:
        m = float(input("Digite os metros: "))
        print("Centímetros:", metros_para_centimetros(m))

    elif opcao == 3:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")