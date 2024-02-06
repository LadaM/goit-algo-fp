import networkx as nx
from matplotlib import pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Recursive function going through the tree and adding edges between nodes
    """
    if node is not None:
        # Saving a node color in a graph
        graph.add_node(node.val, color=node.color)
        if node.left:
            graph.add_edge(node.val, node.left.val)
            left_pos = x - 1 / 2 ** layer
            pos[node.left.val] = (left_pos, y - 1)
            add_edges(graph, node.left, pos, x=left_pos,
                      y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            right_pos = x + 1 / 2 ** layer
            pos[node.right.val] = (right_pos, y - 1)
            add_edges(graph, node.right, pos, x=right_pos,
                      y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(
        data=True)]  # Collect node colors to display

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, with_labels=True, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


if __name__ == "__main__":

    # Creating the tree
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Displaying the tree
    draw_tree(root)
