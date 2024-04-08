"""
Parse a linked list from a string.
"""

class Node:
    """
    Node.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    """
    Link. 
    """
    items = s.replace("->", "").split()
    print(items)
    head = None
    for data in reversed(items):
        if data != "None":
            node = Node(int(data), head)
            head = node
    return head
