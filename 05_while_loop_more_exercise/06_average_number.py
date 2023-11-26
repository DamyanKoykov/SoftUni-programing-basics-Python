how_much_numbers = int(input())

total_sum = 0
for counter in range(1, how_much_numbers + 1):
    current_num = int(input())
    total_sum += current_num

average = total_sum / how_much_numbers
print(f"{average :.2f}")
