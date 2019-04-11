from myCode.bellmanFord import *
from myCode.createGraphExample import *


# grafo com valores positivos
grafo = graphOne()

# grafo com valores negativos
# grafo = graphTwo()



grafo_adjacencia = grafo_para_adjacencia(grafo)

# dijkstra = buscaMenorCaminho(grafo_adjacencia)
ford = buscaMenorCaminhoFord(grafo_adjacencia)



# grafo nomal com pesos positivos
origem = grafo_adjacencia.buscaVerticePorDado("nome", "A")
destino = grafo_adjacencia.buscaVerticePorDado("nome", "F")

# grafo com pesos negativos
# origem = grafo_adjacencia.buscaVerticePorDado("nome", "S")
# destino = grafo_adjacencia.buscaVerticePorDado("nome", "B")


# Codigo do algoritimo do dijkstra
# Aceita somente origem e destino e retorna uma lista de objetos Vertice
# que ja estao na ordem a serem seguidos
# print("O caminho é:{}\n".format(dijkstra.menorCaminho(origem, destino)))


# Colocando so a origem como parametro a funcao irar retornar uma lista com o historico de todos os pesos
# adicionando o destino vai devolver uma lista de objetos na ordem do melhor caminho
print(ford.menorCaminho(origem,destino))


