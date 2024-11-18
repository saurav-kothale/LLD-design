import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)
    

class Charactor(Prototype):
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def __str__(self):
        return f"Character(name={self.name}, level={self.level}, health={self.health})"
    
prototype_character = Charactor("Hero", 1, 100)

character1 = prototype_character.clone()
character1.name = "my_name"
character1.health = 50

character2 = prototype_character.clone()
character2.name = "Mage"
character2.health = 80

print(character1)
print(character2)