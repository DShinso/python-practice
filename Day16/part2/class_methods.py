class Robot:

    total_robots = 0
    factory_name = "Shinso Robotics"

    def __init__(self, name):
        self.name = name
        Robot.total_robots += 1

    @classmethod
    def show_total_robots(cls):
        print("Total robots:", cls.total_robots)

    @classmethod
    def show_factory(cls):
        print("Factory:", cls.factory_name)

robot1 = Robot("Atlas")
robot2 = Robot("Optimus")
robot3 = Robot("Titan")

Robot.show_factory()
Robot.show_total_robots()