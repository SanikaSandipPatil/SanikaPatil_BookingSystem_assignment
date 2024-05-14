class Event:
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price,
                 event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def calculate_total_revenue(self):
        return self.ticket_price * (self.total_seats - self.available_seats)

    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked successfully for {self.event_name}.")
        else:
            print("Not enough available seats.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled for {self.event_name}.")

    def display_event_details(self):
        print("Event Details:")
        print("Name:", self.event_name)
        print("Date:", self.event_date)
        print("Time:", self.event_time)
        print("Venue:", self.venue_name)
        print("Total Seats:", self.total_seats)
        print("Available Seats:", self.available_seats)
        print("Ticket Price:", self.ticket_price)
        print("Event Type:", self.event_type)


# Example Usage:
if __name__ == "__main__":
    # Creating an Event object
    event = Event("Movie Night", "2024-05-15", "18:00", "Grand Theater", 100, 100, 10.00, "Movie")

    # Display event details
    event.display_event_details()

    # Book tickets
    event.book_tickets(5)
    event.book_tickets(10)

    # Cancel booking
    event.cancel_booking(3)

    # Display updated event details
    event.display_event_details()

    # Calculate total revenue
    revenue = event.calculate_total_revenue()
    print("Total Revenue:", revenue)
