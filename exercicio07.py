nome= [""]*2
senha= [0]*2

for i in range(len(nome)):
    nome[i] = input("Digite o nome do Usuario: ")
    senha[i] = int(input("Digite a sua senha: "))

lognome = input("Digite o nome do Login: ")
logsenha = int(input("Digite a Senha: "))

for x in range(len(nome)):
    if lognome == nome[x] and logsenha == senha[x]:
        print("Login Efetuado com Sucesso!!")
        break
    elif lognome == nome[x] and logsenha != senha[x]:
        print("Senha Incorreta!!")
        break
    else:
        print("Nome Incorreto!!")
        break