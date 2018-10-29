import vtk

def geraListaTriangulos(listaVertices,listaArestas):
  listaTriangulos = []
  ladosTrianguloOk = 0
  v1 = "0"
  v2 = "0"
  v3 = "0"
  for vertice in listaVertices:
    for aresta in listaArestas:
        if aresta.find(vertice) != -1 :
            ladoTriangulo = aresta.split("-")
            ladosTrianguloOk += 1
        if ladosTrianguloOk == 1:
            v1 = ladoTriangulo[0]
            v2 = ladoTriangulo[1]
        if ladosTrianguloOk == 2:
            v3 = ladoTriangulo[1]
        if (aresta.find(v2) != -1) and (aresta.find(v3) != -1):
            triangulo = [v1,v2,v3]
            if triangulo not in listaTriangulos:
                listaTriangulos.append(triangulo)
  return listaTriangulos

def geraListaQuadrangulos(listaVertices,listaArestas):
    listaQuadrangulos = []
    ladosQuadranguloOk = 0
    v1 = "0"
    v2 = "0"
    v3 = "0"
    v4 = "0"
    for vertice in listaVertices:
      for aresta in listaArestas:
        if aresta.find(vertice) != -1 :
          ladoQuadrangulo = aresta.split("-")
          ladosQuadranguloOk += 1
        if ladosQuadranguloOk == 1:
          v1 = ladoQuadrangulo[0]
          v2 = ladoQuadrangulo[1]
        if ladosQuadrangulosOk == 2:
          v3 = ladoQuadrangulo[1]
        if (aresta.find(v2) != -1) and :
            if quadrangulo not in listaQuadrangulos:
                listaQuadrangulos.append(quadrangulo)
    return listaQuadrangulos


arquivo = open("dados.txt","r")
dados = arquivo.read() #Recebe string com arestas
listaArestas = dados.split(" ")
dados = dados.replace(" ","-") #Troca espacos por -
listaVertices = dados.split("-") #Transforma string em lista
listaVertices = list(set(listaVertices)) #Retira vertices duplicados
print(listaArestas)
print(listaVertices)
listaTriangulos = geraListaTriangulos(listaVertices,listaArestas)
print(listaTriangulos)
