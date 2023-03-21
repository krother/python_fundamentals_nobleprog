Writing text files
==================

Open a file for writing
-----------------------

Writing text to files is very similar to reading. One main difference is
that you need to add the ``'w'`` parameter for *writing*.

.. code:: python3

   with open('my_file', 'w') as f:
       f.write('line of text\n')


The ``with`` statement is called a **Context Manager**.
It takes care of closing the file automatically.

.. note::

   When writing data, Python *buffers* the data and writes it to the disk
   with a delay. The writing occurs after the file has been closed, when
   Python ends or when the buffer runs full.
   The ``with`` block makes sure the data gets written immediately.

----

Write a list of strings
-----------------------

If your data is a list of strings, it can be written to a file in one
line of code. You only need to take care of adding line breaks at the
end of each line:

.. code:: python3

   lines = ['first line\n', 'second line\n']
   open('my_file.txt','w').writelines(lines)

----

Write a table to a text file
----------------------------

A straightforward pattern to write multiple columns to a file uses a
``for`` loop to create lines with separators and newline characters:

.. code:: python3

   names = ['Emily', 'Bob', 'Charlie']
   ages = [23, 45, 67]

   with open('my_file.txt', 'w') as f:
      for name, age in zip(names, ages):
          line = "{};{}\n".format(name, age)
          f.write(line)

Like with reading, the ``csv`` and ``pandas`` offer more sophisticated
ways to write tables.

----

Append to a file
----------------

It is possible to append text to an existing file, too.

.. code:: python3

   with open('my_file.txt','a') as f:
       f.write('line appended at the end\n')
