from Mapa import Mapa
from estruturasDados.Fila import Fila


class Largura:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(50)
        self.fronteira.enfileirar(inicio)
        self.achou = False

    def buscar(self):
        primeiro = self.fronteira.getPrimeiro()
        print('Primeiro ::', primeiro.nome)

        if primeiro == self.objetivo:
            self.achou = True
            print(':: FIM :: ')
        else:
            temp = self.fronteira.desenfileirar()
            print("Desenfileirar ::", temp.nome)

            for a in primeiro.adjacentes:
                print("Verificando se ja visitado :: ", a.no.nome)
                if a.no.visitado == False:
                    a.no.visitado = True
                    self.fronteira.enfileirar(a.no)
            if self.fronteira.numeroElementos > 0:
                Largura.buscar(self)


'''teste'''
mapa = Mapa()
largura = Largura(mapa.a, mapa.bb)
largura.buscar()