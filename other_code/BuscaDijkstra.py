# from other_code.GrafoAdjassencia import ListaAdjassencia
#
#
# class buscaMenorCaminho:
#     def __init__(self, lista):
#         self.listaAdjassencia = ListaAdjassencia()
#
#     def menorCaminho(self, VA, VB):
#         self.listaAdjassencia.addMultItemAllVertice(["Pai", "distancia"], [None, float('inf')])
#         VA.addDado('distancia', 0)
#         verticeAvaliado = VA
#         ListaAux = list()
#         ListaAux.append(verticeAvaliado)
#
#         while len(ListaAux) != 0:
#             for are in verticeAvaliado.Aresta:
#
#                 if are.VerticeLigado.dado["distancia"] > are.peso + verticeAvaliado.dado["distancia"]:
#                     are.VerticeLigado.dado["distancia"] = are.peso + verticeAvaliado.dado["distancia"]
#                     are.VerticeLigado.dado["Pai"] = verticeAvaliado
#                     ListaAux.append(are.VerticeLigado)
#
#             while verticeAvaliado in ListaAux:
#                 ListaAux.remove(verticeAvaliado)
#
#             if len(ListaAux) > 0:
#                 verticeAvaliado = ListaAux[0]
#
#             for ver in ListaAux:
#                 if verticeAvaliado.dado["distancia"] > ver.dado["distancia"]:
#                     verticeAvaliado = ver
#
#         if VB.dado["Pai"] != None:
#             ListaResposta = list()
#             verticeAvaliado = VB
#
#             while verticeAvaliado != VA:
#                 ListaResposta.append(verticeAvaliado)
#                 verticeAvaliado = verticeAvaliado.dado["Pai"]
#
#             ListaResposta.append(verticeAvaliado)
#             # Talvez não de pra reverter no retorno, caso não de é só separar em 2 linhas
#             return ListaResposta.reverse()
#         else:
#             return None
