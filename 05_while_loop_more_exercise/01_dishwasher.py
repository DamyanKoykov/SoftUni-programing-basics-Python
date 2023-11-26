dish_washing_liquid_milliliters = int(input()) * 750
command = input()  # End or count of dishes to eb washed

washing_cycles_counter = 1
dish_counter = 0
pot_counter = 0

while command != "End":
    how_much_dishes_current = int(command)

    if washing_cycles_counter % 3 == 0:
        washing_liquid_needed_per_dish = 15
        pot_counter += how_much_dishes_current
    else:
        washing_liquid_needed_per_dish = 5
        dish_counter += how_much_dishes_current

    dish_washing_liquid_milliliters -= (how_much_dishes_current * washing_liquid_needed_per_dish)
    if dish_washing_liquid_milliliters < 0:
        break

    command = input()
    washing_cycles_counter += 1
if dish_washing_liquid_milliliters >= 0:
    print("Detergent was enough!")
    print(f"{dish_counter} dishes and {pot_counter} pots were washed.")
    print(f"Leftover detergent {dish_washing_liquid_milliliters} ml.")
else:
    print(f"Not enough detergent, {abs(dish_washing_liquid_milliliters)} ml. more necessary!")
