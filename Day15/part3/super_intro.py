class Robot:
    def __init__(self, name):
        self.name = name
        print("Robot constructor")


class BattleRobot(Robot):
    pass


robot = BattleRobot("Atlas")

print(robot.name)