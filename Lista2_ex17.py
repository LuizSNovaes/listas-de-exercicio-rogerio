lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 + lado2 > lado3 and
    lado1 + lado3 > lado2 and
    lado2 + lado3 > lado1):

    print("O triângulo existe.")

    if lado1 == lado2 == lado3:
        print("Classificação dos lados: Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Classificação dos lados: Isósceles")
    else:
        print("Classificação dos lados: Escaleno")
        
else: print("Os valores não formam um triângulo.")