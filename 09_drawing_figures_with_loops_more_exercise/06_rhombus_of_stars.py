size = int(input())

for row in range(1, size + 1):
    print((" " * (size - row)) + "*" + (" *" * (row - 1)))

for bottom_row in range(size - 1, 1 - 1, -1):
    print((" " * (size - bottom_row)) + "*" + (" *" * (bottom_row - 1)))
