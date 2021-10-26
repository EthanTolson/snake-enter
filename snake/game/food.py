import random as r
from game import constants as c
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here
class Food(Actor):
    def __init__(self):
        self._points = None
        super().__init__()
        super().set_text("@")
        self.reset()

    def reset(self):
        super().set_position(Point(r.randint(1,c.MAX_X - 2), \
            r.randint(1,c.MAX_Y - 2)))
        self._points = r.randint(1,5)

    def get_points(self):
        return self._points