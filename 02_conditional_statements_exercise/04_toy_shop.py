price_of_holiday = float(input())
puzzle_ordered = int(input())
talking_doll_ordered = int(input())
teddy_bear_ordered = int(input())
minion_ordered = int(input())
truck_ordered = int(input())

puzzle_price = 2.60 * puzzle_ordered
talking_doll_price = 3 * talking_doll_ordered
teddy_bear_price = 4.10 * teddy_bear_ordered
minion_price = 8.20 * minion_ordered
truck_price = 2 * truck_ordered

discount = 1
total_toy_ordered = puzzle_ordered + talking_doll_ordered + teddy_bear_ordered + minion_ordered + truck_ordered

if total_toy_ordered >= 50:
    discount = 0.75

rent = ((puzzle_price + talking_doll_price + teddy_bear_price + minion_price + truck_price) * discount) * 0.10

total_profit = ((puzzle_price + talking_doll_price + teddy_bear_price + minion_price + truck_price) * discount) - rent
result = abs(total_profit - price_of_holiday)

if total_profit >= price_of_holiday:
    print(f"Yes! {result :.2f} lv left.")
else:
    print(f"Not enough money! {result :.2f} lv needed.")

