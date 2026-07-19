class Robot:
    def introduce(self):
        print("I am a robot")


class BattleRobot(Robot):
    def attack(self):
        print("Laser Attack!")



robot = BattleRobot()

robot.introduce()
robot.attack()