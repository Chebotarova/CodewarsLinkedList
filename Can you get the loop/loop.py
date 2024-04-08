"""
Can you get the loop ?
"""

class Node:
    """
    Node.
    """
    def __init__(self):
        self.next = None

def loop_size(node):
    """
    Loop.
    """
    visited_nodes = set()
    current_node = node
    while current_node not in visited_nodes:
        visited_nodes.add(current_node)
        current_node = current_node.next
    loop_length = 0
    loop_node = current_node
    while True:
        loop_length += 1
        loop_node = loop_node.next
        if loop_node == current_node:
            break
    return loop_length
