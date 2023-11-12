day_of_week = input()

workday_or_weekend = ""
if (day_of_week == "Monday"
        or day_of_week == "Tuesday"
        or day_of_week == "Wednesday"
        or day_of_week == "Thursday"
        or day_of_week == "Friday"):
    workday_or_weekend = "Working day"

elif day_of_week == "Saturday" or day_of_week == "Sunday":
    workday_or_weekend = "Weekend"

else:
    print("Error")

print(workday_or_weekend)
