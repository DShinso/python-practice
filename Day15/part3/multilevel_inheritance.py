class Animal:
    def Speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def Bark(self):
        print("Woof!")

class PoliceDog(Dog):
    def Catch(self):
        print("Criminal caught!")

robot1 = PoliceDog()
robot1.Speak()
robot1.Bark()
robot1.Catch()