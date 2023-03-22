Automated Tests
===============

In this session, we will use **automated tests** for the kingdom simulator
in order to improve its structure.

Run the Tests
-------------

We will use the `pytest <https://pytest.org>`__ library.
Please make sure it is installed:

::

   pip install pytest

Place the following test code in the file `test_sim_kingdom.py`:

.. literalinclude:: test_sim_kingdom.py

Then run the tests with:

::

   pytest test_sim_kingdom.py

You should see a message that the tests fail.

----

Code with functions
-------------------

For the tests to work, we will need a modified version of the code:

* there needs to be a function ``simulate_month()`` that the test will call.
* we cannot use keyboard input (or had to use )

Please download :download:`sim_kingdom.py <sim_kingdom.py>` and run the tests again.

--------------

Debugging
---------

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

Extract a function
------------------

With the test in place, you can comfortable restruture the code.
Move the code for printing the resources into a new function
``print_report``. Follow the recipe:

::

   1. Write a function definition: `def print_report(resources):`
   2. Move the print statements of the report into the new function
   3. Add an extra parameter `month` to the function definition.
   4. Add a function call where the code was before
   5. Run the tests

--------------

Extract a module
----------------

To make the file smaller, move the newly created function to a new file.
Follow the recipe:

1. create an empty Python file ``report.py``
2. cut and paste the ``print_report()`` function into the new module\`
3. add an import ``from report import print_report``
4. run the tests again

The tests should still pass.

--------------

Extract Data Structures
-----------------------

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

