import random

football_teams = ["portugal", "France", "Spain", "England"]

print("Random team is " + random.choice(football_teams))

random.shuffle(football_teams)
print("Shuffled list: ", football_teams)