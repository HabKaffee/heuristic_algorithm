import numpy as np
from random import choices

def find_clique(graph):
    clique = []
    vertices = list(graph.keys())
    weights = [len(i) for i in graph.values()]
    
    starting_vertex = choices(list(graph.keys()), weights=weights)[0]
    clique.append(vertices[starting_vertex])
    potential_nodes = set(graph[clique[-1]])

    while len(potential_nodes):
        potential_nodes_weights = [weights[node] for node in potential_nodes]
        new_vertex = choices(list(potential_nodes), weights=potential_nodes_weights)[0]
        clique.append(new_vertex)
        potential_nodes = list(set(graph[new_vertex]).intersection(potential_nodes))

    return clique

def solve(graph, threshold = 30000):
    max_clique_size = 0
    attempt = 0
    while attempt < threshold:
        current_clique = find_clique(graph)
        
        if len(current_clique) > max_clique_size:
            attempt = 0
            max_clique_size = len(current_clique)
        else:
            attempt += 1
    return max_clique_size
        