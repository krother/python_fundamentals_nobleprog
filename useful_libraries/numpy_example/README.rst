NumPy Arrays
============

Create a NumPy Array
~~~~~~~~~~~~~~~~~~~~

Install Numpy and Pillow with:

.. code:: python3

   python -m pip install numpy pillow

You might also try the Jupyter notebook

::

   python -m pip install jupyter
   jupyter notebook

Try the code:

.. code:: python3

   import numpy as np

   a = np.random.randint(1, 10, size=(7, 7), dtype=np.uint8)
   print(a)

Add the instructions:

.. code:: python3

   a = a * 10
   print(a)

--------------

Create an image
~~~~~~~~~~~~~~~

Increase the size of the array to ``(200, 200)``.

Add the lines:

.. code:: python3

   from PIL import Image

   im = Image.fromarray(a)
   im.save('area.png')

----

Slicing Numpy Arrays
~~~~~~~~~~~~~~~~~~~~

Slicing NumPy arrays allows you to edit rectangular blocks of data.

Check out the code in `flags.py <flags.py>`__

Hints:
^^^^^^

-  the slicing contains an interval ``from:to`` for each dimension
-  the smallest ``from`` value is zero
-  the highest ``to`` value is the size of that dimension plus one
-  negative numbers count from the back
-  both ``from`` and ``to`` can be omitted

--------------

Challenge
~~~~~~~~~

Draw the flag of a country of your choice.
