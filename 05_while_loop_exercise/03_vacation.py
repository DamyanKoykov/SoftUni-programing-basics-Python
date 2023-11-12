holiday_price = float(input())
current_money_savings = float(input())

day_counter = 0
spend_counter = 0
spend_or_save = ""
while current_money_savings < holiday_price and spend_counter != 5:
    spend_or_save = input()
    current_amount = float(input())
    day_counter += 1
    if spend_or_save == "save":
        current_money_savings += current_amount
        spend_counter = 0
    if spend_or_save == "spend":
        spend_counter += 1
        if current_amount >= current_money_savings:
            current_money_savings = 0
        else:
            current_money_savings -= current_amount

if spend_counter == 5:
    print(f"You can't save the money.\n{day_counter}")
elif holiday_price <= current_money_savings:
    print(f"You saved the money for {day_counter} days.")
