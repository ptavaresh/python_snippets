"""

pattern
(values) = [(expresssion) for (value) in (collection)]
"""


squares = [x * x
    for x in range(10)]
print(squares)

# List comprehensions: Filetring

even_squares = [x * x
    for x in range(10)
        if x % 2 == 0]
print(even_squares)
