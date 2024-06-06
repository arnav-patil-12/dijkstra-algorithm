from dijkstra import Graph


def create_graph(size):
    """
    (None) -> Graph

    Returns a Graph object of size parameter.
    """
    graph = Graph(size)
    return graph


def label_graph(graph):
    """
    (Graph) -> None

    Prompts user to enter vertex labels to construct graph.
    Stores each label as a string.
    Prints each vertex label and its corresponding index to the output.
    """
    for i in range(graph.size):
        vertex_label = str(input(f"Enter vertex label for INDEX {i}: "))
        graph.add_vertex_data(i, vertex_label)
    print("\n")
    return


def set_edges(graph):
    """
    (Graph) -> None

    Prompts user to enter start and end vertex INDICES and edge weights. Entering '.'
    in start vertex prompt will finish and return program.
    """
    weight = 1
    while weight != 0:
        weight = int(input("Enter edge weight (0 to finish): "))
        if weight == 0:
            return
        else:
            start = int(input("Enter start vertex INDEX: "))
            end = int(input("Enter end vertex INDEX: "))
            graph.add_edge(start, end, weight)
            print("\n")
    return


def execute_dijkstra(graph):
    """
    (Graph) -> None

    Prompts user for starting point, and prints the shortest path from
    the starting vertex to each other vertex in the graph.
    """
    start = str(input("Enter LABEL of starting point: "))
    print(f"Dijkstra's Algorithm starting from vertex INDEX {start}:")
    distances = graph.dijkstra(start)
    for i, d in enumerate(distances):
        print(f"Distance from {start} to {graph.vertex_data[i]}: {d}")
    return
