import copy


class buscaMenorCaminhoFord:
    def __init__(self, lista):
        self.listaAdjassencia = lista
        self.listaAdjassencia.addMultItemAllVertice(["Pai", "distancia"], [None, float('inf')])
        self.historicoLista = list()

    def menorCaminho(self, VA, VB=None):
        for i in range(len(self.listaAdjassencia.lista) - 1):
            VA.addDado("distancia", 0)
            verticeAvaliado = VA
            listaAux = list()
            listaVerticesRelaxados = list()
            listaAux.append(verticeAvaliado)

            while len(listaAux) != 0:
                listaVerticesRelaxados.append(verticeAvaliado)
                verticeAvaliado.aresta.sort(key=lambda x: x.peso)
                for are in verticeAvaliado.aresta:

                    if are.verticeLigado.dado["distancia"] > are.peso + verticeAvaliado.dado["distancia"]:
                        are.verticeLigado.dado["distancia"] = are.peso + verticeAvaliado.dado["distancia"]
                        are.verticeLigado.dado["Pai"] = verticeAvaliado

                        if are.verticeLigado not in listaVerticesRelaxados:
                            listaAux.append(are.verticeLigado)

                listaAux = list(filter((verticeAvaliado).__ne__, listaAux))

                listaAux.sort(key=lambda x: x.dado["distancia"])

                if listaAux:  verticeAvaliado = listaAux[0]

                for ver in listaAux:
                    if verticeAvaliado.dado["distancia"] > ver.dado["distancia"]: verticeAvaliado = ver

                self.historicoLista.append(copy.deepcopy(self.listaAdjassencia))

        if VB is not None:
            return self.lista_para_caminho(VA, VB)

        return self.historicoLista


    def lista_para_caminho(self, VA, VB):
        if VB.dado["Pai"] != None:
            ListaResposta = list()
            verticeAvaliado = VB
            while verticeAvaliado != VA:
                ListaResposta.append(verticeAvaliado)
                verticeAvaliado = verticeAvaliado.dado["Pai"]
                if verticeAvaliado in ListaResposta:
                    raise ValueError('Um ciclo Negativo foi encontrado')
            ListaResposta.append(verticeAvaliado)
            return ListaResposta[::-1]
        else:
            return None
