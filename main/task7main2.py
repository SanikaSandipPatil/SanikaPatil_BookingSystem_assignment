from entity.booking_system import BookingSystem
from entity.customer import Customer
from entity.venue import Venue
from datetime import datetime


def main():
    booking_system = BookingSystem()

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
            event_name = input("Enter event name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            total_seats = input("Enter total seats: ")
            while not total_seats.isdigit() or int(total_seats) <= 0:
                print("Invalid input. Please enter a valid positive integer.")
                total_seats = input("Enter total seats: ")
            total_seats = int(total_seats)
            ticket_price = input("Enter ticket price: ")
            while not is_float(ticket_price) or float(ticket_price) <= 0:
                print("Invalid input. Please enter a valid positive floating-point number.")
                ticket_price = input("Enter ticket price: ")
            ticket_price = float(ticket_price)
            event_type = input("Enter event type (Movie/Sport/Concert): ")
            venue_name = input("Enter venue name: ")
            venue_address = input("Enter venue address: ")
            venue = Venue(venue_name, venue_address)
            event = booking_system.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)
            print("Event created successfully.")

        elif choice == "2":
            event_name = input("Enter event name: ")
            num_tickets = input("Enter number of tickets: ")
            while not num_tickets.isdigit() or int(num_tickets) <= 0:
                print("Invalid input. Please enter a valid positive integer.")
                num_tickets = input("Enter number of tickets: ")
            num_tickets = int(num_tickets)
            customers = []
            for i in range(num_tickets):
                print(f"Enter details for Customer {i + 1}:")
                customer_name = input("Name: ")
                email = input("Email: ")
                phone_number = input("Phone Number: ")
                customer = Customer(customer_name, email, phone_number)
                customers.append(customer)
            booking = booking_system.book_tickets(event_name, num_tickets, customers)
            if booking:
                print("Tickets booked successfully. Booking ID:", booking.get_booking_id())
            else:
                print("Event not found or insufficient seats available.")

        elif choice == "3":
            booking_id = input("Enter booking ID: ")
            while not booking_id.isdigit() or int(booking_id) <= 0:
                print("Invalid input. Please enter a valid positive integer.")
                booking_id = input("Enter booking ID: ")
            booking_id = int(booking_id)
            if booking_system.cancel_booking(booking_id):
                print("Booking canceled successfully.")
            else:
                print("Booking not found.")

        elif choice == "4":
            event_name = input("Enter event name: ")
            available_seats = booking_system.get_available_no_of_tickets(event_name)
            if available_seats is not None:
                print("Available seats:", available_seats)
            else:
                print("Event not found.")

        elif choice == "5":
            event_name = input("Enter event name: ")
            event_details = booking_system.get_event_details(event_name)
            if event_details:
                event_details.display_event_details()
            else:
                print("Event not found.")

        elif choice == "6":
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
