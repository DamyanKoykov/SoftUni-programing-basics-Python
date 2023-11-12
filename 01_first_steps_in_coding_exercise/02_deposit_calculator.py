deposit_amount = float(input())
deposit_period = int(input())
annual_interest_rate = float(input())
total_amount = deposit_amount + deposit_period * ((deposit_amount * (annual_interest_rate / 100)) / 12)

print(total_amount)
