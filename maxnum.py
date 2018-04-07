"""Return the largest integer in a list.

Given a list of integers, return the largest. Recursively

For example::

    >>> max_num([1, 3, 2, 4, 7, 2])
    7

    >>> max_num([5, 5, 5])
    5

    >>> max_num([10])
    10

    >>> max_num([-1, -2, -3])
    -1

    >>> max_num([-10, 0])
    0

"""


def max_num(num_list):
    """Returns largest integer from given list"""

    if len(num_list) == 1:
        return num_list[0]

    return max(num_list[0], max_num(num_list[1:]))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"
