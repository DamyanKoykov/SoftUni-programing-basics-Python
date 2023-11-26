season = input()  # “Winter”, “Spring” или “Summer”
type_of_group = input()  # “boys”, “girls” или “mixed”
students_count = int(input())
nights_count = int(input())

price_per_night = 0
if type_of_group == "boys" or type_of_group == "girls":
    if season == "Winter":
        price_per_night = 9.60
    elif season == "Spring":
        price_per_night = 7.20
    elif season == "Summer":
        price_per_night = 15
elif type_of_group == "mixed":
    if season == "Winter":
        price_per_night = 10
    elif season == "Spring":
        price_per_night = 9.50
    elif season == "Summer":
        price_per_night = 20

total_price = (students_count * price_per_night) * nights_count
if 10 <= students_count < 20:
    total_price *= (1 - 0.05)
elif 20 <= students_count < 50:
    total_price *= (1 - 0.15)
elif 50 <= students_count:
    total_price *= (1 - 0.50)

sport_type = ""
if type_of_group == "girls":
    if season == "Winter":
        sport_type = "Gymnastics"
    elif season == "Spring":
        sport_type = "Athletics"
    elif season == "Summer":
        sport_type = "Volleyball"
elif type_of_group == "boys":
    if season == "Winter":
        sport_type = "Judo"
    elif season == "Spring":
        sport_type = "Tennis"
    elif season == "Summer":
        sport_type = "Football"
elif type_of_group == "mixed":
    if season == "Winter":
        sport_type = "Ski"
    elif season == "Spring":
        sport_type = "Cycling"
    elif season == "Summer":
        sport_type = "Swimming"

print(f"{sport_type} {total_price :.2f} lv.")
