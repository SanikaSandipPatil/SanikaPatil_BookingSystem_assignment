def book_tickets(available_tickets, no_of_booking_tickets):
    if available_tickets >= no_of_booking_tickets:
        remaining_tickets = available_tickets - no_of_booking_tickets
        print("Tickets booked successfully!")
        print("Remaining tickets:", remaining_tickets)
    else:
        print("Ticket unavailable. Available tickets:", available_tickets)


def main():
    available_tickets = int(input("Enter the number of available tickets: "))
    no_of_booking_tickets = int(input("Enter the number of tickets you want to book: "))

    book_tickets(available_tickets, no_of_booking_tickets)


if __name__ == "__main__":
    main()
