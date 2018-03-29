"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    longest_distance = 0

    for i in range(num_holes):
        
        distance = min([abs(i-cafe) for cafe in cafes])
        longest_distance = max(distance, longest_distance)

    return longest_distance


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
