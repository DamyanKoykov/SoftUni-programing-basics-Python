size = int(input())

vertical_list = []
horizontal_list = []

current_row = 0
for current_row in range(1, size + 1):
    if current_row == 1 or current_row == size:
        print("+ " + ("- " * (size - 2) + "+"))
    else:
        print("| " + ("- " * (size - 2) + "|"))
