student_count = int(input())

first_student_count = 0
second_place_student = 0
third_place_student = 0
fail_place_student = 0
total_grade_sum = 0
for _ in range(student_count):
    current_student_grade = float(input())
    if current_student_grade < 3:
        fail_place_student += 1
    elif current_student_grade <= 3.99:
        third_place_student += 1
    elif current_student_grade <= 4.99:
        second_place_student += 1
    else:
        first_student_count += 1
    total_grade_sum += current_student_grade

first_student_percent = (100 / student_count) * first_student_count
second_place_percent = (100 / student_count) * second_place_student
third_place_percent = (100 / student_count) * third_place_student
fail_place_percent = (100 / student_count) * fail_place_student
avg_grade = total_grade_sum / student_count

print(f"Top students: {first_student_percent :.2f}%")
print(f"Between 4.00 and 4.99: {second_place_percent :.2f}%")
print(f"Between 3.00 and 3.99: {third_place_percent :.2f}%")
print(f"Fail: {fail_place_percent :.2f}%")
print(f"Average: {avg_grade :.2f}")
