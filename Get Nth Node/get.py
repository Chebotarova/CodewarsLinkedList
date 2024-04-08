"""
Linked Lists - Get Nth Node.
"""

class Node(object):
    """Node class for reference"""
    def __init__(self, data):
        self.data = data
        self.next = None

def get_nth(node, index):
    """
    Get nth.
    """
    head=node
    temp=head
    count=0
    while head:
        if count==index:
            if not temp:
                raise IndexError
            return temp
        count+=1
        temp=temp.next
    raise IndexError
  