'''
sam attacks paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks paul and deals 19 damage
paul is down to -9 health
Paul has died and sam is victorious
game over
'''
import random
import math

class Warrior:

    def __init__(self, name = "", health=0, attackMax=0, blockMax =0):
        self.name = name
        self.health =health
        self.attackmax =attackMax
        self.blockmax = blockMax

    #attack method
    def attack(self):
        attackAmount = self.attackmax *(random.random() + 0.5) #random takes a value of btwn 0 and 1

        return attackAmount
    #block
    def block(self):
        blockAmount = self.blockmax * (random.random() + 0.5) #random takes a value of btwn 0 and 1

        return blockAmount
    






#capabilities to attack and block random numbers

class Battle:
    #requirements for starting a fight
    def startfight(self, warrior1, warrior2):
        while True:
            #2 attacks for each warrior
            if self.getAttackResult(warrior1,warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2,warrior2) == "Game Over":
                print("Game Over")
                break

    #class method -doesn't need self and not tied to any type of object
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        #focus on attacking and blocking of each player start with warriorA
        warriorAAttackAmount = warriorA.attack()
        warriorBBlock = warriorB.block()

        damagetoWarriorB = math.ceil(warriorAAttackAmount-warriorBBlock)
        warriorB.health = warriorB.health - damagetoWarriorB
        print(f"{warriorA.name} attacks {warriorB.name} and deals {damagetoWarriorB}")

        print(f"{warriorB.name} is down to {warriorB.health} health")

        #death of warrior
        if warriorB.health <= 0:
            print(f"{warriorB.name} has died and {warriorA.name} is victorious")
            return "Game Over"
        else:
            return "Fight Again"
def main():
    #create two warriors
    maximus = Warrior("Maximus", 50, 20, 10)
    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()
    battle.startfight(maximus, galaxon)

main()






    #capability of looping until one dies
    #warriors will get a turn to attack each other
    #fucntion gets two warrirs and one ttacjks the other
    #attacks and blocks be inits