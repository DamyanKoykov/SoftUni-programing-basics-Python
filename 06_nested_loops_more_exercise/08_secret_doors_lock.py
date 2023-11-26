first_num_limit = int(input())
second_num_limit = int(input())
third_num_limit = int(input())

for first in range(1, first_num_limit + 1):
    for second in range(1, second_num_limit + 1):
        for third in range(1, third_num_limit + 1):
            if first % 2 == 0 and third % 2 == 0:
                if 2 <= second <= 7:
                    if second == 2:
                        print(f"{first} {second} {third}")
                    else:
                        for i in range(2, int(second / 2) + 1):
                            if (second % i) == 0:  # it is not prime
                                break
                        else:
                            print(f"{first} {second} {third}")
