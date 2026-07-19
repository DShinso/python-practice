class Robot:

    total_robots = 0

    def __init__(self, name, power):
        self.name = name
        self.power = power

        Robot.total_robots += 1

    def introduce(self):
        print("Name:", self.name)
        print("Power:", self.power)

robot1 = Robot("Atlas", 90)
robot2 = Robot("Optimus", 100)
robot3 = Robot("Titan", 80)

robot1.introduce()
print()

robot2.introduce()
print()

robot3.introduce()

print()
print("Total Robots:", Robot.total_robots)