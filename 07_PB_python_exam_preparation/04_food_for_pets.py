total_days = int(input())
total_food_available = float(input())

cat_ate_total = 0
dog_ate_total = 0
biscuit_for_the_day = 0
biscuit_total_eaten = 0
for day_counter in range(1, total_days + 1):
    dog_ate_current_day = float(input())
    cat_ate_current_day = float(input())
    dog_ate_total += dog_ate_current_day
    cat_ate_total += cat_ate_current_day
    if day_counter % 3 == 0:
        biscuit_for_the_day = (dog_ate_current_day + cat_ate_current_day) * 0.10
        biscuit_total_eaten += biscuit_for_the_day

total_food_eaten = dog_ate_total + cat_ate_total
percent_food_eaten = (100 / total_food_available) * total_food_eaten
percent_that_dog_ate = (100 / total_food_eaten) * dog_ate_total
percent_that_cat_ate = (100 / total_food_eaten) * cat_ate_total
print(f"Total eaten biscuits: {round(biscuit_total_eaten)}gr.")
print(f"{percent_food_eaten :.2f}% of the food has been eaten.")
print(f"{percent_that_dog_ate :.2f}% eaten from the dog.")
print(f"{percent_that_cat_ate :.2f}% eaten from the cat.")
