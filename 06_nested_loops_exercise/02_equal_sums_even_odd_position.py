number_range_start = int(input())
number_range_end = int(input())

for num_to_check in range(number_range_start, number_range_end + 1):
    sum_even = 0
    sum_odd = 0
    num_to_str = str(num_to_check)
    for position, digit in enumerate(num_to_str):
        if position % 2 == 0:
            sum_even += int(digit)
        elif position % 2 != 0:
            sum_odd += int(digit)
    if sum_even == sum_odd:
        print(num_to_check, end=" ")
