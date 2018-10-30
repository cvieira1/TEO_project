from math import sqrt
import re

# trata a conexão com o arquivo
def padronizaArquivo():
    arquivo = open("dados.txt", "r")
    linha = arquivo.readline() # pega as linhas do arquivo
    linha = linha.replace("\n","")
    lista_entradas = linha.split(" ")
    arquivo.close() 
    return lista_entradas

# pega somente os vertices
def getListavertice(lista_arestas):
    lista_vertices = []
    lista_arestas_sep = []
    for v in lista_arestas:
        s = re.split("-", v)
        s = [int(s[0]), int(s[1])]
        lista_arestas_sep.append(s)
        for v2 in s:
            lista_vertices.append(int(v2))
            
    lista_vertices.sort()
    lista_vertices = list(set(lista_vertices))
    return lista_vertices, lista_arestas_sep

# retira valores duplicados de listas de listas
def Retira_valores_duplicados(lista_original):
    lista = lista_original.copy()
    tamanho = len(lista)
    pos = 0
    while True:
        if pos >= tamanho:
            break
            
        v = lista[pos]
        if v in lista[pos+1:tamanho]:
            indice = lista.index(v)
            lista.pop(indice)
            tamanho = len(lista)
        else:
            pos = pos + 1
        
    return lista

# OBS: TANTO O TRIANGULO QUANTO O QUADRANGULO SÓ FUNCIONAM SE EU ESCOLHER UM VÉRTICE QUALQUER
# E COLOCAR TODOS OS SEGMENTOS LIGADOS A ESSE VÉRTICE EM SEQUÊNCIA.
def geraListaTriangulos(listaArestas):
    lista_triangulos = []
    tamanho = len(lista_arestas)
    pos = 0
    for segmentosFixo in listaArestas:
        for segmentosV in lista_arestas[pos+1:tamanho]:
            temp1 = []
            temp2 = []
            valor_deletado = -1
            v1 = segmentosFixo[0]
            v2 = segmentosFixo[1]
            entrou = False

            if v1 in segmentosV:
                indice1 = segmentosV.index(v1)
                temp1 = segmentosV.copy()
                valor_deletado = temp1.pop(indice1)

                temp2 = segmentosFixo.copy()
                temp2.pop(0)

                temp1.extend(temp2)
                temp1.sort()
                entrou = True

            elif v2 in segmentosV:
                indice2 = segmentosV.index(v2)

                temp1 = segmentosV.copy()
                valor_deletado = temp1.pop(indice2)

                temp2 = segmentosFixo.copy()
                temp2.pop(1)

                temp1.extend(temp2)
                temp1.sort()

                entrou = True

            if entrou == True:
                if temp1 in lista_arestas:
                    temp1.append(valor_deletado)
                    temp1.sort()
                    lista_triangulos.append(temp1)
        pos = pos + 1

    return Retira_valores_duplicados(lista_triangulos)
