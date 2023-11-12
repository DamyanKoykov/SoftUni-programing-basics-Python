width_mtr = float(input())
height_mtr = float(input())

work_place_width = 120  # cm
work_place_height = 70  # cm
corridor_width = 100  # cm

width_cm = width_mtr * 100
height_cm = height_mtr * 100

fit_in_width = int((width_cm - corridor_width) / work_place_width)
fit_in_height = int(height_cm / work_place_height)

# we remove three workplaces for stage and door
fit_in_total = fit_in_width * fit_in_height - 3

print(fit_in_total)
