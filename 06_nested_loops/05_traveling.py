destination = ""
current_budget = 0
current_money_saved = 0

while destination != "End":
    destination = input()
    if destination == "End":
        break
    holiday_cost = float(input())
    while holiday_cost > current_budget:
        current_money_saved = float(input())
        current_budget += current_money_saved
    print(f"Going to {destination}!")
    current_budget = 0
