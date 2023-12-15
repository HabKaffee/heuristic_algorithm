import os
from time import perf_counter
from src.max_clique import solve
from src.utils import read_dimacs_file

def main():
    files = os.listdir('data/')
    for file in files:
        graph = read_dimacs_file('data/' + file)
        start = perf_counter()
        max_clique_size = solve(graph, threshold=20000)
        end = perf_counter()
        print(f'File = {file}\n{end - start}\t{max_clique_size}\n')
if __name__ == '__main__':
    main()