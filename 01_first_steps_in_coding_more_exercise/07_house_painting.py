wall_height = float(input())
wall_length = float(input())
roof_height = float(input())

green_wall_paint_sqm_per_ltr = 3.4
red_roof_paint_sqm_per_ltr = 4.3

front_and_back_walls_area = (wall_height * wall_height) * 2
front_door_area = 1.2 * 2
side_walls_area = (wall_length * wall_height) * 2
side_window_area = (1.5 * 1.5) * 2
side_roof_area = side_walls_area
front_and_back_roof_area = wall_height * roof_height

total_wall_area = (front_and_back_walls_area - front_door_area) + (side_walls_area - side_window_area)
total_roof_area = side_roof_area + front_and_back_roof_area
total_green_wall_paint_ltr = total_wall_area / green_wall_paint_sqm_per_ltr
total_red_roof_paint_ltr = total_roof_area / red_roof_paint_sqm_per_ltr

print(f"{total_green_wall_paint_ltr :.2f}")
print(f"{total_red_roof_paint_ltr :.2f}")
