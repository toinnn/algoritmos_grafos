from myCode.buscaDijkstra import *
from myCode.grafo import *

grafo = Graph()

grafo.addNode("A")
grafo.addNode("B")
grafo.addNode("C")
grafo.addNode("D")
grafo.addNode("E")
grafo.addNode("F")

grafo.addEdge("A", "B", 1)
grafo.addEdge("A", "C", 8)
grafo.addEdge("B", "D", 2)
grafo.addEdge("C", "B", 3)
grafo.addEdge("C", "E", 1)
grafo.addEdge("D", "F", 1)
grafo.addEdge("D", "C", 1)
grafo.addEdge("D", "E", 3)
grafo.addEdge("E", "D", 2)
grafo.addEdge("E", "F", 9)

lol = grafo_para_adjacencia(grafo)
kk = buscaMenorCaminho(lol)

origem = lol.buscaVerticePorDado("nome", "A")

destino = lol.buscaVerticePorDado("nome", "F")

# print(origem.aresta[0].verticeLigado.aresta[0])

print(kk.menorCaminho(origem, destino))

# diji = buscaMenorCaminho(grafo)
