<p align = "center">
<img src="logo/logo.jpg" width=300>
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
## Comparações entre os algoritmos de busca 

Algoritmos  | Completa? | Tempo       | Espaço    | Ótima? |
:----------:|:---------:|:-----------:|:---------:|:------:|
BFS         | 
DFS         | 
Gulosa      | 
A*          | 
***********

# Detalhes sobre o Trabalho

## Legendas

Simbolo   | Descrição
:-------: | ------------------
1         | Caminho vale 1
4         | Caminho vale 4
10        | Caminho vale 10
20        | Caminho vale 20
p         | Parede
R         | Recompensa

***********

## Mapa utilizado para a busca BFS e DFS
### Representação do mapa 
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
### Representação do mapa 
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


