expected_profit = int(input())
command = input()  # End or current item price

transaction_counter = 0
cash_transaction_counter = 0
cash_transaction_total_amount = 0
card_transaction_counter = 0
card_transaction_total_amount = 0
current_profit = 0
is_it_enough = False

while command != "End":
    current_item_price = int(command)
    transaction_counter += 1
    if transaction_counter % 2 != 0 and current_item_price > 100:  # unsuccessful cash payment
        print("Error in transaction!")
    elif transaction_counter % 2 == 0 and current_item_price < 10:  # unsuccessful card payment
        print("Error in transaction!")
    else:
        current_profit += current_item_price
        print("Product sold!")
        if transaction_counter % 2 != 0:  # successful cash payment
            cash_transaction_counter += 1
            cash_transaction_total_amount += current_item_price
        else:  # successful card payment
            card_transaction_counter += 1
            card_transaction_total_amount += current_item_price
    if current_profit >= expected_profit:
        is_it_enough = True
        break

    command = input()

if is_it_enough:
    avg_cash_transaction = cash_transaction_total_amount / cash_transaction_counter
    avg_card_transaction = card_transaction_total_amount / card_transaction_counter
    print(f"Average CS: {avg_cash_transaction :.2f}")
    print(f"Average CC: {avg_card_transaction :.2f}")
elif command == "End":
    print("Failed to collect required money for charity.")
