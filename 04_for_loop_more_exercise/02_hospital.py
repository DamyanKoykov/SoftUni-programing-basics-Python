how_many_days = int(input())
patient_to_do_current_day = int(input())
doctors_count = 7

patient_done_current_day = 0
patient_undone_current_day = 0
patient_undone_total = 0
patient_done_total = 0
for day_counter in range(1, how_many_days + 1):
    if day_counter % 3 == 0 and patient_undone_total > patient_done_total:
        doctors_count += 1

    if patient_to_do_current_day >= doctors_count:
        patient_done_current_day = doctors_count
        patient_undone_total += (patient_to_do_current_day - doctors_count)
    elif patient_to_do_current_day < doctors_count:
        patient_done_current_day = patient_to_do_current_day
    patient_done_total += patient_done_current_day

    if day_counter == how_many_days:
        break

    patient_to_do_current_day = int(input())

print(f"Treated patients: {patient_done_total}.")
print(f"Untreated patients: {patient_undone_total}.")
