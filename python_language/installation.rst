
Installing Python
=================

To use Python, you need the **Python Interpreter** and a **Code Editor**.
A convenient option is `Anaconda <https://store.continuum.io/cshop/anaconda/>`__,
a Python distribution with an editor and many pre-installed packages for scientific applications.
After installing, start the **Anaconda Navigator**:

::

   anaconda-navigator

You will see a startup screen from which you can launch the **Spyder** IDE.

----

Alternatives
------------

-  `Python 3 <https://www.python.org/downloads/>`__ - the standard Python installation
-  **VSCode** - a free multi-purpose editor
-  `PyCharm <https://www.jetbrains.com/pycharm/>`__ - a professional Python development environment capable
   of handling large projects. You won’t need most of the functionality
   for a long time, but it is a well-written editor.
-  **vim** - a console-based text editor for Unix systems. The tool of choice for many system administrators.

----

Installing Libraries
--------------------

Open a terminal. On MacOS and Linux your normal terminal should be fine.
On Windows, the command line within PyCharm is probably the safest way
to get it working fast. Install a few libraries from the command line
with:

::

   pip install pytest
   pip install numpy
   pip install pandas
   pip install seaborn jupyter

There are more Python libraries you might try, but installing them is
not difficult (and a good opportunity to discuss dependency management).
