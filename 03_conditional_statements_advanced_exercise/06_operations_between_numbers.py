n1 = int(input())
n2 = int(input())
operator = input()

odd_or_even = ""
result = 0
if n2 == 0 and (operator == "/" or operator == "%"):
    print(f"Cannot divide {n1} by zero")

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = n1 + n2
        if result % 2 == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"

    elif operator == "-":
        result = n1 - n2
        if result % 2 == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"

    elif operator == "*":
        result = n1 * n2
        if result % 2 == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
    print(f"{n1} {operator} {n2} = {result} - {odd_or_even}")

elif operator == "/" and n2 != 0:
    result = n1 / n2
    print(f"{n1} {operator} {n2} = {result :.2f}")
elif operator == "%" and n2 != 0:
    result = n1 % n2
    print(f"{n1} {operator} {n2} = {result}")
