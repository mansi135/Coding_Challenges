"""Given two linked lists, treat them like numbers and add them together.

This should take two linked lists in "reverse-digit" format, sum them up,
and return the head of a new linked list in "reverse-digit" format.

A list is in reverse-digit format if it is each digit as a node, in
least-significant-place-first order. For example, "123", would become
the list 3->2->1.

Let's add 1 + 2::

    >>> l1 = Node(1)
    >>> l2 = Node(2)
    >>> add_linked_lists(l1, l2).as_rev_string()
    '3'

Let's add 123 + 456::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '579'

Let's make sure we carry: 144 + 456:

    >>> l1 = Node(4, Node(4, Node(1)))
    >>> l2 = Node(6, Node(5, Node(4)))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '600'

Let's make sure it works with mismatched lengths: 123 + 89::

    >>> l1 = Node(3, Node(2, Node(1)))
    >>> l2 = Node(9, Node(8))
    >>> add_linked_lists(l1, l2).as_rev_string()
    '212'

"""

class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))


def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    carry = 0 

    new_node = Node(0) # start with dummy-node
    dummy_node = new_node

    while l1 or l2:

        if l1 is None:
            result = l2.data + carry
        elif l2 is None:
            result = l1.data + carry
        else:
            result = l1.data + l2.data + carry

        node_sum = result % 10
        carry = result / 10

        dummy_node.next = Node(node_sum)
        dummy_node = dummy_node.next 
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        
    new_node = new_node.next
    return new_node




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOWZA!\n"
