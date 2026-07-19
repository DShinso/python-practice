class Robot:
    def introduce(self):
        print("I am a robot")


class flyingrobot(Robot):
    def attack(self):
        print("Flying......")


robot = flyingrobot()

robot.introduce()
robot.attack()