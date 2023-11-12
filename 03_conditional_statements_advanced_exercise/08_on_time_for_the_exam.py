hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_time_in_minutes = (hour_of_exam * 60) + minute_of_exam
arrival_time_in_minutes = (hour_of_arrival * 60) + minute_of_arrival

result = abs(exam_time_in_minutes - arrival_time_in_minutes)
result_hour = result // 60
result_minutes = result % 60

if 1 <= result and exam_time_in_minutes < arrival_time_in_minutes:
    print("Late")
    if result <= 59:
        print(f"{result} minutes after the start")
    elif result >= 60:
        print(f"{result_hour}:{result_minutes :02d} hours after the start")

elif result > 30:
    print("Early")
    if result <= 59:
        print(f"{result} minutes before the start")
    elif result >= 60:
        print(f"{result_hour}:{result_minutes :02d} hours before the start")

elif 30 >= result >= 0:
    print("On time")
    if result >= 1:
        print(f"{result} minutes before the start")
