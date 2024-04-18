from Character import Character 

# Creating the characters for the game 
hero = Character(name="Hero", health=100, damage=5) 
enemy = Character(name="Enemy", health=100, damage=3) 

# Main game loop 
while True: 
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()

