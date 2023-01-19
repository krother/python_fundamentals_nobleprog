# NumPy Arrays

### Create a NumPy Array

Install Numpy with:

    python -m pip install numpy

Try the code:

    import numpy as np

    a = np.random.randint(1, 10, size=(7, 7), dtype=np.uint8)
    print(a)

Add the instructions:

    a = a * 10
    print(a)

----

### Making an image

Install the Pillow library:

    python -m pip install pillow

Increase the size of the image to `(200, 200)`.

Add the lines:

    from PIL import Image

    im = Image.fromarray(a)
    im.save('area.png')


### Slicing Numpy Arrays

Slicing NumPy arrays allows you to edit rectangular blocks of data.

Check out the code in [flags.py](flags.py)

#### Hints:

* the slicing contains an interval `from:to` for each dimension
* the smallest `from` value is zero
* the highest `to` value is the size of that dimension plus one
* negative numbers count from the back
* both `from` and `to` can be omitted

----

### Challenge

Draw the flag of a country of your choice.

