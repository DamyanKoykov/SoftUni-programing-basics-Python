degrees = float(input())

weather = ""
if 5 <= degrees <= 11.9:
    weather = "Cold"
elif 12 <= degrees <= 14.9:
    weather = "Cool"
elif 15 <= degrees <= 20:
    weather = "Mild"
elif 20.1 <= degrees <= 25.9:
    weather = "Warm"
elif 26 <= degrees <= 35:
    weather = "Hot"
else:
    weather = "unknown"

print(weather)
