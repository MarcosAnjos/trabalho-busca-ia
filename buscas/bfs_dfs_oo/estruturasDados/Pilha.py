from Mapa import Mapa


class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.no = [None] * self.tamanho
        self.topo = -1

    def empilhar(self, no):
        if not Pilha.pilhaCheia(self):
            self.topo += 1
            self.no[self.topo] = no
        else:
            print("A pilha já está cheia")

    def desempilhar(self):
        if not Pilha.pilhaVazia(self):
            temp = self.no[self.topo]
            self.topo -= 1
            return temp
        else:
            print("A pilha já está vazia")
            return None

    def getTopo(self):
        return self.no[self.topo]

    def pilhaVazia(self):
        return (self.topo == -1)

    def pilhaCheia(self):
        return (self.topo == self.tamanho - 1)


'''
mapa = Mapa()
pilha = Pilha(5)
pilha.empilhar(mapa.a)
pilha.empilhar(mapa.b)
pilha.empilhar(mapa.c)
print(pilha.getTopo().nome)
pilha.desempilhar()
pilha.empilhar(mapa.d)
'''