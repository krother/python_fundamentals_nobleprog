Builtin functions
=================

In Python, there is a basic set of about 70 functions called **builtin functions**.
Many of them are shortcuts that make your everyday
programming a lot easier. Here, the 22 most important ones are given.

**These 22 functions are your basic vocabulary, knowing these is a must
to write Python efficiently!**

Exercise
--------

Try out the following builtin functions on the Python command line.
Look up their usage in the documentation.

::

   group A        group B        group C
   =======        =======        =======
   min            max            abs    
   range          sum            round  
   open           enumerate      zip    

----

Type Conversions
----------------

The **type conversion functions** convert one data type into another.
Examples for them are in an earlier section:

.. code:: python3

   int(x)        str(x)        dict(x)        bool(x)
   float(x)      list(x)       tuple(x)       set(x)

----

Input and output
----------------

Basic reading and writing data requires just three functions:

.. code:: python3

   print(s)      
   input(s)
   open(filename, mode)

----

Mathematical functions
----------------------

With ``abs()`` you can calculate the absolute value of a number:

.. code:: python3

   abs(-42)

With ``round()`` you can round numbers to a given number of digits:

.. code:: python3

   round(3.14159, 2)
   
----

Working with sequences
----------------------

There are tons of functions that help with **Python sequences** (lists,
dictionaries, tuples and *iterators*). The most common ones are:

.. code:: python3

   len(x)
   range(x)
   min(x)
   max(x)
   sum(x)
   reversed(x)
   enumerate(x)
   zip(x)
   

I will explain them one by one

Determining the length of sequences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``len()`` function returns an integer with the length of an
argument. It works with strings, lists, tuples, and dictionaries.

.. code:: python3

   data = [0, 1, 2, 3]
   len(data)

Summing up numbers
~~~~~~~~~~~~~~~~~~

The sum of a list of integer or float numbers can be calculated by the
``sum()`` function.

.. code:: python3

   data = [1, 2, 3, 4]
   sum(data)
   
Smallest and largest value
~~~~~~~~~~~~~~~~~~~~~~~~~~

The functions ``min()`` and ``max()`` determine the smallest and largest
value of a list:

.. code:: python3

   data = [3, 5, 1, 7]
   min(data), max(data)

Creating lists of integer numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``range()`` function allows to create lists of numbers on-the-fly.
There are two optional parameters for the start value and the step size.

.. code:: python3

   list(range(4))
   list(range(1, 5))
   list(range(2, 9, 2))
   list(range(5, 0, -1))
   
Note that because ``range()`` returns an **iterator** (a kind of lazy
on-demand list), you need to convert it to a list to see the data.

Enumerating list elements
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``enumerate()`` function helps with counting elements. It creates
tuples consisting of an integer number starting from zero and the
elements of the list.

.. code:: python3

   fruits = ['apple', 'banana', 'orange']
   list(enumerate(fruits))

   # [(0, 'apple'), (1, 'banana'), (2, 'orange')]

Note that ``enumerate()`` produces an iterator. To obtain a list, you
need to convert it.

``enumerate()`` is a great shortcut to loops with counter variables:

.. code:: python3

   i = 0
   for elem in data:
       print(i, elem)
       i += 1

becomes simply:

.. code:: python3

   for i, elem in enumerate(data):
       print(i, elem)


Reversing data
~~~~~~~~~~~~~~

The ``reversed()`` function reverses the order of list elements, but
does not change the original data. It returns an iterator.

.. code:: python3

   >>> data = [3, 5, 1, 7]
   >>> list(reversed(data))
   [7, 1, 5, 3]

Merging two lists
~~~~~~~~~~~~~~~~~

The ``zip()`` function associates the elements of two lists to a single
list or tuple. Excess elements are ignored.

.. code:: python3

   fruits = ['apple','banana','orange']
   prices = [0.55, 0.75, 0.80, 1.23]
   for fruit, price in zip(fruits, prices):
       print(fruit, price)
