class buscaMenorCaminho:
    def __init__(self, lista):
        self.listaAdjassencia = lista
        self.listaAdjassencia.addMultItemAllVertice(["Pai", "distancia"], [None, float('inf')])

    def menorCaminho(self, VA, VB):
        VA.addDado("distancia", 0)
        verticeAvaliado = VA
        listaAux = list()
        listaVerticesRelaxados = list()
        listaAux.append(verticeAvaliado)

        while len(listaAux) != 0:
            listaVerticesRelaxados.append(verticeAvaliado)
            for are in verticeAvaliado.aresta:

                if are.verticeLigado.dado["distancia"] > are.peso + verticeAvaliado.dado["distancia"]:
                    are.verticeLigado.dado["distancia"] = are.peso + verticeAvaliado.dado["distancia"]
                    are.verticeLigado.dado["Pai"] = verticeAvaliado

                    if are.verticeLigado not in listaVerticesRelaxados:
                        listaAux.append(are.verticeLigado)

            listaAux.remove(verticeAvaliado)

            if len(listaAux) > 0:
                verticeAvaliado = listaAux[0]

            for ver in listaAux:
                if verticeAvaliado.dado["distancia"] > ver.dado["distancia"]:
                    verticeAvaliado = ver

        if VB.dado["Pai"] != None:
            ListaResposta = list()
            verticeAvaliado = VB

            while verticeAvaliado != VA:
                ListaResposta.append(verticeAvaliado)
                verticeAvaliado = verticeAvaliado.dado["Pai"]

            ListaResposta.append(verticeAvaliado)
            # Talvez não de pra reverter no retorno, caso não de é só separar em 2 linhas
            return ListaResposta[::-1]
        else:
            return None
