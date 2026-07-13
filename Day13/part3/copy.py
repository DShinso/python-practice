robot = {
    "name": "Atlas",
    "battery": "100%"
}

robot2 = robot.copy()

robot2["battery"] = "50%"
print("Original:")
print(robot)
print()
print("copy: ")
print(robot2)