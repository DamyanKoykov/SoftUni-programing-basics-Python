# password format is abcd

m_control_value = int(input())
fourth_password_is = ""
password_counter = 0
did_you_find_password = False
passwords_list = []

for a in range(1, 9 + 1):  # abcd are all in range 1 to 9
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if (a * b) + (c * d) == m_control_value:
                    if a < b and c > d:
                        current_password = f"{a}{b}{c}{d}"
                        passwords_list.append(current_password)
                        did_you_find_password = True
                        password_counter += 1
                        if password_counter == 4:
                            fourth_password_is = f"Password: {a}{b}{c}{d}"

print(" ".join(passwords_list))
if fourth_password_is != "":
    print(fourth_password_is)
elif not did_you_find_password or fourth_password_is == "":
    print("No!")
