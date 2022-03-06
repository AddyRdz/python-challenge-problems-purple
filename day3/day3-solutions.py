# Problems Completed [ ]

# Your test/solution code here 
def intersect(list1, list2):
    inter = []
    for ele1 in list1:
        for ele2 in list2:
            if ele1 == ele2:
                inter.append(ele1)
    return inter
print(intersect(['a', 'b', 'c'], ['x', 'y', 'z']))

# Problem 0
# Write a function `min_max_product(list)` that return the product between the
# Use min() and max() to find the largest and smallest number of the list.
# largest value and the smallest value in the list.
# sum() both the product of min() and max().
# def min_max_product(list):
# Problem 1
# def find_highest_priced():
# use max() to find highest
# key=priced.get returns highest value
# Problem 2
def bracket_matcher(input):
  stack = []

  open_brackets = ('(', '{', '[')
  close_brackets = (')', '}', ']')

  bracket_pairs = {
    '[' : ']',
    '{' : '}',
    '(' : ')'
  }
  # loop over all the characters in the input string
  for char in input:
  # ignore anything that isn't a bracket
    if char in open_brackets:
  # encounter open bracket: keep track of it in your stack
      stack.append(char)
    elif char in close_brackets:
  # encounter closing bracket: pop() off the stack and compare
      open_pair = stack.pop()

      if len(stack) == 0:
        return False
  return True if len(stack) == 0 else False


# Problem 3
# def count_the_bits():


