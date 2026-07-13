robot = {
    "name": "Sofia",
    "battery": "90%",
    "camera": "Yes",
    "speed": "5 km/h"
}

remove = robot.pop("camera")

print("Removed: ", remove)
print("Updated Dictionary: ", robot)