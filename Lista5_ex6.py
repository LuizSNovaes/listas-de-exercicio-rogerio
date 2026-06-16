def converter(segundos):

    horas = segundos // 3600
    segundos = segundos % 3600

    minutos = segundos // 60
    segundos = segundos % 60

    print("Horas:", horas)
    print("Minutos:", minutos)
    print("Segundos:", segundos)

tempo = int(input("Digite o tempo em segundos: "))

converter(tempo)