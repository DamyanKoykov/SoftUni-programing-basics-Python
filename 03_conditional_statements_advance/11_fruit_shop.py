fruit = input()
day_of_week = input()
quantity = float(input())

total_cost = 0

if day_of_week == "Monday" \
        or day_of_week == "Tuesday" \
        or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" \
        or day_of_week == "Friday":
    if fruit == "banana":
        total_cost = 2.50 * quantity
    elif fruit == "apple":
        total_cost = 1.20 * quantity
    elif fruit == "orange":
        total_cost = 0.85 * quantity
    elif fruit == "grapefruit":
        total_cost = 1.45 * quantity
    elif fruit == "kiwi":
        total_cost = 2.70 * quantity
    elif fruit == "pineapple":
        total_cost = 5.5 * quantity
    elif fruit == "grapes":
        total_cost = 3.85 * quantity


elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        total_cost = 2.70 * quantity
    elif fruit == "apple":
        total_cost = 1.25 * quantity
    elif fruit == "orange":
        total_cost = 0.90 * quantity
    elif fruit == "grapefruit":
        total_cost = 1.60 * quantity
    elif fruit == "kiwi":
        total_cost = 3 * quantity
    elif fruit == "pineapple":
        total_cost = 5.60 * quantity
    elif fruit == "grapes":
        total_cost = 4.20 * quantity

if total_cost != 0:
    print(f"{total_cost :.2f}")
else:
    print("error")
