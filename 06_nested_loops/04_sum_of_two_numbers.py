starting_point_number = int(input())
end_point_number = int(input())
magic_number = int(input())

counter1 = 0
counter2 = 0
combination_counter = 0
combination_is_found = False
for counter1 in range(starting_point_number, end_point_number + 1):
    for counter2 in range(starting_point_number, end_point_number + 1):
        combination_counter += 1
        if counter1 + counter2 == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{combination_counter} ({counter1} + {counter2} = {magic_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")