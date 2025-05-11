from entities.entity import Entity

class Rock(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Rock"
        self.view = "🗻"