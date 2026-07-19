class Robot:
    def introduce(self):
        print("I am a Robot")

class BattleRobot(Robot):
    def introduce(self):
        print("I am a Battle Robot")

class FlyingRobot(Robot):
    def introduce(self):
        print("I am a Flying Robot")

robot1 = Robot()
robot2 = BattleRobot()
robot3 = FlyingRobot()

robot1.introduce()
robot2.introduce()
robot3.introduce()