"""
Linked Lists - Push & BuildOneTwoThree.
"""

class Node:
    """
    Node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """
    Push.
    """
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """
    Build.
    """
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained
