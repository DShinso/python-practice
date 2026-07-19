class Human:
    def speak(self):
        print("Human speaking")


class Robot:
    def speak(self):
        print("Robot speaking")


class Android(Robot, Human):
    pass

android = Android()
android.speak()
print(Android.mro())