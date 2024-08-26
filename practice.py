numbers = [1,2,3,4,5,6]
cubes = []
for number in numbers:
    cubes.append(number ** 3)
    print(cubes)
def get_cube (num):
    return num ** 3

result = list(map(get_cube, numbers))
print(result)
def get_even(num):
    return num % 2 == 0


