"""
Convert a linked list to a string.
"""

class Node():
    """
    Node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def stringify(node):
    """
    Func.
    """
    if not node:
        return 'None'
    res=str(node.data)
    curr=node.next
    while curr:
        res+=' -> '+str(curr.data)
        curr=curr.next
    res+=' -> None'
    return res
