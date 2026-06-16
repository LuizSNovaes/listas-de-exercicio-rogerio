def ordenar(a, b, c):

    if a > b:
        a, b = b, a

    if a > c:
        a, c = c, a

    if b > c:
        b, c = c, b

    print(a, b, c)

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

ordenar(valor1, valor2, valor3)