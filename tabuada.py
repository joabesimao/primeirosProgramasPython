tabuada= int(input("digite o numero:"))
print("tabuada do numero",tabuada)

for valor in range(1,11,1):
    print(str(tabuada) + "x" + str(valor) + "=" + str(tabuada*valor))