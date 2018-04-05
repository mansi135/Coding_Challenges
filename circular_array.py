"""Implement a Circular Array

A circular array is defined by having a start and indexes (be
sure to think about optimizing runtime for indexing)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.print_array()
    harry
    hermione
    ginny
    ron
    >>> circ.get_by_index(2)
    'ginny'
    >>> print circ.get_by_index(15)
    None

However, the last item circles back around to the first item, 
so you can also rotate the list and shift the indexes. Positive
numbers rotate the list start to the right (or higher indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(1)
    >>> circ.print_array()
    hermione
    ginny
    ron
    harry
    >>> circ.get_by_index(2)
    'ron'

And negative numbers rotate the list start to the left (or lower
indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-1)
    >>> circ.print_array()
    ron
    harry
    hermione
    ginny
    >>> circ.get_by_index(2)
    'hermione'

And you can also rotate more than once around the ring::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-17)
    >>> circ.get_by_index(1)
    'harry'

If you add a new item after rotating, it should go at the end of
the list in its current rotation::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-2)
    >>> circ.add_item('dobby')
    >>> circ.print_array()
    ginny
    ron
    harry
    hermione
    dobby

"""

# Since we are optimizing for index(lookup) more than adding/removing ,
# a python list would be better choice than linked-list

# The general usecase for Circular array is never for adding though

class CircularArray(object):
    """An array that may be rotated, and items retrieved by index"""

    def __init__(self):
        """Instantiate CircularArray."""

        self._list = []
        self.start = 0
        self.end = -1

    def add_item(self, item):
        """Add item to array, at the end of the current rotation."""
        l = len(self._list)

        if l == 0 or self.end == l - 1:
            self._list.append(item)
        else:
            # shift things and make room for new entry, hence need to save the last one
            last = self._list[-1]
            for i in range(l-1, self.start, -1):
                self._list[i] = self._list[i-1]
            
            self._list[self.start] = item
            self._list.append(last)

            self.start = (self.start + 1 + l) % l


        l = len(self._list)
        self.end = (self.end + 1 + l) % l

         

    def get_by_index(self, index):
        """Return the data at a particular index."""
        l = len(self._list)

        if index > l - 1:
            return None

        return self._list[(self.start + index) % l]

    def rotate(self, increment):
        """Rotate array, positive for right, negative for left.

        If increment is greater than list length, keep going around.
        """
        l = len(self._list)

        self.start = (self.start + increment + l) % l
        self.end = (self.end + increment + l) % l

        

    def print_array(self):
        """Print the circular array items in order, one per line"""

        l = len(self._list)
        index = self.start

        for i in range(l):
            print self._list[index % l]
            index = index + 1



if __name__ == "__main__":
    print
    import doctest

    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED; YOU MUST BE DIZZY WITH JOY! ***"
    print
