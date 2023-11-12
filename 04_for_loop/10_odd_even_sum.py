amount_of_numbers = int(input())

even_numbers_sum = 0
odd_numbers_sum = 0

for numbers in range(amount_of_numbers):
    current_number = int(input())
    if numbers % 2 == 0:
        even_numbers_sum += current_number
    elif not numbers % 2 == 0:
        odd_numbers_sum += current_number

difference = even_numbers_sum - odd_numbers_sum

if difference == 0:
    print("Yes")
    print(f"Sum = {even_numbers_sum}")
else:
    print("No")
    print(f"Diff = {abs(difference)}")
