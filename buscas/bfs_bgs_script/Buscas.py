import numpy as np 
from collections import deque

linhas = 10 #qtd linhas da matriz
colunas = 7 #qtd colunas 
opt_mhtn = 0 #seleciona distancia manhattan como heuristica
opt_dtlr = 1 #seleciona distancia em linha reta como heuristica
sw_adjs = 0 #selecao de adjencia
sw_pesos = 1 #selecao de pesos

def resetMap():
    mapa = [
        [1,  1 ,  1,  1,  1,  20,  -1],      #a,b,c,d,e
        [1,  0 ,  0,  0,  0,  1,    0],       #f,g,h,i,j
        [1,  4,  10,  10, 0,  1,    1],        #k,l,m,n,o
        [0, -1,  10, -1,  0,  0,    1],         #p,q,r,s,t
        [-1,  0,   4,  0,  0,  1,    1],          #u,v,w,x,y
        [4,  0,  -1,  0,  0,  1,    0],          #u,v,w,x,y
        [1,  1,   1,  1,  4,  1,    1],         #z,aa,bb,cc,dd
        [0,  1,   0,  10, 0,  0,    1],       #ee,ff,gg,hh,ii
        [0,  1,   1,  1, -2,  0,   10],        #jj,kk,ll,mm,nn
        [-1,  4,   0,  0,  4,  4,   -1]
    ]   
    
    return mapa
#calculo de adjacancias
#pesos 0 = parede, aparece na lista porem esta vazia
#      1, 4, 10, 20 normais com pesos diferentes
#       -1 recompensas
#       -2 objetivos

def calcAdjaPesos(mapa, linhas, colunas):
    adjacencias = [] #[[]] *linhas*colunas
    mat_pesos = [] #[[]] *linhas*colunas
    # adjacencias = [[]]

    for l in range(linhas):
        for c in range(colunas):
            elementos = []
            pesos = []
            elemento = l*colunas+c
         
            if mapa[l][c] == 0:
                adjacencias.append(elementos)
                mat_pesos.append(pesos)
            else:
                if l-1 >= 0:
                    if mapa[l-1][c] != 0:

                        # elementos.append((l-1)*colunas+c)
                        pesos.append(mapa[l-1][c])

                        elementos.append([(l-1)*colunas+c, [l-1, c]])
                if c-1 >= 0:
                    if mapa[l][c-1] != 0:

                        # elementos.append((l*colunas+c-1))
                        pesos.append(mapa[l][c-1])
                        
                        elementos.append([l*colunas+c-1, [l, c-1]])

                if c+1 < colunas:
                    if mapa[l][c+1] != 0:
                        
                        # elementos.append(l*colunas+c+1)
                        pesos.append(mapa[l][c+1])
                        
                        elementos.append([l*colunas+c+1, [l, c+1]])

                if l+1 < linhas:
                    if mapa[l+1][c] != 0:

                        # elementos.append((l+1)*colunas+c)
                        pesos.append(mapa[l+1][c])

                        elementos.append([(l+1)*colunas+c, [l+1, c]])

                # print("adjacentes = ", elementos)
                # print("pesos = ", pesos)
                adjacencias.append(elementos) #[elemento] = elementos
                mat_pesos.append(pesos) #[elemento] = pesos

    return [adjacencias, mat_pesos]

#CALCULO DE HEURISTICAS
#DISTANCIAS EM LINHA RETA E MANHATTAN
def calcHeuristicas(dest_i, dest_j):
    heuristicas = []
    dest_i = 8
    dest_j = 4

    # Para todo elemento do mapa
    for i in range(linhas):
        for j in range(colunas):
            aux_i = i
            aux_j = j
            mhtn = 0 #contador de saltos para mhtn
            cat_i = 0 #cateto i para dist em linha reta
            cat_j = 0 #cateto j para dist em linha reta
            elemento = i*colunas+j
                        
            while aux_i != dest_i: #or aux_i > dest_i: #se i for diferente do fim
                if aux_i < dest_i: #i < q fim
                    aux_i += 1 #soma ate chegar

                if aux_i > dest_i: #i > q fim
                    aux_i -=1 #subtrai ate chegar
                
                cat_i += 1 #incremento cateto i
                mhtn += 1 #acumula distanha mhtn

            while aux_j != dest_j: #or aux_j > dest_j: #msm coisa que 118

                if aux_j < dest_j:
                    aux_j += 1

                if aux_j > dest_j:
                    aux_j -= 1
                
                cat_j += 1
                mhtn += 1
            
            #calculo distancia em linha reta
            linha_reta = (((cat_i ** 2) + (cat_j ** 2)) ** 0.5)
            h = [mhtn, linha_reta]
            heuristicas.append(h)
    
    return heuristicas

def buscaGulosaVars(ori_i, ori_j, dest_i, dest_j):
    
    visitados = []
    caminho = []

    #calculo dos nos origem e destino
    origem = ori_i*colunas+ori_j
    destino = dest_i*colunas+dest_j
    # print(origem, destino)
    print(":::Busca Gulosa:::")
    print("Origem = (",ori_i,", ",ori_j,")")
    print("Destino = (",dest_i,", ",dest_j,")")    

    #pegando lista da listas de adjacencias e dos pesos
    adjsPesos = calcAdjaPesos(mapa, linhas, colunas)
    adjs = adjsPesos[sw_adjs]
   
    #calculando heuristicas em linha reta e dist mhtn
    hrstc = calcHeuristicas(dest_i, dest_j)

    # h_opt = opt_mhtn #seleciona distancia manhattan como heuristica
    h_opt = opt_dtlr #seleciona distancia em linha reta como heuristica

    caminho = buscaGulosa([origem, [ori_i, ori_j]], [destino, [dest_i, dest_j]], visitados, adjs, hrstc, h_opt, caminho)

    print("::Caminho = ", caminho)
    print("::Saltos = ", len(caminho[0]))

    for elemento, coord in caminho[0]:
        mapa[coord[0]][coord[1]] = 9

    print(":::Mapa:::")
    for i in range(linhas):
        for j in range(colunas):
            print(mapa[i][j], end='\t')
        print()
    
def buscaGulosa(origem, destino, visitados, adjs, hrstc, h_opt, caminho):
    
    flag = False
    find = False
    menor = 99999999
    if len(visitados) == 0:
        visitados.append(origem)
    
    if origem == destino:
        # print("Destino encontrado!")
        c = tuple(visitados)
        caminho.append(c)
        find = True

    while not find and len(visitados) > 0:
        for i in adjs[origem[0]]:
            if menor > hrstc[i[0]][h_opt] and i not in visitados and not flag:
                menor = hrstc[i[0]][h_opt]
                prox = i
                
        if menor != 99999999 and flag == False:
            flag = True
            visitados.append(prox)
            return  buscaGulosa(prox, destino, visitados, adjs, hrstc, h_opt, caminho)
        else:
            if flag:
                visitados.pop()
            break

    return caminho

# VARIAVEIS INICIADAS PARA PROFUNDIDADE + PRINT DO MENOR CAMINHO ENCONTRADO
def profundidadeVars(ori_i, ori_j, dest_i, dest_j):

    visitados = [] #pilha de visitados
    caminhos = [] #lista do caminhos
    origem = ori_i*colunas+ori_j
    destino = dest_i*colunas+dest_j
    
    print(":::Busca Profundidade:::")
    print("Origem = (",ori_i,", ",ori_j,")")
    print("Destino = (",dest_i,", ",dest_j,")")   

    adjpesos = calcAdjaPesos(mapa, linhas, colunas) #0 lista [elemento, [i,j]], 1 lista pesos
    adjs = adjpesos[sw_adjs] #sw_adjs global

    profundidade([origem, [ori_i, ori_j]], [destino, [dest_i, dest_j]], visitados, caminhos, adjs)

    print(len(caminhos), 'caminhos encontrados')
    menor = range(100000)

    #Pega o menor caminho    
    for c in caminhos:
        if len(menor) > len(c): #pegando menor dos caminhos encontrados
            menor = c
    
    #Mostra o menor caminho
    print("Menor =", menor)
    print("Saltos =", len(menor))

    #Coloca o caminho no mapa
    for elemento, coord in menor: #menor:
        mapa[coord[0]][coord[1]] = 9

    print(":::Mapa:::")
    #Printa mapa com caminho desenhado
    for i in range(linhas):
        for j in range(colunas):
            print(mapa[i][j], end='\t')
        print()
    
# BUSCA EM PROFUNDIDADE ARMAZENANDO MULTIPLOS CAMINHOS
# START SETADO EM 0, 0
def profundidade(origem, destino, visitados, caminhos, adjs):
    flag = False
    if len(visitados) == 0:
        visitados.append(origem)
    if origem == destino:
        # print("Destino encontrado!")
        # print(visitados)
        c = tuple(visitados)
        caminhos.append(c)
        flag = True
    else:
            adjcs = adjs[origem[0]]
            for adj in adjcs:
                if adj not in visitados:
                    visitados.append(adj)
                    profundidade(adj, destino, visitados, caminhos, adjs)

            if len(visitados) > 0:
                visitados.pop()
    if flag == True: #flag da recursao True = do objetivo ate o primeiro antes do inicio da ida
        if len(visitados) > 0:
            visitados.pop()    


mapa = resetMap()

profundidadeVars(0, 0, 8, 4)

print()
print()
print()
print()
print()

mapa = resetMap()

buscaGulosaVars(0, 0, 8, 4)
