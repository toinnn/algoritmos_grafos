from myCode.grafoAdjassencia import *


class Node:
    def __init__(self, name, type=None, weight=None):
        self.name = name
        self.edges = list()
        self.data = dict()

        if (type and weight is not None):
            self.type = type
            self.weight = weight

    def append_edge(self, edge):
        self.edges.append(edge)

    def grau(self):
        return len(self.edges)


class Edge:
    def __init__(self, origin, destiny, weight):
        self.origin = origin
        self.destiny = destiny
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.edges = list()

    def addNode(self, name, type=None, weight=None):
        new_node = Node(name, type, weight)
        self.nodes[name] = new_node

    def addEdge(self, origin, destiny, weight):
        new_edge = Edge(self.nodes[origin], self.nodes[destiny], weight)

        self.edges.append(new_edge)
        self.nodes[origin].append_edge(new_edge)

    def ordem(self):
        return len(self.nodes)

    def tamanho(self):
        return len(self.edges)

    def densidade(self):
        return len(self.edges) / (len(self.nodes) * (len(self.nodes) - 1) / 2)

    def list_grau(self):
        return list(map(lambda x: x.grau(), list(self.nodes.values())))


def grafo_para_adjacencia(grafo):
    lista = ListaAdjassencia()

    for key in grafo.nodes:
        new_vertice = Vertice()
        new_vertice.addTipoDado("nome")
        new_vertice.addDado("nome", grafo.nodes[key].name)

        lista.addVertice(new_vertice)

    for key in grafo.nodes:
        for edg in grafo.nodes[key].edges:
            for vertice in lista.lista:
                if vertice.dado["nome"] == edg.origin.name:
                    destiny = lista.buscaVerticePorDado("nome", edg.destiny.name)
                    vertice.addAresta(edg.weight, destiny)




    # for edge in grafo.nodes[key].edges:
    #     print(edge.destiny)
    # print(lista.lista[])
    return lista
