class Aresta:

    def __init__(self):
        self.peso = 0
        self.verticeLigado = None


class Vertice:

    def __init__(self):
        self.aresta = list()
        self.dado = dict()

    def addDado(self, nomeDado, dado):
        self.dado[nomeDado] = dado

    def addTipoDado(self, tipoDado):
        self.dado[tipoDado] = None

    def getDado(self, key):
        return self.dado[key]

    def showKeys(self):
        return self.dado.keys()

    def addAresta(self, outroVertice, peso):
        aux = Aresta()
        aux.peso = peso
        aux.verticeligado = outroVertice
        self.aresta.append(aux)


class ListaAdjassencia:

    def __init__(self):
        self.lista = []

    def buscaVerticePorDado(self, nomeDado, dado):
        for aux in self.lista:
            if aux.dado[nomeDado] == dado:
                return aux

    def addVertice(self, vertice):
        self.lista.append(vertice)

    def addItemAllVertice(self, nomeDado, dado):
        for x in self.lista:
            x.addDado(nomeDado, dado)

    def addMultItemAllVertice(self, nomeDado, dado):
        for x in self.lista:
            for item in range(0, len(nomeDado)):
                x.addDado(nomeDado[item], dado[item])

    def alteraItemVertice(self, vertice, nomeDado, dado):
        vertice.addDado(nomeDado, dado)
