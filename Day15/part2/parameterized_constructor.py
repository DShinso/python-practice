class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello my name is", self.name)

robot1 = Robot("Atlas")
robot2 = Robot("Optimus")
robot3 = Robot("Avenger")

robot1.introduce()
robot2.introduce()
robot3.introduce()