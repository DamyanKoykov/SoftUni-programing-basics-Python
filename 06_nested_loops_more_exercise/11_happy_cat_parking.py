days_count = int(input())
hours_count = int(input())

parking_price = 0
total_cost = 0
current_day_cost = 0

for current_day in range(1, days_count + 1):
    for current_hour in range(1, hours_count + 1):

        if current_day % 2 == 0 and current_hour % 2 != 0:
            parking_price = 2.50
        elif current_day % 2 != 0 and current_hour % 2 == 0:
            parking_price = 1.25
        else:
            parking_price = 1
        current_day_cost += parking_price
    total_cost += current_day_cost
    print(f"Day: {current_day} - {current_day_cost :.2f} leva")
    current_day_cost = 0

print(f"Total: {total_cost :.2f} leva")
