import random
from rich.console import Console
from rich.text import Text

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self, max_level, total_nodes, traversal_type):
        self.root = None
        self.max_level = max_level
        self.node_count = 0
        self.total_nodes = total_nodes
        self.traversal_type = traversal_type
        self.picked_numbers = set()


    # 1st Helper method for adding nodes to the binary tree.
    def set_node_random(self, value, current_node):
        """
        A helper method for add_node().

        If the current node has no children, it sets a new node on the left or right child, randomly."""
        if random.choice([True, False]):
            current_node.left = Node(value)
        else:
            current_node.right = Node(value)
        self.node_count += 1


    # 2nd Helper method for adding nodes to the binary tree.
    def set_or_traverse_node(self, value, current_node, level, addable, traversable):
        """
        A helper method for add_node().

        If the current node has one child, it either adds a new node on the other child,
        or traverses the other child, randomly..
        """
        if random.choice([True, False]):
            setattr(current_node, addable, Node(value))
            self.node_count += 1
        else:
            self.add_node(value, getattr(current_node, traversable), level + 1)


    # 3rd Helper method for adding nodes to the binary tree.
    def traverse_node_random(self, value, current_node, level):
        """
        A helper method for add_node().

        If the current node has two children, it traverses either the left or right child, randomly."""
        if random.choice([True, False]):
            self.add_node(value, current_node.left, level + 1)
        else:
            self.add_node(value, current_node.right, level + 1)


    def add_node(self, value, current_node, level=0):
        """
        Adds a value to the binary tree. Randomized placement by default,
        but ensures reaching the specified max level.
        """
        if self.root is None:
            self.root = Node(value)
            self.node_count += 1

        # Ensure we reach max level at the start.
        elif self.node_count <= self.max_level:
            if current_node.left is None and current_node.right is None:
                self.set_node_random(value, current_node)
            elif current_node.left:
                self.add_node(value, current_node.left)
            elif current_node.right:
                self.add_node(value, current_node.right)

        # If max level is reached, restart from the root
        elif level == self.max_level:
            self.add_node(value, self.root)

        # Random placement after max level is reached.
        else:
            # Randomly decide where to place the value if both children are None.
            if current_node.left is None and current_node.right is None:
                self.set_node_random(value, current_node)
            # Chooses to set new node on the available child node or traverse the other child node.
            elif current_node.left is None:
                self.set_or_traverse_node(value, current_node, level, "left", "right")
            elif current_node.right is None:
                self.set_or_traverse_node(value, current_node, level, "right", "left")
            # If both children are not None, randomly decide to traverse the left or right child.
            else:
                self.traverse_node_random(value, current_node, level)

    def build_tree(self):
        """Builds the binary tree with unique random integers."""

        for _ in range(self.total_nodes):
            while True:
                value = random.randint(0, 100)
                if value not in self.picked_numbers:
                    self.picked_numbers.add(value)
                    self.add_node(value, self.root)
                    break


    # 1st Helper method for traversing the binary tree.
    def preorder(self, node=None):
        """Pre-order traversal of a binary tree."""
        if node is not None:
            yield node.value
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)


    # 2nd Helper method for traversing the binary tree.
    def inorder(self, node=None):
        """In-order traversal of a binary tree."""
        if node is not None:
            yield from self.inorder(node.left)
            yield node.value
            yield from self.inorder(node.right)

    # 3rd Helper method for traversing the binary tree.
    def postorder(self, node=None):
        """Post-order traversal of a binary tree."""
        if node is not None:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node.value


    def traverse(self):
        """Traverses the binary tree and returns the values in the specified order."""
        if self.traversal_type == "preorder":
            return self.preorder(self.root)
        elif self.traversal_type == "inorder":
            return self.inorder(self.root)
        elif self.traversal_type == "postorder":
            return self.postorder(self.root)
        else:
            raise ValueError("Invalid traversal type.")


    # 1st Helper method for printing the binary tree.
    def build_levels(self, node, depth=0, pos=0, levels=None):
        """
        Traverses the tree and builds a dictionary where each key is the depth level and
        the value is a list of tuples containing the position and value of nodes at that level.
        """

        # Initialize an empty dict if it doesn't exist yet.
        if levels is None:
            levels = {}

        # Proceed if the node exists.
        if node:
            # Initialize an empty list as the value of a depth if it doesn't exist yet.
            if depth not in levels:
                levels[depth] = []
            # Use preorder-type of recursion to build-up the dictionary of levels.
            levels[depth].append((pos, node.value))
            self.build_levels(node.left, depth + 1, pos * 2, levels)
            self.build_levels(node.right, depth + 1, pos * 2 + 1, levels)

        return levels


    # 2nd Helper method for printing the binary tree.
    def build_node_values(self, nodes, spacing, depth, highlight):
        """Builds the line of nodes at a specific depth level."""

        node_values = Text()

       # Iterate through each node (tuple of pos and value) in the list (value of dictionary).
        for pos, value in nodes:
            offset = pos * spacing // (2 ** depth) + spacing // (2 ** (depth + 1))
            node_values.append(" " * (offset - len(node_values)))

            # Center the node value and add padding
            value_str = str(value)
            padding = max(3 - len(value_str),0)
            left_pad = padding // 2
            right_pad = padding - left_pad
            centered_value = " " * left_pad + value_str + " " * right_pad

            # make the node colored if it is currently being traversed and is marked as highlighted.
            if value == highlight:
                node_values.append(centered_value, style="yellow")
            else:
                node_values.append(centered_value)

        return node_values


    # 3rd Helper method for printing the binary tree.
    def build_connection_line(self, nodes, next_level_nodes, depth, spacing):
        """Builds the connection lines between nodes at different levels."""

        connection_lines = Text()

        # Add connection lines to non-leaf nodes.
        for pos, _ in nodes:
            left_child = any(n[0] == pos * 2 for n in next_level_nodes)
            right_child = any(n[0] == pos * 2 + 1 for n in next_level_nodes)

            offset = pos * spacing // (2 ** depth) + spacing // (2 ** (depth + 1))
            connection_lines.append(" " * (offset  - len(connection_lines)))
            connection_lines.append("/" if left_child else " ")
            connection_lines.append(" ")
            connection_lines.append("\\" if right_child else " ")

        return connection_lines


    def print_tree(self, highlight=None):
        """Prints the binary tree with connections between nodes."""

        # Returns early if the tree is empty.
        if not self.root:
            return

        # Calculate maximum depth and width.
        levels = self.build_levels(self.root)
        max_depth = max(levels.keys())
        max_width = 2 ** max_depth
        spacing = max_width * 4

        console = Console()
        print()  # For offset on the top of the terminal.

        # Iterate through each depth level and print the nodes and connections.
        for depth in range(max_depth + 1):
            node_line = self.build_node_values(levels[depth], spacing, depth, highlight)
            console.print(node_line, style='bold')

            # Print connection lines between nodes at different levels, except the last level (non-leaf nodes).
            if depth < max_depth:
                connection_line = self.build_connection_line(levels[depth], levels[depth + 1], depth, spacing)
                console.print(connection_line, style='bold')

