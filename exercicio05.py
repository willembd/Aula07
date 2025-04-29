a = [0]*5
m = [0]*5
for i in range(len(a)):
    a[i]=int(input(f"Digite o {i+1} número: "))

x=int(input("Digite o número que ira fazer a multiplicação: "))

for e in range(len(m)):
    m[e] = a[e] * x
    print(f"{a[e]} X {x} = {m[e]}")

print("Resultado das Multiplicações:")
for o in range(len(m)):
    print(m[o], end=" ")

