# Dijkstra's Algorithm

## Introduction to the Algorithm

Dijkstra's algorithm the most straightforward algorithm used to find the shortest path from one vertex (or point) to another. The algorithm is implemented by repeatedly selecting the nearest unvisited vertex and calculating the distance to the other unvisited adjacent vertices.

A limitation is that Dijkstra's algorithm doesn't work for graphs with negatively-weighted edges. Instead, we use the Bellman-Ford algorithm. 

With that being said, let's dive right into the algorithm and code it in Python. 

## How it works:

[DSA Dijkstra's Algorithm](https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php) on w3schools lays out a good procedure that I will provide below:

> 1. Set initial distances for all vertices. Set the source vertex to 0, and the remaining to infinity.
> 2. Choose the closest unvisited vertex as the current vertex. So, the algorithm will always start with the source as the current vertex.
> 3. For each of the current vertex's unvisited adjacent vertices, calculate the distance from the source. If the new distance is lower than the previous distance, then update it to the lower value.
> 4. We are now done with the current vertex, so we mark it "visited." We do not check a visited vertex again.
> 5. Repeat steps 2-4 to choose a new current vertex until all vertices are visited.
> 6. We are left with the shortest path from the source to each vertex.

NOTE: This version of the algorithm does not provide the shortest path from the source to a given vertex, only the shortest distance from a given point to every other point on the graph. However, we will add this functionality to our code later.

TO BE ADDED: example run-through (same as w3), python code documentation, updates?
