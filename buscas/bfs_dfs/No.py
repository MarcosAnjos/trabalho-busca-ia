class No:
    '''construct class No - salva somente vertices'''

    def __init__(self, nome):
        self.nome = nome
        self.visitado = False
        '''self.distanciaObjetivo = distanciaObjetivo'''
        '''vertives do grafo'''
        self.adjacentes = []

    '''Metodo add no-adjacente'''

    def addNoAdjacente(self, no):
        self.adjacentes.append(no)


'''
c = No("d")
print(c.nome)
print(c.visitado)
'''