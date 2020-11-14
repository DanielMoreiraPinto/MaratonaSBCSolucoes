#lendo N e M (numero de empregados e numero de festas)
linha = input()
info = linha.split()
N = int(info[0])
M = int(info[1])
#lendo pares (Ai, Bi), com A = idade do empregado i na empresa e B = gerente direto  do empregado i
empregado = [] #que guarda (idade, gerente direto e subordinados)
for i in range(N):
    dados = []
    linha = input()
    linha = linha.split()
    dados.append(int(linha[0])) #idade
    dados.append(int(linha[1])) #gerente direto
    dados.append([]) #lista vazia de subordinados(por enquanto)
    empregado.append(dados) #salvando informacoes do empregado
#vendo os gerentes diretos e preenchendo subordinados
for i in range(N):
    gerente = empregado[i][1] #quem é o gerente do empregado N
    #adicionando empregado N como subordinado de empregado gerente   
    empregado[gerente-1][2].append(i+1)
#lendo dados das festas
festa = []
for i in range(M):
    dados = []
    linha = input()
    linha = linha.split()
    dados.append(int(linha[0])) #anfitriao da festa
    dados.append(int(linha[1])) #idade minima na empresa
    dados.append(int(linha[2])) #idade maxima na empresa
    dados.append([]) #lista vazia de convidados (por enquanto)
    festa.append(dados) #salvando informacoes da festa
#verificando festas e seus convidados validos 
for i in range(M):
    idAnf = festa[i][0]-1 #indice do anfitriao no vetor empregados
    idGer = empregado[idAnf][1]-1 #indice do gerente do anfitriao
    idadeMin = festa[i][1] #idade minima da festa
    idadeMax = festa[i][2] #idade maxima da festa
    #adicionando anfitriao (se já não estiver na festa)
    if idAnf+1 not in festa[i][3]:
        festa[i][3].append(idAnf+1) #adicionando anfitriao na festa
    #adicionando empregados validos em ligacao direta com anfitriao (gerente e subordinados)
    if idGer+1 not in festa[i][3] and empregado[idGer][0] >= idadeMin and empregado[idGer][0] <= idadeMax:
        festa[i][3].append(idGer+1) #adicionando gerente na festa
    for subordinado in empregado[idAnf][2]:
        idSub = subordinado-1
        if subordinado not in festa[i][3] and empregado[idSub][0] >= idadeMin and empregado[idSub][0] <= idadeMax:
            festa[i][3].append(subordinado) #adicionando subordinado na festa
    #fazendo agora a verificacao de gerente direto e subordinados para cada novo membro da festa
    while (1):
        mudou = False #flag para encerrar busca
        for convidado in festa[i][3]:
            idConv = convidado-1 #indice do convidado no vetor empregado
            idGer = empregado[idConv][1]-1 #indice do gerente do convidado no vetor empregado
            #adicionando empregados validos em ligacao direta com o convidado atual
            if idGer+1 not in festa[i][3] and empregado[idGer][0] >= idadeMin and empregado[idGer][0] <= idadeMax:
                festa[i][3].append(idGer+1) #adicionando gerente na festa
                mudou = True #mudando flag e tornando valida uma nova busca
            for subordinado in empregado[idConv][2]:
                idSub = subordinado-1
                if subordinado not in festa[i][3] and empregado[idSub][0] >= idadeMin and empregado[idSub][0] <= idadeMax:
                    festa[i][3].append(subordinado) #adicionando subordinado na festa
                    mudou = True #mudando flag e tornando valida uma nova busca
        if not mudou:
            break #encerrando busca pois não houveram mais alterações nos convidados
#contando ocorrencias
for i in range(N):            
    contador = 0
    for j in range(M):
        contador += festa[j][3].count(i+1)
    print(contador, end="")
