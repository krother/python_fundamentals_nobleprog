Regular Expressions
===================

Exercise 1
----------

Examine the Regular Expression examples in the following code:

.. literalinclude:: regex.py

--------------

Exercise 2
----------

Download the Baby name data from `the US census
website <https://www.ssa.gov/oact/babynames/limits.html>`__ - files for
all years (use the 7 MB download).

Open one of the files and copy the contents into the Regex tester
`regex101.com <https://regex101.com/>`__.

Type in a Regular Expressions that finds the following:

-  a precise match of your name
-  your name with a wildcard symbol (``.``)
-  any name starting with your initial (use the ``+`` symbol)
-  a name with 3 or more ‘a’, using the repeat counter symbol ``{3,}``

--------------

Exercise 3
----------

Combine exercises 3 + 4 to do the same in Python.

To load a baby names into a Python string, use the code:

.. code:: python3

   text = open('yob2000.txt').read()

--------------

How can I learn more about Regular Expressions?
-----------------------------------------------

Start here:

-  `regex101.com <https://regex101.com/>`__ – an online RegEx tester
-  `regexone.com/ <http://regexone.com/>`__ – Learning regular
   expressions in 16+ lessons.
-  `Regex Golf <https://regex.alf.nu/>`__ – Very hard regular expression
   problems.
