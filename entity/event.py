from datetime import datetime

class Event:
    def __init__(self, event_name, event_date, event_time, venue, total_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue = venue
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    # Getter and Setter methods
    def get_event_name(self):
        return self.event_name

    def set_event_name(self, event_name):
        self.event_name = event_name

    def get_event_date(self):
        return self.event_date

    def set_event_date(self, event_date):
        self.event_date = event_date

    def get_event_time(self):
        return self.event_time

    def set_event_time(self, event_time):
        self.event_time = event_time

    def get_venue(self):
        return self.venue

    def set_venue(self, venue):
        self.venue = venue

    def get_total_seats(self):
        return self.total_seats

    def set_total_seats(self, total_seats):
        self.total_seats = total_seats

    def get_available_seats(self):
        return self.available_seats

    def set_available_seats(self, available_seats):
        self.available_seats = available_seats

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price

    def get_event_type(self):
        return self.event_type

    def set_event_type(self, event_type):
        self.event_type = event_type

    # Other methods
    def calculate_total_revenue(self):
        return self.ticket_price * (self.total_seats - self.available_seats)

    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for the event {self.event_name}.")
        else:
            print("Insufficient seats available.")

    def cancel_booking(self, num_tickets):
        if num_tickets <= self.total_seats - self.available_seats:
            self.available_seats += num_tickets
            print(f"{num_tickets} tickets canceled for the event {self.event_name}.")
        else:
            print("Invalid number of tickets to cancel.")

    def display_event_details(self):
        print("Event Details:")
        print(f"Name: {self.event_name}")
        print(f"Date: {self.event_date.strftime('%Y-%m-%d')}")
        print(f"Time: {self.event_time.strftime('%H:%M')}")
        print(f"Venue: {self.venue.get_venue_name()}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Event Type: {self.event_type}")
