first_letter = input()  # 1
second_letter = input()  # 2
third_letter = input()  # 3, also if this letter is in the combination don`t print

combination_counter = 0
for first_letter_ord in range(ord(first_letter), ord(second_letter) + 1):
    if first_letter_ord == ord(third_letter):
        continue
    for second_letter_ord in range(ord(first_letter), ord(second_letter) + 1):
        if second_letter_ord == ord(third_letter):
            continue
        for third_letter_ord in range(ord(first_letter), ord(second_letter) + 1):
            if third_letter_ord == ord(third_letter):
                continue
            else:
                first = chr(first_letter_ord)
                second = chr(second_letter_ord)
                third = chr(third_letter_ord)
                print(f"{first}{second}{third}", end=" ")
                combination_counter += 1
print(combination_counter)
