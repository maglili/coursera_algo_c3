import random
import numpy as np


def prim_mst(vertices, edge_list):
    s = random.choice(list(vertices.keys()))
    X = {s: True}  # Vertices spined so far
    T = []  # MST

    while X != vertices:
        min_cost = np.inf
        min_edge = None

        # Scaning thorugth all edges, find min cost edge
        for edge in edge_list:
            # both vertices in X or both vertices not in X, continue
            if (edge[0] in X and edge[1] in X) or (
                edge[0] not in X and edge[1] not in X
            ):
                continue
            if edge[2] < min_cost:
                min_edge = edge
                min_cost = edge[2]

        # add v to X
        if min_edge[0] not in X:
            X[min_edge[0]] = True
        if min_edge[1] not in X:
            X[min_edge[1]] = True

        # add e to T
        T.append(min_edge)

    return T


def prep_graph(path):
    """
    Opening file and create vertices and edges.
    Input:
        path (string): file path
    Output:
        vertices (dict): key = vertice, value = useless
        edge_list (list): e.g. [(node1, node2, cost),...]
    """
    vertices = {}
    edge_list = []
    with open(path, "r") as fh:
        for idx, row in enumerate(fh):
            row = row.split()
            if idx == 0 or row == []:
                continue

            node1, node2, edge_cost = [int(x) for x in row]

            # put nodes in vertices
            if node1 not in vertices:
                vertices[node1] = True
            if node2 not in vertices:
                vertices[node2] = True

            # put edge to edge_list
            edge_list.append((node1, node2, edge_cost))

    return vertices, edge_list


if __name__ == "__main__":
    random.seed(0)

    path = "./edges.txt"
    vertices, edge_list = prep_graph(path)
    MST = prim_mst(vertices, edge_list)

    # cost result
    res = 0
    for edge in MST:
        res += edge[2]
    print("res:", res)
