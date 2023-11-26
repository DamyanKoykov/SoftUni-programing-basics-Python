start_of_range = int(input())
end_of_range = int(input())
magic_num = int(input())

did_find_magic_combination = False
combination_counter = 0
for first in range(start_of_range, end_of_range + 1):
    for second in range(start_of_range, end_of_range + 1):
        combination_counter += 1
        if first + second == magic_num:
            did_find_magic_combination = True
            print(f"Combination N:{combination_counter} ({first} + {second} = {magic_num})")
            break
    if did_find_magic_combination:
        break
if not did_find_magic_combination:
    print(f"{combination_counter} combinations - neither equals {magic_num}")
