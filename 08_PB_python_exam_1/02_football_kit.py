t_shirt_price = float(input())
how_much_to_win_prize = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (t_shirt_price + shorts_price) * 2

total_order_cost = (t_shirt_price + shorts_price + socks_price + shoes_price) * (1 - 0.15)  # total plus discount 15%
difference = how_much_to_win_prize - total_order_cost

if total_order_cost >= how_much_to_win_prize:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_order_cost :.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference :.2f} lv. more.")
