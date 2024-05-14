from dao.i_booking_system_service_provider import IBookingSystemServiceProvider
from dao.i_event_service_provider import IEventServiceProvider
from entity.booking import Booking
from entity.customer import Customer
from entity.event import Event
from entity.venue import Venue
from datetime import datetime

def main():
    # Initialize dependencies
    db_conn = DBUtil.get_db_conn()
    event_service_provider = IEventServiceProvider()
    booking_service_provider = IBookingSystemServiceProvider()
    booking_system_repository = IBookingSystemRepository(db_conn)
    ticket_booking_system = TicketBookingSystem(event_service_provider, booking_service_provider, booking_system_repository)

    # User interface loop
    while True:
        print("\nTicket Booking System Menu:")
        print("1. Create Event")
        print("2. Book Tickets")
        print("3. Cancel Booking")
        print("4. Get Available Seats")
        print("5. Get Event Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Get event details from user
            event_name = input("Enter event name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            total_seats = int(input("Enter total seats: "))
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type (Movie/Sport/Concert): ")
            venue_name = input("Enter venue name: ")
            venue_address = input("Enter venue address: ")
            venue = Venue(venue_name, venue_address)

            # Call ticket_booking_system.create_event() to create the event
            event = ticket_booking_system.create_event(event_name, date, time, total_seats, ticket_price, event_type,
                                                       venue)
            print("Event created successfully.")

        elif choice == "2":
            # Get booking details from user
            event_name = input("Enter event name: ")
            num_tickets = int(input("Enter number of tickets: "))
            customers = []
            for i in range(num_tickets):
                print(f"Enter details for Customer {i + 1}:")
                customer_name = input("Name: ")
                email = input("Email: ")
                phone_number = input("Phone Number: ")
                customer = Customer(customer_name, email, phone_number)
                customers.append(customer)

            # Call ticket_booking_system.book_tickets() to book tickets
            booking = ticket_booking_system.book_tickets(event_name, num_tickets, customers)
            if booking:
                print("Tickets booked successfully. Booking ID:", booking.get_booking_id())
            else:
                print("Event not found or insufficient seats available.")

        elif choice == "3":
            # Get booking ID from user
            booking_id = int(input("Enter booking ID: "))

            # Call ticket_booking_system.cancel_booking() to cancel booking
            if ticket_booking_system.cancel_booking(booking_id):
                print("Booking canceled successfully.")
            else:
                print("Booking not found.")

        elif choice == "4":
            # Call ticket_booking_system.get_available_no_of_tickets() to get available seats
            available_seats = ticket_booking_system.get_available_no_of_tickets()
            if available_seats is not None:
                print("Available seats:", available_seats)
            else:
                print("Event not found.")

        elif choice == "5":
            # Call ticket_booking_system.get_event_details() to get event details
            event_details = ticket_booking_system.get_event_details()
            for event in event_details:
                event.display_event_details()

        elif choice == "6":
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
