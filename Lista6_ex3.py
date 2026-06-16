logica = []
linguagem = []

print("Alunos de Lógica")

for i in range(10):
    matricula = int(input("Digite a matrícula: "))
    logica.append(matricula)

print("Alunos de Linguagem de Programação")

for i in range(8):
    matricula = int(input("Digite a matrícula: "))
    linguagem.append(matricula)

print("Matrículas que aparecem nas duas listas:")

for matricula in logica:
    if matricula in linguagem:
        print(matricula)