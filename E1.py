Exercise 1: Write a function called chop that takes a list and modifies it, removing
the first and last elements, and returns None. Then write a function called middle
that takes a list and returns a new list that contains all but the first and last
elements

Answer:
letters = ['a', 'b', 'c', 'd']
chop(letters)

def chop(letters):
    del letters[0]
    del letters[-1]

print(letters)

letters = ['a', 'b', 'c', 'd']
middle(letters)

def middle(letters):
    return letters[1:-1]
    rest = middle(letters)

print(middle(letters))