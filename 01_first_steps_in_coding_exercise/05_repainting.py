PROTECTIVE_FILM_PRICE_PSQM = 1.5
PAINT_PRICE = 14.5
PAINT_DISSOLVER_PRICE = 5
CARRIER_BAG_PRICE = 0.4

protective_film_needed_sqm = int(input())
paint_needed = int(input())
paint_dissolver_needed = int(input())
hours_needed = int(input())

# we are adding additional 2sqm of protective film
total_price_for_protective_film = (protective_film_needed_sqm + 2) * PROTECTIVE_FILM_PRICE_PSQM
# we are adding additional 10% of paint
total_price_for_for_paint = ((paint_needed + (paint_needed * 0.10)) * PAINT_PRICE)
total_price_for_dissolver = paint_dissolver_needed * PAINT_DISSOLVER_PRICE
# we are adding just one carrier bag
total_price_for_carrier_bag = CARRIER_BAG_PRICE * 1

# The people get paid 30% of material price per hour
pay_per_hour = (
                           total_price_for_protective_film + total_price_for_for_paint + total_price_for_dissolver + CARRIER_BAG_PRICE) * 0.3
total_price_of_labour = pay_per_hour * hours_needed

total_price_of_repainting = (total_price_of_labour + total_price_for_carrier_bag + total_price_for_dissolver +
                             total_price_for_for_paint + total_price_for_protective_film)

print(total_price_of_repainting)
