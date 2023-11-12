first_d_first_num_k = int(input())
second_d_first_num_l = int(input())
first_d_second_num_m = int(input())
second_d_second_num_n = int(input())

substitute_counter = 0
enough_substitutes = False
for k in range(first_d_first_num_k, 8 + 1):
    for lsd in range(9, second_d_first_num_l - 1, -2):
        for m in range(first_d_second_num_m, 8 + 1):
            for n in range(9, second_d_second_num_n - 1, -1):
                if str(k) + str(lsd) == str(m) + str(n):
                    print("Cannot change the same player.")
                    continue
                if k % 2 == 0 and m % 2 == 0:
                    if lsd % 2 != 0 and n % 2 != 0:
                        substitute_counter += 1
                        print(f"{k}{lsd} - {m}{n}")
                if substitute_counter == 6:
                    enough_substitutes = True
                    break
            if enough_substitutes:
                break
        if enough_substitutes:
            break
    if enough_substitutes:
        break
