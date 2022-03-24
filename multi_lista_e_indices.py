equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento:"))
    valores.append(float(input("Valor:")))
    seriais.append(int(input("Numero Serial:")))
    departamentos.append(input("Departamento:"))
    resposta = input("\n digite \"S\" para continuar...\n").upper()


busca = input("Digite o nome do equipamento que deseja buscar:")

for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor...", valores[indice])
        print("Serial...", seriais[indice])




