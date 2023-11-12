number = int(input())

solutions_cunt = 0
for num1 in range(0, number + 1):
    for num2 in range(0, number + 1):
        for num3 in range(0, number + 1):
            if num1 + num2 + num3 == number:
                solutions_cunt += 1

print(solutions_cunt)
