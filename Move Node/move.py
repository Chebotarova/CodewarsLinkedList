"""
Linked Lists - Move Node.
"""

class Node(object):
    """
    Node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    Context.
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Func.
    """
    node2=source
    node1=source.next
    node2.next=dest
    return Context(node1, node2)
