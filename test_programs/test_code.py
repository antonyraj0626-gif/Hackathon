def square(x):
    return x * x


def cube(x):
    return x * x * x

values = [1, 2, 3, 4, 5]
results = []

for v in values:
    results.append(square(v))
print("Squares:", results)

for v in values:
    results.append(cube(v))

print("Cubes:", results)