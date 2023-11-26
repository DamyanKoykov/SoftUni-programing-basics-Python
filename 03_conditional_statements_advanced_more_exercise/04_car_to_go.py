budget = float(input())
season = input()

class_of_car = ""
vehicle_type = ""
price = 0
if budget <= 100:
    class_of_car = "Economy class"
    if season == "Summer":
        vehicle_type = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        vehicle_type = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    class_of_car = "Compact class"
    if season == "Summer":
        vehicle_type = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        vehicle_type = "Jeep"
        price = budget * 0.80
elif 500 < budget:
    class_of_car = "Luxury class"
    vehicle_type = "Jeep"
    price = budget * 0.90

print(class_of_car)
print(f"{vehicle_type} - {price :.2f}")
