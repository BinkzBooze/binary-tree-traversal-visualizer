# Randomized Binary Tree Generator and Traversal Visualization
## Video Demo: https://youtu.be/fVvBrPHchZg?si=abXxbtZYqaISlnYT
## Description
### About
This project generates a binary tree with a randomized structure and values. It then applies one of three traversal techniques based on user input: preorder, inorder, or postorder. The user specifies the desired tree level, the number of nodes, and the traversal technique. The tree's animation is powered by the 'rich' library for enhanced visual presentation.

### The Binary Tree Class
There is a class Node, which instantiates a new node for the binary tree.
Then there is a class BinaryTree, which is involved in tree generation, traversal, and printing to the terminal.

The binary tree is created by my own algorithm.
It is mainly done by the methods add_node() and build_tree().
There are also three helper functions for the add_node().

The add_node() method works like this:

First, if there is no root node, then set the current node as the root node.
Then, the next nodes are now added randomly, utilizing recursion with three main possibilies.
1. If both children are None, randomly decide where to place the value.
2. If one child is None, chooses to either set new node on the available child node or traverse the other child node.
3. If both children are not None, randomly decide to traverse the left or right child.

There is also a logic that ensures that the specified level is reached by the end of it, as well as the logic that prevents nodes from being added to a level that is higher than the maximum level. However, it is implemented badly since if a node has reached the maximum level without being able to assign a node to the current value, then it just tries again by calling add_node() again on the root node. This bad implementation can theoretically run infinite number of times if we are unlucky, but it is statistically impossible, as the probability of this happening 10 times in a row is 1/1024 or 0.1%.

Then the build_tree() method just uses a for loop to iterate N number of times, where N is the number of nodes specified by the user. I used the 'random' built-in module in order to assign differing numbers to the nodes, and stores the used digits to a set in order to prevent duplicates.

The traversal techniques are pretty common and I just learned them from the internet. Basically it's just three steps but the order in which we do these steps creates three unique traversals. These steps are:

1. yielding the node value
2. recursively call the same traversal technique to the node's left child,
3. recursively call the same traversal technique to the node's right child.

The 'yield' keyword is used instead of 'return' to make this a generator function, which poses numerous advantages like memory-efficiency. However, the main reason on why I used this, is so that I can return nodes but not exit the function, as using the 'return' keyword would make me need to store the data into a list and return that list afterwards.

Last but not the least, we have the print_tree() method. It works by using preorder traversal to generate a dictionary. This dictionary contains the levels as the keys, and lists of tuples as values. These tuples then contain the position and value of the node.

Using this, we can calculate the max_depth just by getting the highest key in the dictionary, and the max_width/spacing by performing some personalized calculations on the max_depth. We can change some of the calculations to change the look of the binary tree.

Now, using nested for loop, we iterate through every level, then we also iterate through every node in each level. One by one, the node values with specific whitespaces, alongside with the connection lines are carefully built up using the rich.Text object. I used this in order to make my text have colors or be stylized into italics/bold. Once the nodes and the connection lines on the non-leaf nodes are finished, they are finally printed onto the terminal.

All of these logic are then divided into three smaller methods called build_tree(), build_node_values(), and build_connection_lines(), in order to make the print_tree() method more modular and understandable.

### The Main Project File
Outside the classes, there are six functions, including main().

The clear_terminal() is a helper function that makes the animation of the traversal in the terminal possible, as it clears the terminal so that we can reprint the tree again cleanly.

The print_error() is a helper function that prints an error message to the console.

The prompt_user_traversal() is a function that lets the user choose between 1 to 3, to select a traversal techinque.

The prompt_user_level() is a function that lets the user choose between 1 to 4, to select the maximum level of the binary tree.

The prompt_user_nodes() is a function that lets the user choose the number of nodes in the binary tree, and the choices will be depending on the level chosen by the user.

Then there is main(), which integrates all of the classes and functions to finally run the binary tree traversal. It first prompts the user, then builds and prints the tree. It keeps on clearing the terminal and reprinting the binary tree with different highlighted node every second, to help in visualizing the traversal. It also keeps track of the traversed node by appending them into a list, then printing them into a terminal, so that we can use this code to run sorting using Binary Search Tree in the future.

My unit test focused on the three user prompt functions, as these three are the most likely to catch a lot of errors, as we all know that relying on user input is prone to errors. And so, ensuring that we catch these accurately is very important.






