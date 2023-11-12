CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

chicken_menu_ordered = int(input()) * CHICKEN_MENU_PRICE
fish_menu_ordered = int(input()) * FISH_MENU_PRICE
vegetarian_menu_ordered = int(input()) * VEGETARIAN_MENU_PRICE

# dessert price is 20% of total price
desert_price = (chicken_menu_ordered + fish_menu_ordered + vegetarian_menu_ordered) * 0.20

final_price = chicken_menu_ordered + fish_menu_ordered + vegetarian_menu_ordered + desert_price + DELIVERY_PRICE

print(final_price)
