season = input()
km_per_month = float(input())

profit_per_km = 0
if km_per_month <= 5_000:
    if season == "Spring" or season == "Autumn":
        profit_per_km = 0.75
    elif season == "Summer":
        profit_per_km = 0.90
    elif season == "Winter":
        profit_per_km = 1.05
elif 5_000 < km_per_month <= 10_000:
    if season == "Spring" or season == "Autumn":
        profit_per_km = 0.95
    elif season == "Summer":
        profit_per_km = 1.10
    elif season == "Winter":
        profit_per_km = 1.25
elif 10_000 < km_per_month <= 20_000:
    profit_per_km = 1.45

profit = ((km_per_month * 4) * profit_per_km) * (1 - 0.10)  # the season is 4 months and he pays 10% tax
print(f"{profit :.2f}")
