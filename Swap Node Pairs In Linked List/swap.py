"""
Swap Node Pairs In Linked List.
"""

class Node:
    """
    Node.
    """
    def __init__(self, *arg):
        self.next = arg

def swap_pairs(head):
    """
    Swap.
    """
    if not head or not head.next:
        return head
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head
    while current and current.next:
        first_node = current
        second_node = current.next
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        prev = first_node
        current = first_node.next
    return dummy.next
