hriznatemi_count = int(input())
roses_count = int(input())
laleta_count = int(input())
season = input()
is_it_praznik = input()  # Y or N

if season == "Spring" or season == "Summer":
    hriznatemi_price = 2
    roses_price = 4.10
    laleta_price = 2.50
elif season == "Autumn" or season == "Winter":
    hriznatemi_price = 3.75
    roses_price = 4.50
    laleta_price = 4.15

total_price = (hriznatemi_count * hriznatemi_price) + (roses_count * roses_price) + (laleta_count * laleta_price)
total_flower_count = hriznatemi_count + roses_count + laleta_count
if is_it_praznik == "Y":
    total_price *= (1 + 0.15)  # if it is praznik the price goes up 15%
if laleta_count > 7 and season == "Spring":
    total_price *= (1 - 0.05)
if roses_count >= 10 and season == "Winter":
    total_price *= (1 - 0.10)
if total_flower_count > 20:
    total_price *= (1 - 0.20)

final_price = total_price + 2  # 2lv fee for making the bouquet

print(f"{final_price :.2f}")
