month = input()
days_booked = int(input())

studio_price_per_night = 0
apartment_price_per_night = 0
discount = 1

if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 7 < days_booked <= 13:
        studio_price_per_night *= (1 - 0.05)
    elif days_booked > 14:
        studio_price_per_night *= (1 - 0.30)
elif month == "June" or month == "September":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if days_booked > 14:
        studio_price_per_night *= (1 - 0.20)
elif month == "July" or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77

if days_booked > 14:
    apartment_price_per_night *= (1 - 0.10)

studio_total_cost = studio_price_per_night * days_booked
apartment_total_cost = apartment_price_per_night * days_booked

print(f"Apartment: {apartment_total_cost :.2f} lv.")
print(f"Studio: {studio_total_cost :.2f} lv.")
