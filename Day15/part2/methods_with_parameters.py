class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self, enemy):
        print(self.name, "attacks", enemy, "with power", self.power)

robot1 = Robot("Atlas", 90)
robot2 = Robot("Optimus", 100)

robot1.attack("Monster")
robot2.attack("Dragon")