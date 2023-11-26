lucky_number = int(input())

for first_digit in range(1, 9 + 1):
    for second_digit in range(1, 9 + 1):
        for third_digit in range(1, 9 + 1):
            for fourth_digit in range(1, 9 + 1):
                if first_digit + second_digit == third_digit + fourth_digit:
                    if lucky_number % (first_digit + second_digit) == 0:
                        print(f"{first_digit}{second_digit}{third_digit}{fourth_digit} ", end="")