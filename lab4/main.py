from src.utils import read_dimacs_file
from src.branch_and_bound import BranchAndBound
import networkx as nx
import pandas as pd

def main():
    data_path = './data/data/'
    files = [
        "brock200_1.clq",
        # "brock200_2.clq",
        # "brock200_3.clq",
        "brock200_4.clq",
        # "c-fat200-1.clq",
        # "c-fat200-2.clq",
        # "c-fat200-5.clq",
        # "c-fat500-1.clq",
        # "c-fat500-10.clq",
        # "c-fat500-2.clq",
        # "c-fat500-5.clq",
        # "C125.9.clq",
        "gen200_p0.9_44.clq",
        # "gen200_p0.9_55.clq",
        # "johnson8-2-4.clq",
        # "johnson8-4-4.clq",
        # "johnson16-2-4.clq",
        # "hamming6-2.clq",
        # "hamming6-4.clq",
        # "hamming8-2.clq",
        # "hamming8-4.clq",
        "keller4.clq",
        # "MANN_a9.clq",
        # "MANN_a27.clq",
        "MANN_a45.clq",
        # "p_hat300-1.clq",
        "p_hat300-2.clq",
        # "p_hat300-3.clq",
        # "san200_0.7_1.clq",
        # "san200_0.7_2.clq",
        # "san200_0.9_1.clq",
        # "san200_0.9_2.clq",
        "san200_0.9_3.clq",
        # "sanr200_0.7.clq"
    ]
    results = {
        "brock200_1.clq" : {'size' : 0, 'true_size' : 21, 'time' : 0},
        "brock200_2.clq" : {'size' : 0, 'true_size' : 12, 'time' : 0},
        "brock200_3.clq" : {'size' : 0, 'true_size' : 15, 'time' : 0},
        "brock200_4.clq" : {'size' : 0, 'true_size' : 17, 'time' : 0},
        "c-fat200-1.clq" : {'size' : 0, 'true_size' : 12, 'time' : 0},
        "c-fat200-2.clq" : {'size' : 0, 'true_size' : 24, 'time' : 0},
        "c-fat200-5.clq" : {'size' : 0, 'true_size' : 58, 'time' : 0},
        "c-fat500-1.clq" : {'size' : 0, 'true_size' : 14, 'time' : 0},
        "c-fat500-10.clq" : {'size' : 0, 'true_size' : 126, 'time' : 0},
        "c-fat500-2.clq" : {'size' : 0, 'true_size' : 26, 'time' : 0},
        "c-fat500-5.clq" : {'size' : 0, 'true_size' : 64, 'time' : 0},
        "C125.9.clq" : {'size' : 0, 'true_size' : 34, 'time' : 0},
        "gen200_p0.9_44.clq" : {'size' : 0, 'true_size' : 44, 'time' : 0},
        "gen200_p0.9_55.clq" : {'size' : 0, 'true_size' : 55, 'time' : 0},
        "johnson8-2-4.clq" : {'size' : 0, 'true_size' : 4, 'time' : 0},
        "johnson8-4-4.clq" : {'size' : 0, 'true_size' : 14, 'time' : 0},
        "johnson16-2-4.clq" : {'size' : 0, 'true_size' : 8, 'time' : 0},
        "hamming6-2.clq" : {'size' : 0, 'true_size' : 32, 'time' : 0},
        "hamming6-4.clq" : {'size' : 0, 'true_size' : 4, 'time' : 0},
        "hamming8-2.clq" : {'size' : 0, 'true_size' : 128, 'time' : 0},
        "hamming8-4.clq" : {'size' : 0, 'true_size' : 16, 'time' : 0},
        "keller4.clq" : {'size' : 0, 'true_size' : 11, 'time' : 0},
        "MANN_a9.clq" : {'size' : 0, 'true_size' : 16, 'time' : 0},
        "MANN_a27.clq" : {'size' : 0, 'true_size' : 126, 'time' : 0},
        "MANN_a45.clq" : {'size' : 0, 'true_size' : 345, 'time' : 0},
        "p_hat300-1.clq" : {'size' : 0, 'true_size' : 8, 'time' : 0},
        "p_hat300-2.clq" : {'size' : 0, 'true_size' : 25, 'time' : 0},
        "p_hat300-3.clq" : {'size' : 0, 'true_size' : 36, 'time' : 0},
        "san200_0.7_1.clq" : {'size' : 0, 'true_size' : 30, 'time' : 0},
        "san200_0.7_2.clq" : {'size' : 0, 'true_size' : 18, 'time' : 0},
        "san200_0.9_1.clq" : {'size' : 0, 'true_size' : 70, 'time' : 0},
        "san200_0.9_2.clq" : {'size' : 0, 'true_size' : 60, 'time' : 0},
        "san200_0.9_3.clq" : {'size' : 0, 'true_size' : 44, 'time' : 0},
        "sanr200_0.7.clq" : {'size' : 0, 'true_size' : 18, 'time' : 0},
    }
    for file in files:
        graph = nx.Graph(read_dimacs_file(data_path + file))
        BnB = BranchAndBound(graph, time_limit=7500, verbosity=2)
        print(f'Current graph = {file}')
        best_f, best_found_solution = BnB.run_branch_and_bound()
        results[file]['size'] = best_f
        results[file]['time'] = BnB.elapled_time
        # print(f'Filename = {data_path + file} | best_f = {best_f} | best_solution = {best_found_solution}')
    df = pd.DataFrame(results).T
    df.to_csv('test.csv')

if __name__ == '__main__':
    main()