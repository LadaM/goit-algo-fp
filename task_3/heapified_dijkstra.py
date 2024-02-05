import heapq

import networkx as nx

from heap_node import HeapNode


def find_shortest_paths(graph: nx.Graph, start):
    """
    Given a graph finds a shortest paths in the graph from start vertex to all other vertices
    Using a heap to optimize the path length
    """
    if start is None:
        print("Start vertex is None")
        return

    visited = set()
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start] = 0
    min_heap = [
        HeapNode(0, start)
    ]  # to ensure that heap is working correctly, we use custom class with comparators

    while min_heap:
        smallest_distance_node = heapq.heappop(min_heap)
        current_distance, current_node = (
            smallest_distance_node.distance,
            smallest_distance_node.node,
        )

        if current_distance > distances[current_node] or current_node in visited:
            continue

        visited.add(current_node)
        for neighbor, attributes in graph[current_node].items():
            distance = current_distance + attributes["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, HeapNode(distance, neighbor))

    return distances


def main():
    graph = nx.Graph()
    start_node = "A"
    test_data = [
        ("A", "B", 5),
        ("A", "C", 10),
        ("B", "D", 3),
        ("C", "D", 2),
        ("D", "E", 4),
        ("A", "E", 1),
        ("F", "E", 1),
        ("F", "G", 4),
    ]
    graph.add_weighted_edges_from(test_data)

    shortest_path = find_shortest_paths(graph, start_node)
    for node, distance in shortest_path.items():
        print(f"{start_node} -> {node}: {distance}")


if __name__ == "__main__":
    main()
