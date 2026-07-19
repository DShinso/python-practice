class Robot:

    factory_name = "Shinso Robotics"
    total_robots = 0

    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level

        Robot.total_robots += 1

    def introduce(self):
        print("Robot:", self.name)
        print("Battery:", self.battery_level, "%")
        Robot.battery_status(self.battery_level)

    @staticmethod
    def battery_status(battery_level):
        if battery_level < 10:
            print("Critical Stage!")
        elif battery_level < 20:
            print("Battery Low")
        else:
            print("OK")

    @classmethod
    def show_factory(cls):
        print("Robot:", cls.factory_name)

    @classmethod
    def show_robots(cls):
        print("Robot:", cls.total_robots)

robot1 = Robot("Atlas", 75)
robot2 = Robot("Optimus", 15)
robot3 = Robot("Titan", 5)

robot1.introduce()
print()
robot2.introduce()
print()
robot3.introduce()
print()

print("Factory:", Robot.factory_name)
print("Robot:", Robot.total_robots)

