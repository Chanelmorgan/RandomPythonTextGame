# ------------ imports ------------
import os
from Character import Hero, Enemy 
from Weapon import short_bow, iron_sword 

def display_menu():
    print("1. Attack")
    print("2. End Game") 


def check_battle_status(hero, enemy):
    if hero.health <= 0:
        print("Game Over! Enemy wins!")
        return True
    elif enemy.health <= 0:
        print("Congratulations! Hero wins!")
        return True
    return False

# ------------ object creation ------------
hero = Hero(name="Hero", health=100) 
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow) 

# ------------ Main game loop ------------ 
while True: 
    os.system("clear")
    print("=== Battle Menu ===")
    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        hero.attack(enemy)
        enemy.attack(hero)
    elif choice == "2":
        print("Ending the game...")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")

    print(f"\nHealth of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    hero.health_bar.draw()
    enemy.health_bar.draw()

    if check_battle_status(hero, enemy):
        break

    input("Press Enter to continue...")

