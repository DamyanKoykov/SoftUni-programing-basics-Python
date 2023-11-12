budget_available = float(input())
destination = input()
season = input()
days_needed = int(input())

cost_per_day = 0
if season == "Winter":
    if destination == "Dubai":
        cost_per_day = 45_000
    elif destination == "Sofia":
        cost_per_day = 17_000
    elif destination == "London":
        cost_per_day = 24_000
elif season == "Summer":
    if destination == "Dubai":
        cost_per_day = 40_000
    elif destination == "Sofia":
        cost_per_day = 12_500
    elif destination == "London":
        cost_per_day = 20_250

total_cost = days_needed * cost_per_day

if destination == "Dubai":
    total_cost *= (1 - 0.30)
elif destination == "Sofia":
    total_cost *= (1 + 0.25)

difference = abs(budget_available - total_cost)

if budget_available >= total_cost:
    print(f"The budget for the movie is enough! We have {difference :.2f} leva left!")
else:
    print(f"The director needs {difference :.2f} leva more!")
