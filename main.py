from igraph import *


def main():
    g = Graph.Read_Ncol('myGraph.ncol', directed=False)
    vertex = 0
    path = []

    while True:
        edges = []
        count = 0
        for e in g.es:                                  # Conta os caminhos / Count the edges
            if e.source == vertex or e.target == vertex:
                count += 1
                edges.append(e)
        if count == 1:                                  # Se houver apenas um caminho / If there is only one edge
            path.append(g.vs(vertex)['name'][0])
            vertex = edges[0].target
            g.delete_edges(edges[0])
        elif count == 0:                                # Se não houver mais caminhos / If there are no edges
            break
        else:                                           # Se houver varios caminhos / If there are multiple edges
            for ed in edges:
                if ed in g.bridges():
                    edges.remove(ed)
                path.append(g.vs(vertex)['name'][0])
                vertex = edges[0].target
                g.delete_edges(edges[0])

    print('Eulerian path:')
    for i in range(len(path)):
        print(path[i], end=' ')


if __name__ == '__main__':
    main()
