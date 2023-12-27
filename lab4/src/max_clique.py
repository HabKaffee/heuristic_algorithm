import numpy as np
from random import choices
import networkx as nx

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

def find_max_clique(graph, threshold = 25000):
    adj_list = nx.to_dict_of_lists(graph)
    max_clique = []
    attempt = 0
    while attempt < threshold:
        current_clique = find_clique(adj_list)
        
        if len(current_clique) > len(max_clique):
            attempt = 0
            max_clique = current_clique
        else:
            attempt += 1
    return max_clique
