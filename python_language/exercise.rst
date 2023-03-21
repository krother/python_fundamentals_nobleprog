Exercise: A first program
=========================

**Let's create a Kingdom Simulator game.**

|image0|

.. card::
   :shadow: lg

   The ruler is planning to build a new enchanted castle.
   Enchanted castles are a complicated matter.
   You are tasked with providing enough resources, coordinating construction work.
   
   Every month, you can build one building:
   
   * a lumber mill (costs nothing and produces 1 unit of wood per month)
   * a quarry (costs 2 wood and produces 1 unit of stone per month)
   * a mage tower (costs 15 stone and 10 wood and produces 1 unit of mana per month)
   * an enchanted castle (costs 100 wood, 100 stone and 100 units of mana)
   
   How many months will the construction work take?

Exercise 1
----------

Here is an **incomplete** Python program:

.. literalinclude:: sim_kingdom.py

Fill in the following lines in the gaps marked by `...`:

.. code:: python3

   quarries += 1
     
   stone = 0

   selected == '3' and wood >= 100 and stone >= 100 and mana >= 100

   print(f"[{counter}] {name}")

   stone += quarries


----

Exercise 2
----------

Execute the program. Play a few rounds and check whether the program works.

----

Exercise 3
----------

The game is not complete yet.

Add the option to build a **mage tower**. It costs 10 wood and 15 stone
and produces 1 mana per turn.

----

Exercise 4
----------

There is a small bug in the program. You might notice it when you solve
the game.

What needs to be done to fix it?

----

Reflection
----------

What language elements or syntax rules of Python have you seen so far?

Collect them in the `Spreadsheet <https://docs.google.com/spreadsheets/d/1Q9s-KTkw8_HvkJZO_hcMXw01m9w9HVGGBaAU8oZ4gsM/edit?usp=sharing>`__

----

License
-------

Castle image by Heindal_Wesnoth from `opengameart.org <https://opengameart.org/content/fantasyart-background>`__ - CC-BY-SA 3.0

.. |image0| image:: castle.png
