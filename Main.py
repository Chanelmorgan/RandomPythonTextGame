# ------------ imports ------------
import os
from Character import Hero, Enemy 
from Weapon import short_bow, iron_sword, fists 

def display_menu(first_round):
    if first_round:
        hero.health_bar.draw()
        enemy.health_bar.draw() 
        print("\n=== Battle Menu ===")
        print("1. Attack")
        print("2. End Game")
    else:
        print("=== Battle Menu ===")
        print("1. Attack")
        print("2. Change Weapon")
        print("3. End Game")



def check_battle_status(hero, enemy):
    if hero.health <= 0:
        print("Game Over! Enemy wins!")
        return True
    elif enemy.health <= 0:
        print("Congratulations! Hero wins!")
        return True
    return False

def change_weapon(hero):
    print("\n=== Weapons Menu ===")
    print("Available Weapons:")
    print("1. Iron Sword")
    print("2. Short Bow")
    print("3. Fists")
    choice = input("Choose weapon (1-3): ")
    if choice == "1":
        hero.equip(iron_sword)
        print(f"{hero.name} equipped {iron_sword.name}!")
    elif choice == "2":
        hero.equip(short_bow)
        print(f"{hero.name} equipped {short_bow.name}!")
    elif choice == "3":
        hero.equip(fists)
        print(f"{hero.name} equipped {fists.name}!")
    else:
        print("Invalid choice! Please enter a number between 1 and 3.")


# ------------ object creation ------------
hero = Hero(name="Hero", health=100) 
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=short_bow) 

# ------------ Main game loop ------------ 
first_round = True 
while True: 
  
    os.system("clear")
    print("=== Welcome To The Game ===")
    display_menu(first_round)

    


    choice = input("Enter your choice: ")
    if choice == "1":
        hero.attack(enemy)
        enemy.attack(hero)
        first_round = False
    elif choice == "2" and not first_round:
        change_weapon(hero) 
    elif choice == "3":
        print("Ending the game...")
        print("=== Game Over ===")
        break
    else:
        print("Invalid choice! Please enter a valid option.")


    print(f"\nHealth of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    hero.health_bar.draw()
    enemy.health_bar.draw() 


    if check_battle_status(hero, enemy):
        break

    input("Press Enter to continue...")
   

