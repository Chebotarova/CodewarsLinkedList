"""
Linked Lists - Alternating Split.
"""

class Node(object):
    """
    Node.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """
    Context.
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Split.
    """
    if head is None or head.next is None:
        raise ValueError
    first_head = head
    second_head = head.next
    first_curr = first_head
    second_curr = second_head
    while first_curr is not None and second_curr is not None:
        first_curr.next = second_curr.next
        if first_curr.next is not None:
            second_curr.next = first_curr.next.next
        first_curr = first_curr.next
        second_curr = second_curr.next
    return Context(first_head, second_head)
