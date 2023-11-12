hour = int(input())
minutes = int(input())

minutes = minutes + 15

if minutes < 60:
    if minutes < 10:
        print(f"{hour}:0{minutes} ")
    else:
        print(f"{hour}:{minutes} ")
elif minutes >= 60:
    hour = hour + 1
    minutes = abs(60 - minutes)
    if hour > 23:
        hour = 0
    if minutes < 10:
        print(f"{hour}:0{minutes} ")
    else:
        print(f"{hour}:{minutes} ")
