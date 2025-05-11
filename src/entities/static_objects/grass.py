from entities.entity import Entity

class Grass(Entity):
    def __init__(self):
        self.name = "Grass"
        self.view = "🌿"
        self.heal = 3