def read_dimacs_file(filename:str):
    graph = dict()
    with open(filename, 'r') as f:
        for line in f:
            if not line or line.startswith('c'):
                continue
            if line.startswith('p'):
                vertex_num = int(line.split()[-2])
                edges_num = int(line.split()[-1])
                graph = {i: [] for i in range(vertex_num)}
            else:
                splitted_line = line.split()
                graph[int(splitted_line[1]) - 1].append(int(splitted_line[2]) - 1)
                graph[int(splitted_line[2]) - 1].append(int(splitted_line[1]) - 1)
    return graph
