third_symbol_limit = int(input())
fourth_symbol_limit = int(input())
pass_generator_limit = int(input())

first_and_sxt_symbol_ord = 35  # must stay between 35 and 55 ASCII
second_and_fifth_symbol_ord = 64  # must stay between 64 and 96 ASCII
third_symbol_current = 1
fourth_symbol_current = 1
limiter = False

while not limiter:
    print(f"{chr(first_and_sxt_symbol_ord)}{second_and_fifth_symbol_ord}{third_symbol_current}/"
          f"{fourth_symbol_current}{chr(second_and_fifth_symbol_ord)}{chr(first_and_sxt_symbol_ord)}|")
    first_and_sxt_symbol_ord += 1
