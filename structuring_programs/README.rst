Structuring Code
================

In this session, we will **refactor** the kingdom simulator using
functions and imports.

I go by the definition of refactoring by *Martin Fowler*: **Refactoring
improves the structure of code without changing its functionality.**

We will apply a very basic refactoring workflow:

::

   1. run the tests
   2. edit the code
   3. run the tests

--------------

Exercise 1: Kingdom Simulator 2.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this session, we use a slightly different version of the game.
Please download :download:`sim_kingdom.py <sim_kingdom.py>` .

--------------

Exercise 2: Run the Tests
~~~~~~~~~~~~~~~~~~~~~~~~~

A fundamental rule in refactoring is: **you need automated tests**.

We will use the `pytest <https://pytest.org>`__ library. Please make
sure it is installed:

::

   pip install pytest

Place the following test code in the file `test_sim_kingdom.py`:

.. literalinclude:: test_sim_kingdom.py

Then run the tests with:

::

   pytest test_sim_kingdom.py

You should see a message that the tests fail.

To see the output from ``print`` statements, do:

::

   pytest -s test_sim_kingdom.py

--------------

Exercise 3: Debugging
~~~~~~~~~~~~~~~~~~~~~

The program contains **5 bugs**.

Fix them and run the tests again.

In the end, you should see a message similar to:

::

   ============================= test session starts ==============================
   platform linux -- Python 3.8.10, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
   rootdir: /home/kristian/projects/refactoring_tutorial
   plugins: flake8-1.0.7, Faker-8.9.1, asyncio-0.15.1, cov-2.10.1, dash-1.18.1, anyio-3.5.0
   collected 12 items                                                             

   test_sim_kingdom.py .                                                     [100%]

   ============================== 1 passed in 0.04s ===============================

--------------

Exercise 4: Extract a function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Move the code for printing the resources into a new function
``print_report``. Follow the recipe:

::

   1. Write a function definition: `def print_report(resources):`
   2. Move the print statements of the report into the new function
   3. Add an extra parameter `month` to the function definition.
   4. Add a function call where the code was before
   5. Run the tests

You might write a new test for the function but this is not a best
practice.

--------------

Exercise 5: Extract a module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To make the file smaller, move the newly created function to a new file.
Follow the recipe:

1. create an empty Python file ``report.py``
2. cut and paste the ``print_report()`` function into the new module\`
3. add an import ``from report import print_report``
4. run the tests again

The tests should still pass.

--------------

Exercise 6: Extract Data Structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The code for checking resources and building is quite redundant. We can
simplify it by adding an extra data structure.

Add a data structure for the costs of all buildings:

.. code:: python3

   costs = {
       'lumber mill': {},
       'quarry': [('wood', 2)],
       'mage tower': [('stone', 5), ('crystals', 13)],
       'castle': [('wood', 100), ('stone', 100), ('mana', 100)],
   }

Adjust the ``simulate_month()`` function accordingly to use the
``costs`` structure.

You might want to introduce a helper function ``check_costs()``.

Run the tests again when you are don. They should still passs.

--------------

Exercise 7
~~~~~~~~~~

Execute the code sniplets in the following code.
Make sure you understand what they do:

.. literalinclude:: function_examples.py
