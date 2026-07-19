class Robot:
    def __init__(self):
        self.name = "Atlas"

    def introduce(self):
        print("Hello my name is", self.name)

robot1 = Robot()
robot2 = Robot()
robot2.name = "optimus"

robot1.introduce()
robot2.introduce()