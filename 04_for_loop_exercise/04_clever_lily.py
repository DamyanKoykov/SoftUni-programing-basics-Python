age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toy_amount = 0
money_gift_amount = 0
total_money_gifted = 0
brother_stolen_amount = 0
for birthday_counter in range(age):
    if birthday_counter % 2 == 0:
        toy_amount += 1
    else:
        money_gift_amount += 10
        total_money_gifted += money_gift_amount
        brother_stolen_amount += 1
toy_sell_profit = toy_amount * toy_price
budget = toy_sell_profit + (total_money_gifted - brother_stolen_amount)
difference = budget - washing_machine_price

if budget >= washing_machine_price:
    print(f"Yes! {difference :.2f}")
else:
    print(f"No! {abs(difference) :.2f}")
