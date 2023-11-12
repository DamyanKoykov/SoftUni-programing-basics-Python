movie_title = " "
free_seats_count = " "
ticket_type_bought = " "

ticket_bought_total = 0
student_ticket_bought = 0
standard_ticket_bought = 0
kid_ticket_bought = 0

while ticket_type_bought != "Finish":
    movie_title = input()
    if movie_title == "Finish":
        break

    free_seats_count = int(input())

    ticket_type_bought = " "
    ticket_bought_per_movie_total = 0
    while ticket_type_bought != "End" and ticket_bought_per_movie_total < free_seats_count:
        ticket_type_bought = input()
        if ticket_type_bought == "End":
            break

        ticket_bought_total += 1
        ticket_bought_per_movie_total += 1
        if ticket_type_bought == "student":
            student_ticket_bought += 1
        elif ticket_type_bought == "standard":
            standard_ticket_bought += 1
        elif ticket_type_bought == "kid":
            kid_ticket_bought += 1
            
    how_much_full_per_movie = (100 / free_seats_count) * ticket_bought_per_movie_total
    print(f"{movie_title} - {how_much_full_per_movie :.2f}% full.")

student_tickets_percent = (100 / ticket_bought_total) * student_ticket_bought
standard_ticket_percent = (100 / ticket_bought_total) * standard_ticket_bought
kid_ticket_percent = (100 / ticket_bought_total) * kid_ticket_bought

print(f"Total tickets: {ticket_bought_total}")
print(f"{student_tickets_percent :.2f}% student tickets.")
print(f"{standard_ticket_percent :.2f}% standard tickets.")
print(f"{kid_ticket_percent :.2f}% kids tickets.")
