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

# teste de ciclo infinito (fake ?)
# grafo.addEdge("C", "A",-1)
# grafo.addEdge("B", "C",-1)


# fica infinito (real ?)
# grafo.addEdge("C", "E", -1)
# grafo.addEdge("E", "D", -2)


grafo_adjacencia = grafo_para_adjacencia(grafo)
dijkstra = buscaMenorCaminho(grafo_adjacencia)

origem = grafo_adjacencia.buscaVerticePorDado("nome", "A")

destino = grafo_adjacencia.buscaVerticePorDado("nome", "F")

print("O caminho é:{}".format(dijkstra.menorCaminho(origem, destino)))
