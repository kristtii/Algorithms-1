import algorithms
import data_structures


if __name__ == "__main__":
    # change the input string to specify the input file
    file = open('input.txt', 'r')

    n, p = [int(x) for x in file.readline().split(" ", 1)]

    g = graph(n, file)

    connected_components = algorithms.dfs(g)
    total_pairings = data_structures.calculate_pairings(connected_components)


    print(total_pairings)