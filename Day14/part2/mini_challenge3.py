python = {"Variables", "Loops", "Functions"}

ai = {"Functions", "NumPy", "Loops", "Pandas"}

print("Union:")
union = python.union(ai)
print(union)
print()

print("Intersection:")
intersection = python.intersection(ai)
print(intersection)
print()

print("Python only:")
python_only = python - ai
print(python_only)
print()

print("AI only:")
ai_only = ai - python
print(ai_only)
print()

print("Symmetric:")
symmetric = python.symmetric_difference(ai)
print(symmetric)
print()