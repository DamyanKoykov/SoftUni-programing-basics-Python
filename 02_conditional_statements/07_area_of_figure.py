import math

type_of_figure = input()

if type_of_figure == "square":
    side_a = float(input())
    area_size = side_a * side_a
elif type_of_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area_size = side_a * side_b
elif type_of_figure == "circle":
    radius = float(input())
    area_size = math.pi * (radius * radius)
elif type_of_figure == "triangle":
    side_a = float(input())
    side_b = float(input())
    area_size = (side_a * side_b) / 2
else:
    area_size = 0
    print("error")

print(f"{area_size:.3f}")
