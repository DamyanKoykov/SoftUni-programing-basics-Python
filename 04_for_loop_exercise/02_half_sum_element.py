import sys

amount_of_num = int(input())

max_num = -sys.maxsize
sum_of_num = 0
for i in range(amount_of_num):
    num_to_add = int(input())
    sum_of_num += num_to_add
    if num_to_add > max_num:
        max_num = num_to_add

check = max_num - (sum_of_num - max_num)
if check == 0:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(check)}")
