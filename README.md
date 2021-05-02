<p align = "center">
<img src="images/logo.jpg" width=300>
</p>

# TRABALHO FUNDAMENTOS DE SISTEMAS INTELIGENTES ⌨
##  O trabalho consiste em implementar um sistema de navegação automática de um agente utilizando o algoritmo de busca em **largura, profundidade, gulosa e AEstrela**
***********

## [Descrição do trabalho](docs/TrabalhoBusca.pdf)
***********

# Algoritmos
## Sem Informação
* Busca em Largura (BFS)
* Busca em Profundidade (DFS)

## Com Informação
* Busca Gulosa 
* Busca A*


***********

# Detalhes sobre o Trabalho
## Legendas

Simbolo   | Descrição
:-------: | ------------------
-1         | Parede
p         | Parede
1         | Caminho vale 1
4         | Caminho vale 4
10        | Caminho vale 10
20        | Caminho vale 20
R         | Recompensa
9         | Caminho para o objetivo


***********

## Mapa utilizado para a busca BFS e DFS em OO
### Representação do mapa de pesos 
  0 | 1 | 2 | 3 | 4 |
:--:|:-:|:-:|:-:|:-:|
 1  | 1 | 10| 20| 0 |
20  |"p"|"p"| 1 | 0 |
1   | 1 | 4 | 1 |"R"|
1   |"p"|"R"|20 |10 |
10  |"p"|"p"| 1 |"R"|
1  | 1  |20 |"F"|"p"|
1  | 4  |"R"|"p"|"R"|
1  | 1  | 1 |04 |10 |

***********
### Representação do mapa de nós

  0 | 1 | 2 | 3 | 4 |
:--:|:-:|:-:|:-:|:-:|
 a  | b | c | d | e |
f   |g  |h  | i | j |
k   |l  |m  | n |o  |
p   |q  |r  |s  |t  |
u   |v  |w  |x  |y  |
z   | aa|bb |cc |dd |
ee  | ff|gg |hh |ii |
jj  | kk|ll |mm |nn |
***********


## Mapa utilizado para a busca BFS e BGS em Script
### Representação do mapa de pesos

  0 | 1 | 2 | 3 | 4 | 5 | 6 |
:--:|:-:|:-:|:-:|:-:|:-:|:-:|
 1  | 1 | 1 | 1 | 1 | 20| -1|
 1  | 0 | 0 | 0 | 0 | 1 | 0 |
 1  | 4 | 10| 10| 0 | 1 | 1 | 
 0  |-1 |10 |-1 | 0 | 0 | 1 |
-1  | 0 | 4 | 0 | 0 | 1 | 1 |
4   | 0 |-1 | 0 | 0 | 1 | 0 |
1   | 1 | 1 | 1 | 4 | 1 | 1 |
0   | 1 | 0 | 10| 0 | 0 | 1 | 
0   | 1 | 1 | 1 | -2| 0 | 10|
-1  | 4 | 0 | 0 | 4 | 4 |-1 |

### Representação do mapa de nos

  0 | 1 | 2 | 3 | 4 | 5 | 6 |
:--:|:-:|:-:|:-:|:-:|:-:|:-:|
 0  | 1 | 2 | 3 | 4 | 5 | 6 |
 7  | 8 | 9 | 10| 11| 12| 13|
 14 | 15| 16| 17| 18| 19| 20| 
 21 | 22| 23| 24| 25| 26| 27|
 28 | 29| 30| 31| 32| 33| 34|
 35 | 36| 37| 38| 39| 40| 41|
 42 | 43| 44| 45| 46| 47| 48|
 49 | 50| 51| 52| 53| 54| 55| 
 56 | 57| 58| 59| 60| 61| 62|
 64 | 64| 65| 66| 67| 68| 69|



## Estrutura OO para gerar o mapa 
* [No](images/No.png)
* [Adjacente](images/Adjacentes.png)
* [Mapa](images/Mapa.png)
* [No](images/No.png)
***********
## Algoritmos OO busca  
* [Largura](images/Largura.png)
* [Profundidade](images/BuscaProfundidadeOO.png)

***********
## Algoritmos Script em Busca 
* [Mapa](images/mapaScript.png)
* [Calculo das Adjacentes](images/calculoAdjacenciasPesos.png)
* [Calculo Heuristicas](images/calHeuristicas.png)
* [Busca Gulosa Vars](images/buscaGulosaVar.png)
* [Busca Gulosa](images/buscaGulosa.png)
* [Busca Profundidade Vars](images/buscaProfundidade.png)
* [Busca Profundidade](images/buscaProfundidadeVar.png)
* [Busca Profundidade](images/buscaProfundidadeVar.png)
***********
***********
## Resultatos
* [Busca Gulosa Distancia Manthattan](images/GulosaDistanciaManhattan.png)
* [Busca Gulosa em Linha Reta](images/GulosaLinhaReta.png)
* [Busca Profundidade](images/Profundidade.png)
* [Busca Largura](images/buscaLargura.png)
* [Busca Largura *](images/buscaLargura2.png)
***********
***********


