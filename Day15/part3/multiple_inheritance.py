class Camera:
    def take_photo(self):
        print("Photo taken!")

class Speaker:
    def play_music(self):
        print("Playing music........")

class Smartphone(Camera, Speaker):
    pass

phone = Smartphone()

phone.take_photo()
phone.play_music()