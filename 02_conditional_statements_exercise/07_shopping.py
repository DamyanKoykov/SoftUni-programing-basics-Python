budget = float(input())
video_card_ordered = int(input())
processor_ordered = int(input())
ram_ordered = int(input())

discount = 1
if video_card_ordered > processor_ordered:
    discount = 0.85

video_card_price = 250 * video_card_ordered
processor_price = (video_card_price * 0.35) * processor_ordered
ram_price = (video_card_price * 0.10) * ram_ordered

total_cost = (video_card_price + processor_price + ram_price) * discount
difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"You have {difference :.2f} leva left!")
else:
    print(f"Not enough money! You need {difference :.2f} leva more!")
