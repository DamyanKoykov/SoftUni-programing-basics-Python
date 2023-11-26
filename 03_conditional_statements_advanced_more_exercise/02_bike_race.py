junior_bikers_count = int(input())
senior_bikers_count = int(input())
track_type = input()

senior_membership_price = 0
junior_membership_price = 0
total_bikers_count = junior_bikers_count + senior_bikers_count
if track_type == "trail":
    junior_membership_price = 5.50
    senior_membership_price = 7
elif track_type == "cross-country":
    junior_membership_price = 8
    senior_membership_price = 9.50
    if total_bikers_count >= 50:
        junior_membership_price *= (1 - 0.25)
        senior_membership_price *= (1 - 0.25)
elif track_type == "downhill":
    junior_membership_price = 12.25
    senior_membership_price = 13.75
elif track_type == "road":
    junior_membership_price = 20
    senior_membership_price = 21.50

profit_for_charity = ((junior_bikers_count * junior_membership_price) +
          (senior_bikers_count * senior_membership_price)) * (1 - 0.05)

print(f"{profit_for_charity :.2f}")
