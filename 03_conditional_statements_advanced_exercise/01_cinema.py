type_of_movie = input()
rows_quantity = int(input())
columns_quantity = int(input())

ticket_price = 0
if type_of_movie == "Premiere":
    ticket_price = 12
elif type_of_movie == "Normal":
    ticket_price = 7.50
elif type_of_movie == "Discount":
    ticket_price = 5

profit = (rows_quantity * columns_quantity) * ticket_price

print(f"{profit :.2f} leva")
