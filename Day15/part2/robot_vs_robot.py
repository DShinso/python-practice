class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self, enemy):
        print(self.name, "attacks", enemy.name)

        enemy.power -= 10

        print(enemy.name, "Power:", enemy.power)

robot1 = Robot("Atlas", 90)
robot2 = Robot("Optimus", 100)

robot1.attack(robot2)
print()
robot1.attack(robot2)
print()
robot1.attack(robot2)
print()

robot2.attack(robot1)
print()
robot2.attack(robot1)
print()
robot2.attack(robot1)