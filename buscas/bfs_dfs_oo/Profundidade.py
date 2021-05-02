from Mapa import Mapa
from estruturasDados.Pilha import Pilha


class Profundidade:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Pilha(60)
        self.fronteira.empilhar(inicio)
        self.achou = False

    def buscar(self):
        topo = self.fronteira.getTopo()
        print('Topo: {}'.format(topo.nome))
        '''Condição parar quando achou objetivo'''
        if topo == self.objetivo:
            self.achou = True
            print(':: FIM :: ')
        else:
            for i in topo.adjacentes:
                if self.achou == False:
                    print('Verificando se visitado: {}'.format(i.no.nome))
                    if i.no.visitado == False:
                        '''Add topo da pilha'''
                        i.no.visitado = True
                        self.fronteira.empilhar(i.no)
                        Profundidade.buscar(self)

        print('Desempilhou: {}'.format(self.fronteira.desempilhar().nome))


'''Teste'''

mapa = Mapa()
profundidade = Profundidade(mapa.a, mapa.mm)
profundidade.buscar()