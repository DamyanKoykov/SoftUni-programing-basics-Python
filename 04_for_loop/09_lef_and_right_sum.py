count_of_couples = int(input())

first_couple_sum = 0
second_couple_sum = 0
for couples in range(count_of_couples * 2):
    numbers = int(input())
    if couples < count_of_couples:
        first_couple_sum += numbers
    else:
        second_couple_sum += numbers

difference = first_couple_sum - second_couple_sum
if first_couple_sum == second_couple_sum:
    print(f"Yes, sum = {first_couple_sum}")
else:
    print(f"No, diff = {abs(difference)}")
