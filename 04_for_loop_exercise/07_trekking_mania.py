groups_count = int(input())

total_amount_people = 0
musala_group_count = 0
monblan_group_count = 0
kilimandjaro_group_count = 0
k2_group_count = 0
everest_group_count = 0

for group_counter in range(groups_count):
    people_per_group = int(input())
    total_amount_people += people_per_group

    if people_per_group <= 5:
        musala_group_count += people_per_group
    elif people_per_group <= 12:
        monblan_group_count += people_per_group
    elif people_per_group <= 25:
        kilimandjaro_group_count += people_per_group
    elif people_per_group <= 40:
        k2_group_count += people_per_group
    elif people_per_group > 40:
        everest_group_count += people_per_group

musala_group_percent = 100 / total_amount_people * musala_group_count
monblan_group_percent = 100 / total_amount_people * monblan_group_count
kilimandjaro_group_percent = 100 / total_amount_people * kilimandjaro_group_count
k2_group_percent = 100 / total_amount_people * k2_group_count
everest_group_percent = 100 / total_amount_people * everest_group_count

print(f"{musala_group_percent :.2f}%")
print(f"{monblan_group_percent :.2f}%")
print(f"{kilimandjaro_group_percent :.2f}%")
print(f"{k2_group_percent :.2f}%")
print(f"{everest_group_percent :.2f}%")
