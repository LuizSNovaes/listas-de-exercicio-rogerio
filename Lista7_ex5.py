votos = [1, 2, 3, 2, 2, 1, 3, 3, 2, 1, 2, 3, 3, 2, 1, 3, 2, 2, 1, 3]

ruim = 0
bom = 0
excelente = 0

for voto in votos:

    if voto == 1:
        ruim += 1

    elif voto == 2:
        bom += 1

    elif voto == 3:
        excelente += 1

total = len(votos)

perc_ruim = (ruim / total) * 100
perc_bom = (bom / total) * 100
perc_excelente = (excelente / total) * 100

print("Ruim:", ruim, "votos -", perc_ruim, "%")
print("Bom:", bom, "votos -", perc_bom, "%")
print("Excelente:", excelente, "votos -", perc_excelente, "%")

if ruim > bom and ruim > excelente:
    print("Avaliação vencedora: Ruim")

elif bom > ruim and bom > excelente:
    print("Avaliação vencedora: Bom")

else:
    print("Avaliação vencedora: Excelente")
    