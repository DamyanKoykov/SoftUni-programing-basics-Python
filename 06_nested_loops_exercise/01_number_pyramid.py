number = int(input())

current_number = 1
is_it_the_end = False
for row in range(1, number + 1):
    for column in range(1, row + 1):

        if current_number > number:
            is_it_the_end = True
            break
        print(f"{current_number}", end=" ")
        current_number += 1
    if is_it_the_end:
        break
    print()
