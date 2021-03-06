import networkx as nx
from functions.drawings import draw_subtree
from functions.prims_functions import cost, min_prims_edge


def prims_algorithm(G, starting_node, draw=False, attrib=False):
    T = nx.Graph()
    T.add_node(starting_node)

    if draw:
        draw_subtree(G, T)

    while set(T.nodes()) != set(G.nodes()):
        e = min_prims_edge(G, T)
        T.add_edge(e[0], e[1], weight=cost(G, e))

        if draw:
            draw_subtree(G, T)

    if attrib:
        total_cost = sum(cost(G, e) for e in T.edges())

        print('________________Properties of the Tree T________________')
        print('________________________________________________________')
        print(f'V(T) = {list(T.nodes())}')
        print(f'E(T) = {list(T.edges())}')
        print(f'Total Cost = {total_cost}')
        print('________________________________________________________')

    return T
