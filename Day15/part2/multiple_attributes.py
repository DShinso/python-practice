class Robot:
    def __init__(self, name, color, power):
        self.name = name
        self.color = color
        self.power = power

    def introduce(self):
        print("Name :", self.name)
        print("Color:", self.color)
        print("Power:", self.power)

robot1 = Robot("Atlas", "Blue", 90)
robot2 = Robot("Optimus", "Red", 100)
robot3 = Robot("Titan", "Black", 95)

robot1.introduce()
print("---------------")
robot2.introduce()
print("---------------")
robot3.introduce()