class Aresta:

    def __init__(self, peso=0, verticeLigado=None):
        self.peso = peso
        self.verticeLigado = verticeLigado

    def __str__(self):
        return "Peso:{}\nVertice Ligado:{}".format(self.peso, self.verticeLigado)


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

    def addAresta(self, peso, outroVertice):
        self.aresta.append(Aresta(peso, outroVertice))

    def __str__(self):
        return "{}".format(self.dado["nome"])

    def __repr__(self):
        return str(self)



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

    def __str__(self):
        return self.lista
