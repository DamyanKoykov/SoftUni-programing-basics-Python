import sys

how_much_numbers = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for numbers in range(how_much_numbers):
    numbers_to_compare = int(input())
    if numbers_to_compare > max_number:
        max_number = numbers_to_compare
    if numbers_to_compare < min_number:
        min_number = numbers_to_compare

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
