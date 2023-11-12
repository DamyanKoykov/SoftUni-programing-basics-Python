strawberry_price_per_kg = float(input())
banana_quantity_kg = float(input())
orange_quantity_kg = float(input())
raspberry_quantity_kg = float(input())
strawberry_quantity_kg = float(input())

raspberry_price_per_kg = strawberry_price_per_kg / 2
orange_price_per_kg = raspberry_price_per_kg * 0.60
banana_price_per_kg = raspberry_price_per_kg * 0.20

total_cost = (strawberry_quantity_kg * strawberry_price_per_kg) + (banana_quantity_kg * banana_price_per_kg) + \
             (orange_quantity_kg * orange_price_per_kg) + (raspberry_quantity_kg * raspberry_price_per_kg)

print(total_cost)
