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
    Prints each vertex label and its corresponding index to the output.
    """
    for i in range(graph.size):
        vertex_label = str(input("Enter vertex label: "))
        graph.add_vertex_data(i, vertex_label)
        print(f"Vertex label: {vertex_label}, index: {i}")
    return


def set_edge(graph):
    """
    (Graph) -> None

    Prompts user to enter start and end vertex labels and edge weight. Entering '.'
    in start vertex will return program
    """
    start = ''
    while start != '.':
        start = str(input("Enter start vertex (enter . to finish): "))
        if start == '.':
            return
        else:
            end = str(input("Enter end vertex: "))
            weight = int(input("Enter edge weight: "))
            graph.add_edge_data(start, end, weight)
    return


def execute_dijkstra(graph):
    start = str(input("Enter start vertex: "))
    print(f"Dijkstra's Algorithm starting from vertex {start}:")
    distances = graph.dijkstra(start)
    for i, d in enumerate(distances):
        print(f"Distance from {start} to {graph.vertex_data[i]}: {d}")
    return
