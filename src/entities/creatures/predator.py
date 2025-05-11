from creature import Creature

class Predator(Creature):
    def __init__(self):
        super().__init__()
        self.name = "Predator"
        self.view = "🐅"
        self.hp = 13
        self.speed = 3
        self.attack_power = 4

    def make_free_move(self, map):
        # Implement the logic for herbivore free movement
        pass


    def make_hungred_move(self, map):
        # Implement the logic for herbivore movement
        pass


    def attack(self, target):
        pass


    def getting_hungry(self, map):
        self.hp -= 1
        if self.hp <= 0:
            map.die_entity(self)