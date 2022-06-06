"""
Execute the code sniplets one by one
"""

def add(a, b):
    """function with return value"""
    return a + b


result = add(3, 4)
print(result)

# ---------------------------------------------------

def add(a, b=5):
    """function with an optional parameter"""
    return a + b


result = add(3)
print(result)

# ---------------------------------------------------

def add(a, b, result):
    """function with a mutable parameter"""
    result.append(a + b)


sums = []
add(3, 5, sums)
add(7, 7, sums)
print(sums)


# ---------------------------------------------------

def add(*args):
    """function with flexible arguments"""
    result = 0
    for number in args:  # args is a list
        result += number
    return result


print(add(1, 2))
print(add(1, 2, 3, 4))

# ---------------------------------------------------

def add(**kwargs):
    """function with keyword arguments"""
    result = 0
    for key in kwargs:
        result += kwargs[key]
    return result


print(add(a=1, b=2))
print(add(a=1, b=2, c=3, d=4))

# ----------------------------------------------------

# anonymous function (discouraged)
add = lambda x, y: x + y
print(add(8, 9))

# ----------------------------------------------------

# functional patterns
from functools import reduce

data = [1, 2, 3, 4, 5, 6, 7]

def add(a, b):
    return a + b

def tenfold(x):
    return x * 10

def even(x):
    return x % 2 == 0

print(reduce(add, map(tenfold, filter(even, data))))

# ----------------------------------------------------

# decorator
from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

for i in range(10):
    print(fibonacci(i))
