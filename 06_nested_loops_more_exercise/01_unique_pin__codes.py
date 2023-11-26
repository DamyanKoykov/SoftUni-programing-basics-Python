first_num_limit = int(input())
second_num_limit = int(input())
third_num_limit = int(input())

for firs_num in range(1, first_num_limit + 1):
    for second_num in range(1, second_num_limit + 1):
        for third_num in range(1, third_num_limit + 1):
            if firs_num % 2 == 0:
                if third_num % 2 == 0:
                    if second_num > 1:
                        # Iterate from 2 to n / 2
                        for i in range(2, int(second_num / 2) + 1):
                            # If num is divisible by any number between
                            # 2 and n / 2, it is not prime
                            if (second_num % i) == 0:
                                break  # it is not prime
                        else:  # it is prime
                            print(f"{firs_num} {second_num} {third_num}")
