vegetable_price = float(input())
fruit_price = float(input())
vegetable_quantity = int(input())
fruit_quantity = int(input())

profit_bgn = vegetable_quantity * vegetable_price + fruit_quantity * fruit_price
profit_euro = profit_bgn / 1.94

print(f"{profit_euro:.2f}")
