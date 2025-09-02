import time
import os
from rich.console import Console
from binary_tree import BinaryTree


def main():

    # Create a console object for colored printing.
    console = Console()

    # Prompt the user for the traversal technique and the number of levels and nodes.
    level = prompt_user_level()
    nodes = prompt_user_nodes(level)
    traversal = prompt_user_traversal()

    # Create a random binary tree with the specified number of levels and nodes, values being RNG from 1-100.
    tree = BinaryTree(level, nodes, traversal)
    tree.build_tree()
    tree.print_tree()
    console.print("\nPress Enter to start the traversal...")
    input()

    # List to track traversed nodes
    traversed_nodes = []

    # Perform the traversal and dynamically highlight nodes.
    for node in tree.traverse():
        clear_terminal()
        tree.print_tree(highlight=node)

        # Update traversed nodes
        traversed_nodes.append(str(node))

        # Print the "Output" section
        console.print(f"\n\nOutput using {traversal} traversal:", style="bold")
        console.print(" ".join(traversed_nodes), style='bold')

        time.sleep(1)  # Pause for 1 second between steps


def clear_terminal():
    """Helper function that clears the terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def print_error_msg(msg):
    """A helper function that prints an error message to the console."""
    print("-" * 50)
    print(msg)
    print("-" * 50)


def prompt_user_traversal(arg_input=None):
    """Prompts the user for the traversal technique."""

    traversals = {1: "preorder", 2: "inorder", 3: "postorder"}
    error_msg = "Invalid input. Please enter 1, 2, or 3."

    try:
        if arg_input is not None:
            prompt = arg_input
        else:
            prompt = int(input(
                "Which traversal would you prefer? (Preorder - 1 / Inorder - 2 / Postorder - 3): "))

        if prompt not in traversals: #.keys() for clarification's sake if needed.
            raise ValueError

    except ValueError:
        print_error_msg(error_msg)
        raise ValueError # For pytest to recognize the error

    return traversals[prompt]


def prompt_user_level(arg_input=None):
    """Prompts the user for the amount of levels in the binary tree."""

    MAX_LEVEL = 4
    error_msg = f"Invalid input. Please enter a valid number between 1 and {MAX_LEVEL}."

    try:
        if arg_input is not None:
            level = arg_input
        else:
            level = int(input(f"How many levels do you like? (1-{MAX_LEVEL}): "))

        if level not in range(1, MAX_LEVEL + 1):
            raise ValueError
    except ValueError:
        print_error_msg(error_msg)
        raise ValueError # For pytest to recognize the error

    return level


def prompt_user_nodes(level, arg_input=None):
    """Prompts the user for the amount of nodes in the binary tree, given the specified level."""

    min_node = level + 1
    max_node = 2 ** (level + 1) - 1
    error_msg = f"Invalid input. Please enter a valid number between {min_node} and {max_node}."

    try:
        if arg_input is not None:
            nodes = arg_input
        else:
            nodes = int(input(f"How many nodes do you like? ({min_node}-{max_node}): "))

        if nodes not in range(min_node, max_node + 1):
            raise ValueError
    except ValueError:
        print_error_msg(error_msg)
        raise ValueError # For pytest to recognize the error

    return nodes


# Main execution
if __name__ == "__main__":
    main()
