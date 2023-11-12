amount_of_num = int(input())

p1_amount = 0
p2_amount = 0
p3_amount = 0
p4_amount = 0
p5_amount = 0

for i in range(amount_of_num):
    numbers = int(input())

    if numbers < 200:
        p1_amount += 1
    elif numbers <= 399:
        p2_amount += 1
    elif numbers <= 599:
        p3_amount += 1
    elif numbers <= 799:
        p4_amount += 1
    elif numbers >= 800:
        p5_amount += 1

p1_percent = (100 / amount_of_num) * p1_amount
p2_percent = (100 / amount_of_num) * p2_amount
p3_percent = (100 / amount_of_num) * p3_amount
p4_percent = (100 / amount_of_num) * p4_amount
p5_percent = (100 / amount_of_num) * p5_amount

print(f"{p1_percent :.2f}%")
print(f"{p2_percent :.2f}%")
print(f"{p3_percent :.2f}%")
print(f"{p4_percent :.2f}%")
print(f"{p5_percent :.2f}%")
