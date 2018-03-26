"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced()
    False

Imbalanced Six:

    1
   / \
  2   6
 / \
3   4
   /
  5

    >>> tree6i = N(1,
    ...         N(2,
    ...       N(3), N(4,
    ...           N(5))),
    ...                   N(6))
    >>> tree6i.is_balanced()
    False
"""

# Write unittests also

class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    ############### METHOD-1 ##############################################

    # Time complexity of calculating height of tree is O(n), since we have to
    # go through each node to find max
    
    def height(self):

        if not self:
          return 0

        left_ht = 0
        right_ht = 0

        if self.left:
          left_ht = 1 + self.left.height()

        if self.right:
          right_ht = 1 + self.right.height()

        return max(left_ht, right_ht)

    # This method has O(n^2) time complexity since ht is calculated again and again
    # To solve this, we use Method-2 where we visit each node only once and calculate
    # height and is_balanced both at the same time

    def is_balanced1(self):     
          """Is the tree at this node balanced?"""


          if self.left is None and self.right is None:
            return True

          if self.left is None:
            return self.right.height() == 0

          if self.right is None:
            return self.left.height() == 0

          return (self.left.is_balanced() and self.right.is_balanced() and 
                  abs(self.left.height() - self.right.height()) <= 1)


    ############### METHOD-2 ##############################################

    # Time Complexity is O(n) since we are visting each node
    # But the problem is if there is an unbalanced sub-tree deep down the call-stack,
    # it will propagate all the way up one-step at a time
    # Hence we can use try-catch, to immediately return to top caller (Method-3)

    def is_balanced_helper(self):

      if self.left is None and self.right is None:
        return (0, True)

      lt_ht = 0
      rt_ht = 0

      if self.left:
        ht, result = self.left.is_balanced_helper()
        if result:
          lt_ht = 1 + ht
        else:
          return (None, False)
      
      if self.right:
        ht, result = self.right.is_balanced_helper()
        if result:
          rt_ht = 1 + ht
        else:
          return (None, False)

      return (max(lt_ht, rt_ht), abs(lt_ht - rt_ht) <= 1)


    def is_balanced2(self):

      return self.is_balanced_helper()[1]


    ############### METHOD-3 ##############################################
    # with try-except

    def is_balanced_helper3(self):

      if self.left is None and self.right is None:
        return 0

      lt_ht = 0
      rt_ht = 0

      if self.left:
        lt_ht = 1 + self.left.is_balanced_helper3()
      
      if self.right:
        rt_ht = 1 + self.right.is_balanced_helper3()

      if abs(lt_ht - rt_ht) > 1:
        raise ValueError()
      
      return max(lt_ht, rt_ht)


    def is_balanced(self):

      try:
        self.is_balanced_helper3()
      except ValueError:
        return False
      return True





if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"
