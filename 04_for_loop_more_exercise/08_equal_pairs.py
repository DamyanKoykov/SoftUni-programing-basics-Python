import sys

couples_count = int(input())

current_sum = 0
list_of_sums = []
for _ in range(couples_count):
    current_num_one = int(input())
    current_num_two = int(input())
    current_sum = current_num_one + current_num_two
    list_of_sums.append(current_sum)

are_all_sums_equal = False
for sum_index in range(0, couples_count - 1, 2):
    if list_of_sums[sum_index] == list_of_sums[sum_index + 1]:
        are_all_sums_equal = True
    else:
        are_all_sums_equal = False

max_difference = -sys.maxsize
if not are_all_sums_equal:
    for sum_compare_index in range(couples_count - 1):
        difference_current = abs(list_of_sums[sum_compare_index] - list_of_sums[sum_compare_index + 1])
        if difference_current > max_difference:
            max_difference = difference_current

if are_all_sums_equal or couples_count == 1:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={max_difference}")
