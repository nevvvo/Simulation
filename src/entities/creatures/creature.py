from abc import abstractmethod
from entities.entity import Entity

class Creature(Entity):
    def __init__(self):
        super().__init__()
        self.hp = None
        self.speed = None
    @abstractmethod
    def make_free_move(self, map):
        pass


    @abstractmethod
    def make_hungred_move(self, map):
        pass
    

    @abstractmethod
    def getting_hungry(self):
        pass
