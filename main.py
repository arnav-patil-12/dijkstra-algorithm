import run

# Create a graph with the desired size.
size = int(input("Enter desired number of vertices: "))
print("\n")
my_graph = run.create_graph(size)

# Label each vertex in the graph, use letters by convention.
run.label_graph(my_graph)

# Set the weight of each edge, the function sets negative weights to positive.
# Function takes only integer values of weights.
run.set_edges(my_graph)

# With the graph fully constructed, we can now implement the algorithm to find
# the shortest distance from a given point to every other point on the graph.
run.execute_dijkstra(my_graph)

# However, we see that having only the shortest distance is not of much use.
# Instead, we would benefit from having the shortest PATH from a starting point to
# Every other point on the graph.
run.print_paths(my_graph)
