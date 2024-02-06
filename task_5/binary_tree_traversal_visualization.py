from collections import deque

from binary_tree_visualisation import draw_tree, Node
from colors import lighten_color

ROOT_COLOR = "#009688"


def visualize_binary_tree_traversal(tree):
    pass


def bfs_coloring(root: Node):
    visit_order = []
    current_color = ROOT_COLOR
    if not root:
        return []

    # initialization of the queue with the root
    queue = deque([root])

    while queue:  # while the queue is not empty
        # getting the first on the queue (FIFO)
        current_node = queue.popleft()
        print(current_node, end=" ")  # visit node
        current_node.color = current_color
        current_color = lighten_color(current_color)
        visit_order.append(current_node)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return visit_order


def dfs_coloring(root):
    if root is None:
        return

    stack = deque([root])
    current_color = ROOT_COLOR

    while stack:
        current_node = stack.pop()

        # Visit node
        current_node.color = current_color

        # Push right child first so that left child is processed first (LIFO)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

        # Update current_color for the next iteration
        current_color = lighten_color(current_color)


def get_tree():
    # Creating the tree
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    return root


def main():
    t1 = get_tree()
    bfs_coloring(t1)
    draw_tree(t1)

    t2 = get_tree()
    dfs_coloring(t2)
    draw_tree(t2)


if __name__ == "__main__":
    main()
