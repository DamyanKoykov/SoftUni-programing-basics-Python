stadium_capacity = int(input())
fan_count = int(input())

a_sector_count = 0
b_sector_count = 0
v_sector_count = 0
g_sector_count = 0

for _ in range(fan_count):
    sector_current_fan = input()  # A, B, V or G
    if sector_current_fan == "A":
        a_sector_count += 1
    elif sector_current_fan == "B":
        b_sector_count += 1
    elif sector_current_fan == "V":
        v_sector_count += 1
    elif sector_current_fan == "G":
        g_sector_count += 1

a_sector_percent = (100 / fan_count) * a_sector_count
b_sector_percent = (100 / fan_count) * b_sector_count
v_sector_percent = (100 / fan_count) * v_sector_count
g_sector_percent = (100 / fan_count) * g_sector_count
fullness_capacity = (100 / stadium_capacity) * fan_count

print(f"{a_sector_percent :.2f}%")
print(f"{b_sector_percent :.2f}%")
print(f"{v_sector_percent :.2f}%")
print(f"{g_sector_percent :.2f}%")
print(f"{fullness_capacity :.2f}%")
