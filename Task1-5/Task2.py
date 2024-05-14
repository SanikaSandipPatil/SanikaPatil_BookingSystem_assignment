def calculate_ticket_cost(ticket_type, no_of_tickets):
    base_prices = {"Silver": 50, "Gold": 100, "Diamond": 200}

    if ticket_type in base_prices:
        base_price = base_prices[ticket_type]
        total_cost = base_price * no_of_tickets
        return total_cost
    else:
        print("Invalid ticket type.")


def main():
    print("Welcome to the Ticket Booking System!")
    print("Ticket options: Silver, Gold, Diamond")

    ticket_type = input("Enter the type of ticket you want to book: ")
    no_of_tickets = int(input("Enter the number of tickets you want to book: "))

    total_cost = calculate_ticket_cost(ticket_type, no_of_tickets)
    if total_cost is not None:
        print("Total cost:", total_cost)


if __name__ == "__main__":
    main()
