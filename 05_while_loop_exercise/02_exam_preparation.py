fail_limit = int(input())

name_of_exercise = ""
grade_counter = 0
grade_sum = 0
average_grade = 0
fail_counter = 0
is_it_enough_switch = False
fail_limiter_switch = False
while not is_it_enough_switch:
    command = input()
    if command == "Enough":
        is_it_enough_switch = True
    else:
        name_of_exercise = command
    grade = int(input())
    grade_counter += 1
    grade_sum += grade
    average_grade = grade_sum / grade_counter
    if grade <= 4:
        fail_counter += 1
        if fail_counter == fail_limit:
            fail_limiter_switch = True
            break

if is_it_enough_switch:
    print(f"Average score: {average_grade :.2f}\nNumber of problems: {grade_counter}\nLast problem: {name_of_exercise}")
elif fail_limiter_switch:
    print(f"You need a break, {fail_counter} poor grades.")
