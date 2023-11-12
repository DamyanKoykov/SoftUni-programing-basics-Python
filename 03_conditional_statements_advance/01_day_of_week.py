day_of_week_number = int(input())

day_of_week = ""
if day_of_week_number == 1:
    day_of_week = "Monday"
elif day_of_week_number == 2:
    day_of_week = "Tuesday"
elif day_of_week_number == 3:
    day_of_week = "Wednesday"
elif day_of_week_number == 4:
    day_of_week = "Thursday"
elif day_of_week_number == 5:
    day_of_week = "Friday"
elif day_of_week_number == 6:
    day_of_week = "Saturday"
elif day_of_week_number == 7:
    day_of_week = "Sunday"
else:
    print("Error")

print(day_of_week)
