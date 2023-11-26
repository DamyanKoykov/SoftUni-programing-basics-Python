budget_available = float(input())
category_ticket = input()
people_count = int(input())

budget_left = budget_available
if 1 <= people_count <= 4:
    budget_left *= (1 - 0.75)
elif 4 < people_count <= 9:
    budget_left *= (1 - 0.60)
elif 9 < people_count <= 24:
    budget_left *= (1 - 0.50)
elif 24 < people_count <= 49:
    budget_left *= (1 - 0.40)
elif 49 < people_count:
    budget_left *= (1 - 0.25)

vip_ticket_price = 499.99
normal_ticket_price = 249.99
total_price = 0
if category_ticket == "VIP":
    total_price = vip_ticket_price * people_count
elif category_ticket == "Normal":
    total_price = normal_ticket_price * people_count

difference = abs(budget_left - total_price)
if budget_left >= total_price:
    print(f"Yes! You have {difference :.2f} leva left.")
else:
    print(f"Not enough money! You need {difference :.2f} leva.")
