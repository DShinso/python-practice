class Robot:
    def introduce(self):
        print("I am a Robot")


class FlyingRobot(Robot):
    def introduce(self):
        super().introduce()
        print("I can fly!")


robot = FlyingRobot()
robot.introduce()