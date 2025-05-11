from creature import Creature

class Herbivore(Creature):
    def __init__(self):
        super().__init__()
        self.name = "Herbivore"
        self.view = "🐄"
        self.hp = 17
        self.speed = 2


    def make_free_move(self, map):
        # Implement the logic for herbivore free movement
        pass


    def make_hungred_move(self, map):
        # Implement the logic for herbivore movement
        pass


    def getting_hungry(self, map):
        self.hp -= 1
        if self.hp <= 0:
            map.die_entity(self)

            