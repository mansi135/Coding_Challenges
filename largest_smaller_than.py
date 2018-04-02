"""Return index of largest num in sorted list that is smaller than given num.

For example:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
    2

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    4

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
    1

Never find xnumber --- it's not smaller than itself!

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
    1

    >>> find_largest_smaller_than([-5, -2, 22, 25, 61, 100], 24)
    2

    >>> find_largest_smaller_than([-5, -2, 7, 8, 9, 12, 25, 26], 24)
    5

If no such number exists, return None:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
    True

"""

# handle the case where largest number can repeat
def find_largest_smaller_than_helper(nums, start, end, xnumber):
    """Find largest number in sorted list that is smaller than given number."""

    # Fail fast
    if nums[start] >= xnumber:
        return None

    #end_index = start + length - 1

    # Win fast  (But should we avoid so many if conditions??)
    if nums[end] < xnumber:
        return end

    mid = int((start + end) / 2) #  +1....

    res = None

    if nums[mid] < xnumber:
        if nums[mid + 1] >= xnumber:
            res = mid
        else:
            start = mid + 1
            res = find_largest_smaller_than_helper(nums, start, end, xnumber)

    elif nums[mid] >= xnumber:
        end = mid - 1
        res = find_largest_smaller_than_helper(nums, start, end, xnumber)

    return res

def find_largest_smaller_than(nums, xnumber):
    return find_largest_smaller_than_helper(nums, 0, len(nums)-1, xnumber)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE THE MAXIMUM!\n"

