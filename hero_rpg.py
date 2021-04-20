# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


            

        # if hero.health == 10:
        #     print("hero shoots the Goblin with Parasol Gun")

        # else: 
        #     print("the Goblin spurts purple sludge and dies!") 
        # print(f'Hero takes{self.power}damage, hero has{hero.health}health remaining,')

        # if goblin.health != hero.power: 
        # print("Zombie carry on!!")

    # def print_status(self, goblin):
    #     print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))

# class Medic(Character):

#     def Medic_attack(self, enemy, health):
#         Medic.health = self.power
        # print(f'Medic receives {self.power}recup, medic has{Medic.health} at %d,')
    # def attack(self, enemy):
    #     if random.randint(0,100) < 20:
    #         enemy.Health -= (self.health * 2)
    #         print("{Shadow} does double damage({}) to {}.".format(self.name, (self.health * 2), enemy.name ))
    #     else:
    #         enemy.Health -= self.health
    #         print("{} does {} damage to {}.".format(self.name, self.health, enemy.name))


# class Shadow:
#     def __init__(self, health, power, name):
#         self.health = 8
#         self.power = 6
#         self.name = 'Shadow'

#     def attack(self, enemy):
#         if random.randint(0,100) < 20:
#             enemy.Health -= (self.health * 2)
#             print("{Shadow} does double damage({}) to {}.".format(self.name, (self.health * 2), enemy.name ))
#         else:
#             enemy.Health -= self.health
#             print("{} does {} damage to {}.".format(self.name, self.health, enemy.name))

# class Zombie(Character):
#     def Zombie_attack(self, health, name):
#         Zombie.health = self.health
# def main():
# class Shaker(Character):
#     def Shaker_attack(self, health, name):
#         pass


# class Twink(Character):
#     def Twink_attack(self, health, name):
#         Twink.power = self.name 
        
# main ()

def main():
    hero = Hero (10, 5, 'hero') 
    goblin = Goblin (6, 2, 'goblin')
    # Goblin.health = (5, 1)
    # Hero.power = (8, 4)
    # Medic = Medic(5,3)

    # Zombie = Zombie(7,1)
    # Shadow = Shadow(3,2)


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
    


import random
class Character:
    def __init__(self, health, power, name):
        self.health = 10
        self.power = 9
        self.name = 2
    def alive(self):
        if self.name == ['Zombie,' 'Shadow']:
            return True
        elif self.health > 10:
            return True
        else:
            return False  

class Hero(Character):
            
    def Hero_attack(self, goblin, hero, attack):
        Hero = hero
        Goblin = goblin 
        Goblin = attack
        Hero = attack
        # while goblin.health < 0 and hero.health > 0:
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
            Goblin == attack(hero) 
            if hero.health():
                print(f"You {hero.power} caused injury to the Goblin")
                hero.health > goblin.power
                print("The goblin has {goblin} health and {goblin} power.".format(goblin.health, goblin.power))

            # goblin.health -= Hero.power
            # print("You do {} damage to the goblin.".format(hero.health))
        else:
            print("You've been injured by the goblin.".format(hero.health))   
        if goblin.health <= 2:
                print("The goblin is dead.")

        # elif raw_input == "2":
        #     pass
        # elif raw_input == "3":
        #     print("Goodbye.")
            # break
        # else:
        #     print("Invalid input {}".format(raw_input))
        
        
    def print_status(self, hero):
        print("You did {} damage to the goblin.".format(hero.power))
    
            
class Goblin(Character):
    
    def Goblin_attack(self, hero, goblin, attack):
        globin = goblin("Goblin", "Zombie", "Shadow")
        hero.health == attack 
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
            Hero == attack(globin)
        if goblin.health():
            print("You have {hero} health and {hero} power.".format(hero.health, hero.power))
            hero.health <= goblin.power
            print("The Shadow has {goblin} health and {goblin} power.".format(goblin.health, goblin.power))
        
        while globin.health <= 0 and hero.health > 1:
            print("Shadow wants a match, are you game?")
            print("Engage Shadow?") 
            print("Flee Shadow") 
        # if raw_input == "1":
            break
main ()

    