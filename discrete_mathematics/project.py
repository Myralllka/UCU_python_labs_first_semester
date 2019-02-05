def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.
    """
    result = []
    with open(file_name, "r", encoding='utf-8') as input_file:
        matrix = input_file.readlines()
    for ind in range(len(matrix)):
        for column in range(len(matrix[ind])):
            if matrix[ind][column] == "1" and [column + 1, ind + 1] not in result:
                result.append([ind + 1, column + 1])
    return result


def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices's.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    result = {}
    a = set(j for i in edge_list for j in i)
    for each in a:
        result[each] = [j[1] for j in edge_list if j[0] == each]
        result[each].extend([j[0] for j in edge_list if j[1] == each])
    for each in result:
        result[each].sort()
    return result


def hamiltonian_cycle(in_graph, vertex, path=[]):
    '''
    Recursive search of Hamiltonian cycle

    Arguments:
        in_graph {dict} -- dictionary of graph
        vertex {str} -- vertex

    Keyword Arguments:
        path {list} -- current path (default: {[]})

    Returns:
        Hamiltonian cycle path or None
    '''

    if vertex not in set(path):
        path.append(vertex)
        if (len(path) == len(in_graph) and
                (path == [] or path[0] in in_graph[vertex])):
            return path
        for pt_next in in_graph.get(vertex, []):
            res_path = [i for i in path]
            candidate = hamiltonian_cycle(in_graph, pt_next, res_path)
            if candidate is not None:
                return candidate


if __name__ == "__main__":
    file_name = input("Create txt file with adjacency matrix.\nFile name: ")
    graph_dict = to_edge_dict(get_graph_from_file(file_name))
    print(hamiltonian_cycle(graph_dict, (list(graph_dict.keys())[0])))
