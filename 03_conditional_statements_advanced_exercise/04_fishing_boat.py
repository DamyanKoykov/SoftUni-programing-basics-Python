budget = int(input())
season = input()
fisherman_quantity = int(input())

rent = 0
discount = 1
extra_discount = 1

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if fisherman_quantity <= 6:
    discount = 1 - 0.10
elif fisherman_quantity <= 11:
    discount = 1 - 0.15
elif fisherman_quantity >= 12:
    discount = 1 - 0.25

if fisherman_quantity % 2 == 0 and season != "Autumn":
    extra_discount = 1 - 0.05

total_cost = (rent * discount) * extra_discount
difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Yes! You have {difference :.2f} leva left.")
else:
    print(f"Not enough money! You need {difference :.2f} leva.")
