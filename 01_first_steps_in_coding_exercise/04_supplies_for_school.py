PEN_PRICE = 5.8
MARKER_PRICE = 7.2
CLEANING_LIQUID_PRICE = 1.2

pens = int(input()) * PEN_PRICE
markers = int(input()) * MARKER_PRICE
cleaning_liquid_liters = int(input()) * CLEANING_LIQUID_PRICE
discount = int(input()) / 100

final_price = pens + markers + cleaning_liquid_liters
discounted_price = final_price - (final_price * discount)

print(discounted_price)
