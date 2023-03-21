Print
=====

The command ``print()`` Writes text output to the screen.
It accepts one or more arguments in parentheses - all things that will be printed.
You can print both strings and integer numbers.
You can also provide variables as arguments to ``print()``.

We need ``print`` because typing a variable name in a Python program
does not give you any visible output.

The Python ``print`` function is very versatile and accepts many
combinations of strings, numbers, function calls, and arithmetic
operations separated by commas.

----

Example print statements
------------------------

::

   print('Hello World\n')
   print(3 + 4)
   print(3.4)

   print("""Text that 
   stretches over 
   multiple lines.
   """)

   print('number', 77)

   a = "7"
   print(a * 7)
   print(int(a) * 7)
   print("Hello", end=" ")
   print("World")

----

Format strings
--------------

Variables and strings can be combined, using **f-strings**. f-strings
contain placeholders with variable names and format characters. Here are
some examples:

.. code:: python3
   
   name = 'Roger'
   number = 42
   pi = 3.14159

   print(f'Hello {name}')
   print(f'Result: {number:6d}')
   print(f'{number:06d}')
   print(f'{name:>20} {name:20}')
   print(f'{pi:8.3f})

The winged brackets are placeholders for the parameters in the
``format`` function. Thy consist of two parts ``{a:b}``. Part ``a`` is a
variable name (or expression). The optional part ``b`` contains format
characters. Options include:

============= ====================================
format        description
============= ====================================
``{var}``     insert the variable only.
``{var:xd}``  an integer with x digits.
``{var:<xd}`` a left-formatted integer with x digits.
``{var:0xd}`` a left-formatted integer with x digits filled up with zeroes.
``{:>5}``     a right-aligned string of width 5.
``{:6.2f}``   a float number with 6 digits (2 after the dot).
============= ====================================
