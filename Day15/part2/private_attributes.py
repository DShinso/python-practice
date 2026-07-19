class Robot:

    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def show_health(self):
        print("Health:", self.__health)


robot = Robot("Atlas", 100)

print(robot.name)

robot.show_health()