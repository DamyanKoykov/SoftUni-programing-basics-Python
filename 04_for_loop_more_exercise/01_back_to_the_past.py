available_money = float(input())
target_year = int(input())

age = 18
for current_year in range(1800, target_year + 1):
    if current_year % 2 == 0:
        available_money -= 12_000
    elif current_year % 2 != 0:
        available_money -= (12_000 + (50 * age))
    age += 1

if available_money >= 0:
    print(f"Yes! He will live a carefree life and will have {available_money :.2f} dollars left.")
else:
    print(f"He will need {abs(available_money) :.2f} dollars to survive.")
