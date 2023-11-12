nights_booked = int(input()) - 1  # if we book 11 days we pay 10 nights that is why we take 1 out
type_of_accommodation = input()
rating = input()

room_price = 0
rating_price_adjustment = 1
discount = 1
final_price = 0

# if the rating is positive we tip 25% after discount and if rating is negative we get 10% discount
if rating == "positive":
    rating_price_adjustment = 1 + 0.25
elif rating == "negative":
    rating_price_adjustment = 1 - 0.10

# we calculate discount with days booked not nights that is why we add 1 (look at first row)
if type_of_accommodation == "room for one person":
    room_price = 18.00
elif type_of_accommodation == "apartment":
    room_price = 25.00
    if nights_booked + 1 < 10:
        discount = 1 - 0.30
    elif nights_booked + 1 <= 15:
        discount = 1 - 0.35
    elif nights_booked + 1:
        discount = 1 - 0.50
elif type_of_accommodation == "president apartment":
    room_price = 35.00
    if nights_booked + 1 < 10:
        discount = 1 - 0.10
    elif nights_booked + 1 <= 15:
        discount = 1 - 0.15
    elif nights_booked + 1:
        discount = 1 - 0.20

final_price = (((room_price * nights_booked) * discount) * rating_price_adjustment)
print(f"{final_price :.2f}")
