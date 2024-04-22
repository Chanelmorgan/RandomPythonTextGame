import os
from Character import Hero, Enemy 
from Weapon import short_bow, iron_sword 

# Creating the characters for the game 
hero = Hero(name="Hero", health=100) 
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow) 

# Main game loop 
while True: 
    os.system("clear")
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    hero.health_bar.draw()
    enemy.health_bar.draw()


    input()

