# first symbol is  digit range from 1 to n
first_symbol_range_limit = int(input())
# second symbol is digit with same limit as the first one
second_symbol_range_limit = first_symbol_range_limit
# the input shows how much symbol from ASCII starting at 97 "a" get 1 out for the range
third_symbol_range_limit = 97 + int(input())
# fourth symbol is the same principle as third one
fourth_Symbol_range_limit = third_symbol_range_limit
# fifth symbol is digit with same limit but range is 2 to n
fifth_symbol_range_limit = first_symbol_range_limit

for first in range(1, first_symbol_range_limit + 1):
    for second in range(1, second_symbol_range_limit + 1):
        for third in range(97, third_symbol_range_limit):
            for fourth in range(97, fourth_Symbol_range_limit):
                for fifth in range(2, fifth_symbol_range_limit + 1):
                    if fifth > first and fifth > second:
                        print(f"{first}{second}{chr(third)}{chr(fourth)}{fifth}", end=" ")
