import sys

num_count = int(input())

odd_num_counter = 0
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_num_counter = 0
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
for num_index in range(1, num_count + 1):
    current_num = float(input())
    if num_index % 2 != 0:
        odd_sum += current_num
        odd_num_counter += 1
        if current_num < odd_min:
            odd_min = current_num
        if current_num > odd_max:
            odd_max = current_num
    elif num_index % 2 == 0:
        even_sum += current_num
        even_num_counter += 1
        if current_num < even_min:
            even_min = current_num
        if current_num > even_max:
            even_max = current_num

if even_num_counter == 0:
    even_max = "No"
    even_min = "No"
if odd_num_counter == 0:
    odd_max = "No"
    odd_min = "No"

print(f"OddSum={odd_sum :.2f},")
if odd_num_counter != 0:
    print(f"OddMin={odd_min :.2f},")
    print(f"OddMax={odd_max :.2f},")
else:
    print("OddMin=No,")
    print("OddMax=No,")
print(f"EvenSum={even_sum :.2f},")
if even_num_counter != 0:
    print(f"EvenMin={even_min :.2f},")
    print(f"EvenMax={even_max :.2f}")
else:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
