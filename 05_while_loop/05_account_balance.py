input_amount = input()

total_amount = 0
while input_amount != "NoMoreMoney":
    current_amount = float(input_amount)
    if current_amount < 0:
        print("Invalid operation!")
        break
    total_amount += current_amount
    print(f"Increase: {current_amount :.2f}")
    input_amount = input()

print(f"Total: {total_amount :.2f}")
