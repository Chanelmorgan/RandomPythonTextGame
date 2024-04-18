from Weapon import Weapon

class Character: 

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists

def attack(self, target) -> None:
    target.health -= self.weapon.damage
    target.health = max(target.health, 0)


# Creating a sub class Hero 
class Hero(Character): 
    def __init__(self, name:str, health:int) -> None:
        super().__init__(name=name, health=health)


# Creating a sub class Enemy
class Enemy(Character): 
    def __init__(self, name:str, health:int) -> None:
        super().__init__(name=name, health=health)