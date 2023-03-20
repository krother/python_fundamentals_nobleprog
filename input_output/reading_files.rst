Reading text files
==================

Open a file for reading
-----------------------

Text files can be accessed using the ``open()`` function. ``open()``
gives you a *file object* that you can use in a ``for`` loop. The loop
processes the contents of the file line by line:

.. code:: python3
   
   f = open('my_file.txt')
   for line in f:
       print(line)

Alternatively, you can write both commands in one line:

.. code:: python3
   
   for line in open('my_file.txt'):
       print(line)

----

Read an entire file to a string variable
----------------------------------------

You can read the entire content of a file to a single string:

.. code:: python3
   
   f = open('my_file.txt')
   text = f.read()
   f.close()

Closing files in Python is not mandatory but good practice. If you open
too many files at the same time this can be a problem.

----

File and directory names
------------------------

When opening files, you often need to specify a directory name as well.
You can use both full or relative directory names. A full file name
contains the absolute path from the root directory, e.g.:

::
   
   /home/kristian/Desktop/myfile.txt

or on Windows

::

   C:/Python3/python.exe

A relative path starts from the current working directory,
often the directory in which your program is started:

::

   data/my_file.txt

or go one directory level up, then move into the folder below:

::

   ../data/my_file.txt

----

Slashes versus Backslashes
--------------------------

On Windows, getting directory names right is a bit cumbersome, because
the directory names easily become long easily. Note that you can use
forward slashed to separate between directories. If you use the
backslash ``\``, you need to write a double backslash ``\\`` (because
``\`` is also used for escape sequences like ``\n`` and ``\t``).

.. code:: python3
   
   f = open('..\\my_file.txt')
   f = open('C:\\Python\\my_file.txt')

----

Reading files with a Context Manager
------------------------------------

The modern way to open files in Python is using a **Context Manager** (a
code block started by ``with``). The ``with`` statement takes care of
closing the file automatically:

.. code:: python3
   
   with open('my_file.txt') as f:
       text = f.read()
