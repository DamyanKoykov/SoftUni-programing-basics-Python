first_couple_range_start = int(input())
second_couple_range_start = int(input())
first_couple_range_end = first_couple_range_start + int(input())
second_couple_range_end = second_couple_range_start + int(input())

for first_couple_current in range(first_couple_range_start, first_couple_range_end + 1):
    for second_couple_current in range(second_couple_range_start, second_couple_range_end + 1):
        if first_couple_current > 1:
            for i in range(2, int(first_couple_current / 2) + 1):
                if (first_couple_current % i) == 0:  # first couple is not prime
                    break
            else:
                if second_couple_current > 1:
                    for i in range(2, int(second_couple_current / 2) + 1):
                        if (second_couple_current % i) == 0:  # second couple is not prime
                            break
                    else:
                        print(f"{first_couple_current}{second_couple_current}")
