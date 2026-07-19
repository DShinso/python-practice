class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self, enemy):
        print(self.name, "attacks", enemy)

    def upgrade(self):
        self.power = self.power + 10
        print(self.name, "Upgraded!")
        print("New power:", self.power)

robot1 = Robot("Optimus", 90)

robot1.upgrade()
robot1.upgrade()
robot1.upgrade()