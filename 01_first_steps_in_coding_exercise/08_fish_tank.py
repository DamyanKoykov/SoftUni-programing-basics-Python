length_of_tank_cm = int(input())
width_of_tank_cm = int(input())
height_of_tank_cm = int(input())
occupied_space_percent = int(input()) / 100

total_volume_from_qubic_mtr_to_ltr = (((length_of_tank_cm * width_of_tank_cm * height_of_tank_cm) / 1000) *
                                      (1 - occupied_space_percent))

print(total_volume_from_qubic_mtr_to_ltr)
