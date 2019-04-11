from myCode.grafo import *
def graphOne():
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

    # teste com valores negativos
    # grafo.addEdge("C", "A",-1)
    # grafo.addEdge("B", "C",-1)

    # Ciclo infinito bug na hora de rotanar a lista de Pai
    # grafo.addEdge("C", "E", -1)
    # grafo.addEdge("E", "D", -2)



    return grafo


def graphTwo():
    grafo = Graph()

    grafo.addNode("S")
    grafo.addNode("A")
    grafo.addNode("B")
    grafo.addNode("C")
    grafo.addNode("D")
    grafo.addNode("E")

    grafo.addEdge("S", "A", 10)
    grafo.addEdge("S", "E", 8)
    grafo.addEdge("A", "C", 2)
    grafo.addEdge("E", "D", 1)
    grafo.addEdge("D", "A", -4)
    grafo.addEdge("D", "C", -1)
    grafo.addEdge("C", "B", -2)
    grafo.addEdge("B", "A", 1)








    return grafo
