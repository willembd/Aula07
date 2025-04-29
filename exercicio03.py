nomes=["vivi", "karol", "lais", "guilherme", "willem"]

pesq = input("Digite o nome que você quer pesquisar: ")

for i in range(len(nomes)):
    if nomes[i] == pesq:
        print(f"O nome {nomes[i]} está na posição {i}")