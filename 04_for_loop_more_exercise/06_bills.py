water_bill_per_month = 20
water_bill_total = 0
internet_bill_per_month = 15
internet_bill_total = 0
electric_bill_total = 0

time_period_months = int(input())
for _ in range(time_period_months):
    electric_bill_current = float(input())
    electric_bill_total += electric_bill_current
    water_bill_total = water_bill_per_month * time_period_months
    internet_bill_total = internet_bill_per_month * time_period_months

#  we add all bills together and add 20% on top to calculate other expenses
other_bill_total = (electric_bill_total + water_bill_total + internet_bill_total) * (1 + 0.20)
all_bill_total = electric_bill_total + water_bill_total + internet_bill_total + other_bill_total
avg_per_month = all_bill_total / time_period_months

print(f"Electricity: {electric_bill_total :.2f} lv")
print(f"Water: {water_bill_total :.2f} lv")
print(f"Internet: {internet_bill_total :.2f} lv")
print(f"Other: {other_bill_total :.2f} lv")
print(f"Average: {avg_per_month :.2f} lv")
