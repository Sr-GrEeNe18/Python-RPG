# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

def main():
    hero = Hero(10,5) 
    goblin = Goblin (6,2)
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while goblin.health > 0 and hero.health > 0:
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin.health -= hero.power
            print("You do {} damage to the goblin.".format(hero.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin is dead.")
            if hero.health <= 0:
                print("You are dead.")

class Character:
    def __init__(self, health, power):
        self.health = 10
        self.power = 5
        
    def alive(self):
        if self.health > 0:
            return True


class Hero(Character):
            
    def Hero_attack(self, enemy):
        if enemy.health <= 0:
            print("The goblin is dead.")     
            
    def print_status(self, hero):
        print("You do {} damage to the goblin.".format(hero.power))
    
            
class Goblin(Character):
    
    def Goblin_attack(self, hero):
        hero.health -= self.power
        print(f'Hero takes{self.power}damage, hero has{hero.health}health remaining,')

    def print_status(self, goblin):
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))

# def main():

    
main()
    