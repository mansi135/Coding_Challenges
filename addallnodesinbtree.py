"""

We'll start with this tree::

                4
           2         7
         1   3     5   8

like this::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(7, Node(5), Node(8))
    ... )

    >>> t.sum_dfs()
    30

    >>> t.sum_bfs()
    30

"""


class Node(object):
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def __repr__(self):
        if self.left is None and self.right is None:
            return "<Node %s>" % self.data
        else:
            return "<Node %s l=%s r=%s>" % (self.data, self.left, self.right)

    def sum_dfs(self):

        node_sum = 0

        if self.left:
            node_sum += self.left.sum_dfs()

        if self.right:
            node_sum += self.right.sum_dfs()

        node_sum += self.data

        return node_sum

    # The disadvantage of using queue is extra storage space
    def sum_bfs(self):

        queue = [self]
        node_sum = 0

        while len(queue) > 0:
            n = queue.pop() # if using collections, use queue.deque , but that will have O(n^2) run time
            node_sum += n.data

            if n.left:
                queue.append(n.left)

            if n.right:
                queue.append(n.right)

        return node_sum



if __name__ == "__main__":
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NODES ADDED SUCCESSFULLY!\n"
