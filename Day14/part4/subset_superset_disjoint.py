frontend = {"HTML", "CSS"}
fullstack = {"HTML", "CSS", "JavaScript", "Python"}

print(frontend.issubset(fullstack))
print(fullstack.issuperset(frontend))
print(frontend.isdisjoint(fullstack))