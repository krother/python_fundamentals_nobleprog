"""
Here we manage the player-controlled snake
"""

UP, DOWN, LEFT, RIGHT = range(1, 5)


class Snake:
    """A snake with a tail that grows"""

    def __init__(self, xstart, ystart):
        self.head = xstart, ystart
        self.tail = []
        self.direction = RIGHT

    def forward(self):
        """Moves the snake one step ahead"""
        x, y = self.head
        if self.direction == RIGHT:
            self.head = x + 1, y
        elif self.direction == UP:
            self.head = x, y - 1
        elif self.direction == DOWN:
            self.head = x, y + 1
        else:
            self.head = x - 1, y

    def grow(self):
        ...

    def eat(self, playground):
        """Eats food at the position of the head, if any"""
        if playground.food == self.head:
            self.grow()
            playground.food = None

    def check_collision(self, playground):
        """Returns True if the head hits an obstacle or the tail"""
        return (
            self.head in playground.walls # wall collisions
        )
        