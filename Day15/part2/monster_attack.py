class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self, enemy):
        print(self.name, "attacks", enemy)
        self.power = self.power - 10
        print("Power left:", self.power)

robot1 = Robot("Optimus", 90)

robot1.attack("Monster")
print()
robot1.attack("Dragon")
print()
robot1.attack("Boss")