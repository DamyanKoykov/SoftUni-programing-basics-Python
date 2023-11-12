jury_count = int(input())
name_of_presentation = input()

grade_counter = 0
grade_per_presentation_sum = 0
grade_per_presentation_sum_for_total_average = 0

while name_of_presentation != "Finish":
    average_grade_for_presentation = 0
    grade_per_presentation_sum = 0
    for jury_counter in range(jury_count):
        grade = float(input())
        grade_counter += 1
        grade_per_presentation_sum += grade
        grade_per_presentation_sum_for_total_average += grade
        average_grade_for_presentation = grade_per_presentation_sum / jury_count
    print(f"{name_of_presentation} - {average_grade_for_presentation :.2f}.")
    name_of_presentation = input()

if name_of_presentation == "Finish":
    average_total = grade_per_presentation_sum_for_total_average / grade_counter
    print(f"Student's final assessment is {average_total :.2f}.")
