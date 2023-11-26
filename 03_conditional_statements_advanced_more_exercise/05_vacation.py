budget = float(input())
season = input()

accommodation_type = ""
location = ""
price = 0
if budget <= 1_000:
    accommodation_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    if season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif 1_000 < budget <= 3_000:
    accommodation_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    if season == "Winter":
        location = "Morocco"
        price = budget * 0.60
elif 3_000 < budget:
    accommodation_type = "Hotel"
    if season == "Summer":
        location = "Alaska"
    if season == "Winter":
        location = "Morocco"
    price = budget * 0.90

print(f"{location} - {accommodation_type} - {price :.2f}")
