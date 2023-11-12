annual_tax_price = int(input())
# shoe price is 40% less than annual tax
shoe_price = annual_tax_price * 0.60
# clothes are 20% cheaper than shoe price
clothes_price = shoe_price * 0.80
# basketball proice is one quarter of clothes price
basketball_price = clothes_price / 4
# accessories price is one fifth of basketball_price
accessories_price = basketball_price / 5

total_price = annual_tax_price + shoe_price + clothes_price + basketball_price + accessories_price
print(total_price)
