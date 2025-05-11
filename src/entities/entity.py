from abc import ABC
from random import randint

class Entity(ABC):
    def __init__(self):
        self.name = None
        self.view = None
        self.x = randint(0, 10)
        self.y = randint(0, 10)
        self.coord = (self.x, self.y)
        

    