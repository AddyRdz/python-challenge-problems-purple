# Problems Completed [ ]

# Your test/solution code here 

# Problem 0

# Problem 1

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


