city = input()
sales_quantity = float(input())

total_earning = 0

if city == "Sofia":
    if 0 <= sales_quantity <= 500:
        total_earning = sales_quantity * 0.05
    elif 500 < sales_quantity <= 1000:
        total_earning = sales_quantity * 0.07
    elif 1000 < sales_quantity <= 10000:
        total_earning = sales_quantity * 0.08
    elif sales_quantity > 10000:
        total_earning = sales_quantity * 0.12

elif city == "Varna":
    if 0 <= sales_quantity <= 500:
        total_earning = sales_quantity * 0.045
    elif 500 < sales_quantity <= 1000:
        total_earning = sales_quantity * 0.075
    elif 1000 < sales_quantity <= 10000:
        total_earning = sales_quantity * 0.10
    elif sales_quantity > 10000:
        total_earning = sales_quantity * 0.13

elif city == "Plovdiv":
    if 0 <= sales_quantity <= 500:
        total_earning = sales_quantity * 0.055
    elif 500 < sales_quantity <= 1000:
        total_earning = sales_quantity * 0.08
    elif 1000 < sales_quantity <= 10000:
        total_earning = sales_quantity * 0.12
    elif sales_quantity > 10000:
        total_earning = sales_quantity * 0.145

if total_earning != 0:
    print(f"{total_earning :.2f}")
else:
    print("error")
