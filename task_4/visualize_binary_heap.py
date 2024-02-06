import heapq

import matplotlib.pyplot as plt
import networkx as nx


def add_edges(graph, heap, parent_index, pos, x, y, layer):
    """
    Recursive function going through the heap, adding nodes and edges between nodes to the graph
    """
    if parent_index < 0 or parent_index >= len(heap) - 1:
        return graph

    parent = heap[parent_index]
    graph.add_node(parent)
    left_child_index = 2 * parent_index + 1
    right_child_index = 2 * parent_index + 2

    # adding left subtree
    if left_child_index < len(heap):
        left_child = heap[left_child_index]
        graph.add_edge(parent, left_child)
        left_pos = x - 1 / 2**layer
        pos[left_child] = (left_pos, y - 1)
        add_edges(
            graph, heap, left_child_index, pos, x=left_pos, y=y - 1, layer=layer + 1
        )

    # adding right subtree
    if right_child_index < len(heap):
        right_child = heap[right_child_index]
        graph.add_edge(parent, right_child)
        right_pos = x + 1 / 2**layer
        pos[right_child] = (right_pos, y - 1)
        add_edges(
            graph, heap, right_child_index, pos, x=right_pos, y=y - 1, layer=layer + 1
        )

    return graph


def draw_heap(heap, max_heap=False):
    if max_heap:
        heap = [-i for i in heap]
    heapq.heapify(heap)
    if max_heap:
        heap = [-i for i in heap]

    graph = nx.DiGraph()
    pos = {(heap[0]): (0, 0)}
    heap_graph = add_edges(graph, heap, 0, pos, x=0, y=0, layer=1)

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap_graph,
        pos=pos,
        with_labels=True,
        arrows=False,
        node_size=1500,
        node_color="turquoise",
    )
    plt.show()


def main():
    heap = [100, 2, 3, 25, 11, 82, 7, 13, 38, 91, 4, 56]

    draw_heap(heap)
    draw_heap(heap, max_heap=True)


if __name__ == "__main__":
    main()
