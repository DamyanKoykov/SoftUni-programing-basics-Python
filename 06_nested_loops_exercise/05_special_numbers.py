num = int(input())

is_it_special = "False"
for num_to_check in range(1111, 9999 + 1):
    for _, current_digit in enumerate(str(num_to_check)):
        if int(current_digit) == 0 or num % int(current_digit) != 0:
            is_it_special = False
            break
        else:
            is_it_special = True
    if is_it_special:
        print(num_to_check, end=" ")
