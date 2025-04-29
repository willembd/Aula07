nomes=[""]*5
a=1
for i in range(len(nomes)):
    nomes[i] = input(f"Digite o nome do Aluno {a}:")
    a+=1

for i in range(len(nomes)):
    print(f"{nomes[i]} está na posição {i}")