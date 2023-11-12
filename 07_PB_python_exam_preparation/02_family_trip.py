current_budget = float(input())
nights_booked = int(input())
price_per_night = float(input())
percent_for_expenses = int(input())

if nights_booked > 7:
    price_per_night *= 0.95  # 5% discount for over 7 nights stay

hotel_cost = nights_booked * price_per_night
expense_cost = current_budget * (percent_for_expenses / 100)
total_cost = hotel_cost + expense_cost

difference = abs(current_budget - total_cost)

if current_budget >= total_cost:
    print(f"Ivanovi will be left with {difference :.2f} leva after vacation.")
else:
    print(f"{difference :.2f} leva needed.")
