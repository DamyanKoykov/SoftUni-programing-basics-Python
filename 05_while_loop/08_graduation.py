student_name = input()

year = 1
fail_counter = 0
average_grade = 0
grade_sum = 0
while year <= 12:
    grade = float(input())
    if grade < 4:
        fail_counter += 1
        if fail_counter == 2:
            print(f"{student_name} has been excluded at {year} grade")
            break
        continue
    year += 1
    grade_sum += grade
    average_grade = grade_sum / 12
    if year > 12:
        print(f"{student_name} graduated. Average grade: {average_grade :.2f}")
        break
