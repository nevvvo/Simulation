from entities.entity import Entity

class Tree(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Tree"
        self.view = "🌳"