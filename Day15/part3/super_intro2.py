class Robot:
    def __init__(self, name):
        self.name = name
        print("Robot constructor")


class BattleRobot(Robot):
    def __init__(self, name):
        super().__init__(name)
        print("BattleRobot constructor")


robot = BattleRobot("Atlas")
print(robot.name)