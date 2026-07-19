class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, enemy):
        print(self.name, "attacks", enemy.name)

        enemy.health -= 20

        print(enemy.name, "Health:", enemy.health)

        if enemy.health <= 0:
            print(enemy.name, "is dead")

robot1 = Robot("Atlas", 100)
robot2 = Robot("Optimus", 100)

robot1.attack(robot2)
print()
robot1.attack(robot2)
print()
robot1.attack(robot2)
print()
robot1.attack(robot2)
print()
robot1.attack(robot2)