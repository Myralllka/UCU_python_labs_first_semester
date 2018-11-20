# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.


def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    inp_file = open(file_name, "r", encoding='utf-8')
    result = ([[int(a) for a in each if a.isdigit()]
               for each in inp_file.readlines()])
    inp_file.close()
    return result

print(get_graph_from_file("data1.txt"))


def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

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


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> dict

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    return graph[edge[0]] == [edge[1]]


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
    return graph


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    graph[edge[0]].remove(edge[1])
    graph[edge[1]].remove(edge[0])
    return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    graph[node] = []
    return graph


def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    for each in graph:
        try:
            graph[each].remove(node)
        except ValueError:
            continue
    del graph[node]
    return graph


def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    file_out = open("output.dot", 'w', encoding='utf-8')
    print('graph {\n', file=file_out, end='')
    for each in graph:
        string = str(graph[each]).replace(
            ",", "").replace("]", "").replace('[', "")
        print('\t' + str(each) + ' -- { ' +
              string + " };", file=file_out, end='\n')
    print("}", file=file_out)
    file_out.close()
