from src.utils import create_matrix
from src.max_clique import find_max_clique
import numpy as np
import networkx as nx
import time
import cplex

class BranchAndBound:
    def __init__(self, graph, time_limit = 7500, verbosity=1):
        self.graph = graph
        self.eps = 1e-6
        self.model = cplex.Cplex()
        self.time_limit = time_limit
        self.best_found_solution = find_max_clique(graph=graph)
        self.best_f = len(self.best_found_solution)
        self.num_of_branches = 0
        self.used_vars = [0 for i in range(graph.number_of_nodes())]
        self.elapled_time = 0
        self.verbosity = verbosity
        self.print_threshold = int(10000/self.verbosity)
        
    def find_independent_sets(self):
        independent_sets = []
        
        strategies = [
            nx.coloring.strategy_largest_first,
            nx.coloring.strategy_random_sequential,
            nx.coloring.strategy_independent_set,
            nx.coloring.strategy_connected_sequential_bfs,
            nx.coloring.strategy_connected_sequential_dfs,
            nx.coloring.strategy_saturation_largest_first
        ]
        
        for strat in strategies:
            colored_set = nx.greedy_color(self.graph, strategy=strat)
            for color in set(color for node, color in colored_set.items()):
                independent_sets.append([node for node, value in colored_set.items() if value == color])
        
        return independent_sets

    def check_if_int_solution(self, solution):
        for value in solution:
            if abs(value - np.round(abs(value))) >= self.eps:
                return False
        return True

    def check_if_clique(self, nodes):
        subgraph = self.graph.subgraph(nodes)
        return ((len(nodes) * (len(nodes) - 1)) / 2) == subgraph.number_of_edges()

    def init_model(self):
        num_nodes = self.graph.number_of_nodes()
        
        self.model.variables.add(
            obj=[1] * num_nodes,
            lb=[0] * num_nodes,
            ub=[1] * num_nodes,
            types=[self.model.variables.type.continuous] * num_nodes,
            names=[str(i) for i in range(num_nodes)]
        )
        self.model.objective.set_sense(self.model.objective.sense.maximize)
        
        not_neighbours = list(nx.non_edges(self.graph))
        constraints = []
        for edge in not_neighbours:
                constraints.append([[str(edge[0]), str(edge[1])], [1.0, 1.0]])
        
        independent_sets = self.find_independent_sets()
        for ind_set in independent_sets:
            constraints.append(
                [[str(i) for i in ind_set], [1.0] * len(ind_set)])
        
        self.model.linear_constraints.add(
            lin_expr=constraints,
            senses=['L'] * len(constraints),
            rhs=[1.0] * len(constraints)
        )
        self.model.set_log_stream(None)
        self.model.set_error_stream(None)
        self.model.set_warning_stream(None)
        self.model.set_results_stream(None)

    def branching(self, solution):
        for node, value in enumerate(solution):
            if abs(value - np.round(value)) >= self.eps and self.used_vars[node] == 0:
                return node
        return None

    def branch_and_bound(self):
            end = time.time()

            if (end - self.start_time) > self.time_limit:
                print("Time limit")
                return
            try:
                self.model.solve()

                solution = self.model.solution.get_values()
                upper_bound = np.floor(self.model.solution.get_objective_value())
                
                if not (self.num_of_branches % self.print_threshold):
                    print(f'Num of branches = {self.num_of_branches}, current solution = {self.best_f}, upper bound = {upper_bound}')
                
                if self.best_f >= upper_bound:
                    return
                
                if self.check_if_int_solution(solution):
                    vertex_in_clique = [i for i in range(len(solution)) if np.round(solution[i]) != 0]
                    if not self.check_if_clique(vertex_in_clique):
                        return
                    if self.best_f < int(upper_bound):
                        self.best_found_solution = vertex_in_clique
                        self.best_f = int(upper_bound)
                
                branching_variable = self.branching(solution)
                if branching_variable is None:
                    return

                for branch in [0, 1]:
                    self.num_of_branches += 1
                    self.used_vars[branching_variable] = 1
                    branch_id = self.num_of_branches
                    
                    self.model.linear_constraints.add(
                        lin_expr=[[[str(branching_variable)], [1.0]]],
                        senses=['E'],
                        rhs=[branch],
                        names=[str(branch_id)]
                    )

                    self.branch_and_bound()
                    self.used_vars[branching_variable] = 0
                    self.model.linear_constraints.delete(str(branch_id))
                
            except:
                print('No solution found')
                return

    def run_branch_and_bound(self):
        self.start_time = time.time()
        self.init_model()
        print('BnB started')
        self.branch_and_bound()
        self.elapled_time = time.time() - self.start_time
        return self.best_f, self.best_found_solution
        