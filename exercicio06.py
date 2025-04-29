a = [0]*5

for i in range(len(a)):
    a[i]=int(input(f"Digite o {i+1} número: "))

'''a.reverse()'''

for x in range(len(a)-1,-1,-1):
   print(a[x], end=" ")