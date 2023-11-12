import math

days_count = int(input())
km_run_first_day = float(input())

total_km_current = km_run_first_day
total_km = km_run_first_day
for _ in range(days_count):
    percent_to_add_for_current_day = float(input())
    total_km_current += ((total_km_current / 100) * percent_to_add_for_current_day)
    total_km += total_km_current

difference = abs(1_000 - total_km)
if total_km >= 1_000:
    print(f"You've done a great job running {math.ceil(difference)} more kilometers!")
if total_km < 1_000:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(difference)} more kilometers")
