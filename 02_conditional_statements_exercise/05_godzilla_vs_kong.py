budget = float(input())
statists_amount = int(input())
clothes_price = float(input())

if statists_amount > 150:
    clothes_price = clothes_price * 0.90

decor = budget * 0.10
clothes_total = statists_amount * clothes_price
total_cost = decor + clothes_total
difference = abs(budget - total_cost)

if budget < total_cost:
    print("Not enough money!")
    print(f"Wingard needs {difference :.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference :.2f} leva left.")
