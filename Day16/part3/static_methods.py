class Battery:

    @staticmethod
    def is_low(level):
        return level < 20

    @staticmethod
    def charging_time(current, maximum):
        return maximum - current

print(Battery.is_low(10))
print(Battery.is_low(70))

print()

print(Battery.charging_time(40, 100))
print(Battery.charging_time(90, 100))