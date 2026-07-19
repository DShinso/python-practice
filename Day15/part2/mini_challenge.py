class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello my name is", self.name)

robot1 = Robot("Atlas")
robot2 = Robot("Optimus")
robot3 = Robot("Avenger")

print(robot1.name)
print(robot2.name)
print(robot3.name)

robot3.name = "Titan"

robot3.introduce()