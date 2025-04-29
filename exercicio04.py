notas=[0.0]*5
soma = 0
notaacima=0

for e in range(len(notas)):
    notas[e]=float(input(f"Digite a {e+1} nota:"))

for i in range(len(notas)):
    soma += notas[i]

media = soma/len(notas)

for x in range(len(notas)):
    if notas[x] > media:
        notaacima+=1

print(f"A média da turma é {media}, e {notaacima} estão acima da média")