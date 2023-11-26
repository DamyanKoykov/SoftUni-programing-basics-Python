one_lev_coins_count = int(input())
two_lev_coins_count = int(input())
five_lev_coins_count = int(input())
total_amount_lev = int(input())

for one_lv_counter in range(one_lev_coins_count + 1):
    for two_lv_counter in range(two_lev_coins_count + 1):
        for five_lv_counter in range(five_lev_coins_count + 1):
            if (one_lv_counter * 1) + (two_lv_counter * 2) + (five_lv_counter * 5) == total_amount_lev:
                print(f"{one_lv_counter} * 1 lv. + {two_lv_counter} * 2 lv. + "
                      f"{five_lv_counter} * 5 lv. = {total_amount_lev} lv.")
