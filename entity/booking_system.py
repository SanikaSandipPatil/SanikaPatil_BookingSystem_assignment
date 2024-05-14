from .event import Event
from .booking import Booking
from datetime import datetime

class BookingSystem:
    def __init__(self):
        self.events = []
        self.bookings = []

    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue):
        event_date = datetime.strptime(date, "%Y-%m-%d")
        event_time = datetime.strptime(time, "%H:%M")
        event = Event(event_name, event_date, event_time, venue, total_seats, ticket_price, event_type)
        self.events.append(event)
        return event

    def calculate_booking_cost(self, num_tickets, ticket_price):
        return num_tickets * ticket_price

    def book_tickets(self, event_name, num_tickets, array_of_customers):
        for event in self.events:
            if event.get_event_name() == event_name:
                total_cost = self.calculate_booking_cost(num_tickets, event.get_ticket_price())
                booking = Booking(array_of_customers, event, num_tickets, total_cost)
                event.book_tickets(num_tickets)
                return booking
        return None

    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking.get_booking_id() == booking_id:
                self.bookings.remove(booking)
                booking.get_event().cancel_booking(booking.get_num_tickets())
                return True
        print("Booking not found.")
        return False

    def get_available_no_of_tickets(self, event_name):
        for event in self.events:
            if event.get_event_name() == event_name:
                return event.get_available_seats()
        return None

    def get_event_details(self, event_name):
        for event in self.events:
            if event.get_event_name() == event_name:
                return event
        return None

    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking.get_booking_id() == booking_id:
                self.bookings.remove(booking)
                booking.get_event().cancel_booking(booking.get_num_tickets())
                return True
        print("Booking not found.")
        return False

