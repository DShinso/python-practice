robot = {
    "name": "sofia",
    "height": "140cm",
    "language": "python",
    "battery": "90%"
}
print("Robot:", robot)

print("Robot Name: ", robot["name"])
print("Robot Height: ", robot["height"])
print("Number of Items: ", len(robot))
print("Is battery Exists: ", "battery" in robot)
print("Is camera Exists: ", "camera" in robot)