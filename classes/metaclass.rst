Metaclasses
===========

Metaclasses change the objects creation mechanics in Python.
Whenever a Python class is called, it calls the ``__new__()`` method of the metaclass.
By default, ``__new__()`` does the following:

1. create an instance of the class
2. calls its ``__init__()`` method
3. returns the instance

You could write a new metaclass that does something else instead of calling ``__init__()`` .
Examples when a this mechanism is used are:

-  writing an ORM like **Django models** or **SQLAlchemy**
-  hijacking internal Python logic (e.g. like **pytest** does)
-  emulating JavaScript-like objects (the Prototype pattern)

Throughout 20 years of Python programming, I have not come across a single situation where writing a metaclass was necessary.
But it helps to understand Python on a deeper level.

Here is an example:

.. code:: python3
    
   class CrazyMonkeyPack(type):
       """a new metaclass that implements object creation logic"""

       def __new__(mcs, name, bases, dict):
           cls = type.__new__(mcs, name, bases, dict)

           def wrapper(*args):
               instance = []
               for i in range(1, args[0]+1):
                   monkey = cls(f'monkey #{i}')  # calls __init__
                   monkey.state = 'crazy'  # monkey-patches the state attribute
                   instance.append(monkey)
               return instance

           return wrapper


   class CrazyMonkeys(metaclass=CrazyMonkeyPack):
       """A self-expanding horde of monkeys"""
       def __init__(self, name):
           self.name = name

       def __repr__(self):
           return f"<{self.name} ({self.state})>"


   monkeys = CrazyMonkeys(3)  # calls __new__
   print(monkeys)             # see what happens!


.. warning::
    
   Don’t try using metaclasses at work, unless

   -  you have excluded all alternatives
   -  you really know what you are doing
   -  you have talked to a developer more experienced than you
