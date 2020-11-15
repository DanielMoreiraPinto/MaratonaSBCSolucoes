#lendo numero de caixas
N = int(input())
#lendo valores das caixas em sequencia
caixas = []
for i in range(N):
    caixas.append(int(input()))
#verificando maior valor possivel ao escolher caixas surpresas
maior = 100 #valor inicial, caso encerre no inicio
for i in range(N):
    valor = 100
    for j in range(N):
        valor += caixas[j]
        if (i == j):
            break
    #verificando se o novo valor eh maior
    if valor > maior:
        maior = valor
print(maior)
