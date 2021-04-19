from Mapa import Mapa


class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.Nos = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0

    def enfileirar(self, No):
        if not Fila.filaCheia(self):
            if self.fim == self.tamanho - 1:
                self.fim = -1
            self.fim += 1
            self.Nos[self.fim] = No
            self.numeroElementos += 1
        else:
            print("A fila já está cheia")

    def desenfileirar(self):
        if not Fila.filaVazia(self):
            temp = self.Nos[self.inicio]
            self.inicio += 1
            if self.inicio == self.tamanho:
                self.inicio = 0

            self.numeroElementos -= 1
            return temp
        else:
            print("A fila já está vazia")
            return None

    def getPrimeiro(self):
        return self.Nos[self.inicio]

    def filaVazia(self):
        return self.numeroElementos == 0

    def filaCheia(self):
        return self.numeroElementos == self.tamanho


'''
mapa = Mapa()
fila = Fila(5)
fila.enfileirar(mapa.a)
fila.desenfileirar()
fila.enfileirar(mapa.b)
print('Primeiro da Fila', fila.getPrimeiro().nome)
fila.desenfileirar()
fila.enfileirar(mapa.d)
fila.desenfileirar()
fila.enfileirar(mapa.e)
fila.enfileirar(mapa.f)
fila.enfileirar(mapa.g)
print('Primeiro da Fila', fila.getPrimeiro().nome)
'''