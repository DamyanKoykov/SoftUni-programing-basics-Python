people_count = int(input())
season = input()

cost_per_person = 0
if people_count <= 5:
    if season == "spring":
        cost_per_person = 50
    elif season == "summer":
        cost_per_person = 48.50
    elif season == "autumn":
        cost_per_person = 60
    elif season == "winter":
        cost_per_person = 86

elif people_count > 5:
    if season == "spring":
        cost_per_person = 48
    elif season == "summer":
        cost_per_person = 45
    elif season == "autumn":
        cost_per_person = 49.5
    elif season == "winter":
        cost_per_person = 85

total_cost = cost_per_person * people_count

if season == "summer":  # summer discount 15%
    total_cost *= (1 - 0.15)
elif season == "winter":  # winter is 8% more expensive
    total_cost *= (1 + 0.08)

print(f"{total_cost :.2f} leva.")
