type_of_flowers = input()
flowers_quantity = int(input())
budget = int(input())

discount = 1
flowers_price = 0
if type_of_flowers == "Roses":
    flowers_price = 5
    if type_of_flowers == "Roses" and flowers_quantity > 80:
        discount = 1 - 0.10
elif type_of_flowers == "Dahlias":
    flowers_price = 3.80
    if type_of_flowers == "Dahlias" and flowers_quantity > 90:
        discount = 1 - 0.15
elif type_of_flowers == "Tulips":
    flowers_price = 2.80
    if type_of_flowers == "Tulips" and flowers_quantity > 80:
        discount = 1 - 0.15
elif type_of_flowers == "Narcissus":
    flowers_price = 3
    if type_of_flowers == "Narcissus" and flowers_quantity < 120:
        discount = 1 + 0.15
elif type_of_flowers == "Gladiolus":
    flowers_price = 2.50
    if type_of_flowers == "Gladiolus" and flowers_quantity < 80:
        discount = 1 + 0.20

total_cost = (flowers_price * flowers_quantity) * discount
money_difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Hey, you have a great garden with {flowers_quantity} \
{type_of_flowers} and {money_difference :.2f} leva left.")

elif budget < total_cost:
    print(f"Not enough money, you need {money_difference :.2f} leva more.")
