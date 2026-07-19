class Robot:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health


robot1 = Robot("Atlas", 100)
robot2 = Robot("Optimus", 0)

print(robot1.is_alive())
print(robot2.is_alive())
print(robot1.get_health())
print(robot2.get_health())